# Scrip para enviar e-mails. 

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_email(remetente=None, senha=None, destinatario=None, assunto=None, corpo=None):
    """Envia um e-mail simples via SMTP (Gmail). Retorna True se enviado com sucesso, False caso contrário.

    Nota: não deixe credenciais hardcoded; prefira variáveis de ambiente (ver README).
    """
    # Configurar a mensagem
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto

    # Adicionar o corpo do e-mail
    msg.attach(MIMEText(corpo, 'plain'))

    # Permitir obter credenciais a partir de variáveis de ambiente quando não fornecidas
    if remetente is None:
        remetente = os.environ.get('EMAIL_USER')
    if senha is None:
        senha = os.environ.get('EMAIL_PASS')

    servidor = None
    try:
        # Conectar ao servidor SMTP do Gmail
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        
        # Fazer login na conta de e-mail
        if not remetente or not senha:
            raise ValueError('Credenciais de e-mail não informadas (remetente/senha). Use variáveis de ambiente EMAIL_USER e EMAIL_PASS ou passe como parâmetros).')
        servidor.login(remetente, senha)
        
        # Enviar o e-mail
        servidor.send_message(msg)
        print('E-mail enviado com sucesso!')
    except Exception as e:
        print(f'Erro ao enviar e-mail: {e}')
        return False
    finally:
        if servidor:
            servidor.quit()

    return True

# Exemplo de uso
# Exemplo de uso (ordem correta dos parâmetros abaixo)
if __name__ == '__main__':
    enviar_email(
        'seu_email@gmail.com',  # remetente
        'SUA_SENHA_OU_APP_PASSWORD',  # senha/app password
        'destinatario@example.com',  # destinatário
        'Relatório Semanal',  # assunto
        'Aqui está o relatório semanal em anexo.'  # corpo
    )
