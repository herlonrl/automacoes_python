# Este script combina web scraping com envio de e-mails para monitorar preços de produtos e notificar quando o preço cair abaixo do valor desejado.

import requests
from bs4 import BeautifulSoup
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def verificar_preco(url, preco_desejado, seletor_css):
    # Fazer requisição para o site
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    resposta = requests.get(url, headers=headers)
    
    # Analisar o HTML
    soup = BeautifulSoup(resposta.text, 'html.parser')
    
    # Encontrar o elemento de preço
    preco_elemento = soup.select_one(seletor_css)
    
    if not preco_elemento:
        print('Elemento de preço não encontrado.')
        return None
    
    # Extrair o texto do preço e convertê-lo para float
    preco_texto = preco_elemento.get_text().strip().replace('R$', '').replace(',', '.')
    
    try:
        preco_atual = float(preco_texto)
        return preco_atual
    except ValueError:
        print('Erro ao converter o preço para float.')
        return None
    
def enviar_alerta(preco, produto, url, remetente=None, senha=None, destinatario=None):
    # Configuração de e-mail
    # Permite obter credenciais a partir de variáveis de ambiente se não fornecidas
    import os
    remetente = remetente or os.environ.get('EMAIL_USER')
    senha = senha or os.environ.get('EMAIL_PASS')
    destinatario = destinatario or os.environ.get('EMAIL_DEST')
    
    # Montar mensagem
    assunto = f'Alerta de Preço: {produto} agora por R$ {preco}'
    corpo = f'O preço do produto "{produto}" caiu para R$ {preco}.\nConfira o link: {url}' 
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto
    msg.attach(MIMEText(corpo, 'plain'))
    
    # Enviar e-mail
    servidor = None
    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
            if not remetente or not senha or not destinatario:
                raise ValueError('Credenciais/recipient não configurados. Use variáveis de ambiente EMAIL_USER, EMAIL_PASS e EMAIL_DEST ou passe como parâmetros.')
            servidor.login(remetente, senha)
        servidor.send_message(msg)
        print('Alerta de preço enviado!')
    finally:
        if servidor:
            servidor.quit()
    
def monitorar_preco(url, preco_desejado, seletor_css, produto, intervalo, remetente=None, senha=None, destinatario=None):
    print(f'Monitorando o preço de "{produto}"...')
    
    while True:
        try:
            preco_atual = verificar_preco(url, preco_desejado, seletor_css)
            if preco_atual is not None:
                print(f'Preço atual de "{produto}": R$ {preco_atual}')
                if preco_atual <= preco_desejado:
                    enviar_alerta(preco_atual, produto, url, remetente=remetente, senha=senha, destinatario=destinatario)
                    break
            time.sleep(intervalo)
        except Exception as e:
            print(f'Erro ao monitorar o preço: {e}')
            time.sleep(intervalo) 
            
# Exemplo de uso
monitorar_preco(
    url='https://www.exemplo.com/produto',
    preco_desejado=150.00,
    seletor_css='.preco-produto',  # Ajuste conforme a estrutura do site
    produto='Nome do Produto',
    intervalo=3600  # Verificar a cada hora
)

if __name__ == '__main__':
    monitorar_preco(
        url='https://www.exemplo.com/produto',
        preco_desejado=150.00,
        seletor_css='.preco-produto',  # Ajuste conforme a estrutura do site
        produto='Nome do Produto',
        intervalo=3600  # Verificar a cada hora
    )
