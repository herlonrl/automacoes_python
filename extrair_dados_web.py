# Este scrip acessa um site de notícias, analisa o HTML e extrai os títulos das manchetes. 
# O mesmo princípio pode ser aplicado para extrair preços de produtos, dados de clima, cotações de ações e muito mais.
# Requer as bibliotecas requests e BeautifulSoup4.
# pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

def extrair_noticias(url):
    # FAzer requisição para o site
    try:
        resposta = requests.get(url, timeout=10)
    except Exception as e:
        print(f'Erro ao fazer requisição: {e}')
        return []
    
    # Verificar se a requisição foi bem-sucedida
    if resposta.status_code != 200:
        print(f'Erro ao acessar o site: {resposta.status_code}')
        return []
    
    # Analisar o HTML
    soup = BeautifulSoup(resposta.text, 'html.parser')
    
    # Encontrar o títulos da noticias (ajuste o seletor conforme a estrutura do site)
    titulos = soup.select('.feed-item-header a')
    
    # Extrair o texto dos títulos
    noticias = []
    for titulo in titulos:
        noticias.append(titulo.text)
    return noticias

if __name__ == '__main__':
    noticias = extrair_noticias('https://g1.globo.com/')
    for i, noticia in enumerate(noticias, 1):
        print(f'{i}. {noticia}')
