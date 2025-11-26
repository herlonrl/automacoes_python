# automacoes_python
Coleção de scripts simples e práticos para automatizar tarefas comuns em sistemas pessoais (Linux/Windows).

Conteúdo
1. Organizando arquivos automaticamente
2. Automatizando backups
3. Renomeando arquivos em lote
4. Extraindo dados de páginas web
5. Automatizando envio de e-mails
6. Monitoramento de preços de produtos online

Referência / inspiração
https://academify.com.br/automatizando-tarefas-com-python/

---

Visão geral
Este repositório contém pequenos scripts em Python que demonstram automações práticas e facilmente adaptáveis: mover e organizar arquivos, renomear em lote, copiar backups, extrair dados web com requests + BeautifulSoup, enviar e-mails via SMTP e monitorar preços online com alerta por e-mail.

Requisitos
- Python 3.8+
- pip (para instalar dependências opcionais)

Dependências (instalar se for usar scraping ou monitoramento que precisa de requests/BeautifulSoup):

```bash
pip install requests beautifulsoup4
```

Observações de segurança
- Evite deixar senhas em texto puro dentro dos scripts (ex.: credenciais de e-mail). Prefira variáveis de ambiente ou arquivos de configuração protegidos.
- Para envio via Gmail, gere uma senha de app (App Password) em sua conta Google e use-a em vez da senha principal, se a verificação em duas etapas estiver ativada.

---

Descrição dos scripts

1) renomar_arquivos.py ✅
- Função principal: renomear_arquivos(diretorio, prefixo, iniciar_em=1)
- O que faz: lista os arquivos do diretório, ordena e renomeia para prefixo_XXX.ext (XXX = número sequencial com 3 dígitos).
- Exemplo de uso:
```py
from renomar_arquivos import renomear_arquivos
renomear_arquivos('/caminho/para/seu/diretorio', 'foto', 1)
```
- Dica: você pode filtrar por extensão (ex.: apenas .jpg) alterando a lista de arquivos no script.

2) organizando_arquivos.py ✅
- Função principal: organizar_arquivos(diretorio)
- O que faz: detecta tipos por extensão e move arquivos para pastas categorizadas (Imagens, Documentos, Videos, Musicas, Arquivos_Comprimidos, Scripts).
- Exemplo de uso:
```py
from organizando_arquivos import organizar_arquivos
organizar_arquivos('/caminho/para/seu/diretorio')
```

3) automatizando_backups.py ✅
- Função principal: fazer_backup(pasta_origem, pasta_destino)
- O que faz: cria uma pasta com timestamp em `pasta_destino` e copia arquivos e subpastas de `pasta_origem` para lá (shutil.copy2 / shutil.copytree).
- Observação: no código original há uma pequena inconsistência de nome de variável (`paste_destino`), então verifique o parâmetro ao chamar a função.
- Exemplo:
```py
from automatizando_backups import fazer_backup
fazer_backup('/caminho/para/pasta_origem', '/caminho/para/pasta_destino')
```

4) extrair_dados_web.py ✅
- Função principal: extrair_noticias(url)
- O que faz: usa requests + BeautifulSoup para obter títulos/elementos a partir de um seletor (o exemplo usa `.feed-item-header a`).
- Dependências: requests, beautifulsoup4
- Exemplo:
```py
from extrair_dados_web import extrair_noticias
noticias = extrair_noticias('https://g1.globo.com/')
for i, n in enumerate(noticias, 1):
	print(i, n)
```

5) envio_email.py ✅
- Função principal: enviar_email(remetente, senha, destinatario, assunto, corpo)
- O que faz: monta um MIME e envia via servidor SMTP (ex.: smtp.gmail.com:587). O script original traz um exemplo com parâmetros fora de ordem — atente para a assinatura correta.
- Exemplo correto:
```py
from envio_email import enviar_email
remetente = 'seu_email@gmail.com'
senha = 'SENHA_OU_APP_PASSWORD'
destinatario = 'destino@example.com'
assunto = 'Relatório Semanal'
corpo = 'Aqui está o relatório semanal.'
enviar_email(remetente, senha, destinatario, assunto, corpo)
```

6) monitorar_precos_online.py ✅
- Funções: verificar_preco(url, preco_desejado, seletor_css), enviar_alerta(preco, produto, url), monitorar_preco(...)
- O que faz: faz scraping do preço via seletor CSS, compara com `preco_desejado` e, se o preço estiver abaixo, envia alerta por e-mail (usa enviar_alerta — com credenciais embutidas em placeholders no script de exemplo).
- Requisitos: requests, beautifulsoup4 e configuração de e-mail válida (ver observações de segurança).
- Exemplo:
```py
from monitorar_precos_online import monitorar_preco
monitorar_preco(
	url='https://www.exemplo.com/produto',
	preco_desejado=150.00,
	seletor_css='.preco-produto',
	produto='Nome do Produto',
	intervalo=3600
)
```

---

Como executar
- Como script único (linha de comando):
```bash
python3 renomar_arquivos.py       # se o script tiver lógica para rodar como main
```
- Importando como módulo (recomendado para reutilização e testes):
```py
from renomar_arquivos import renomear_arquivos
renomear_arquivos('/path', 'prefix')
```

Testes rápidos / como executar (exemplos)

- Instale dependências (se necessário):

```bash
pip install -r requirements.txt
```

- Testar organização de arquivos (modo direto):

```bash
python3 organizando_arquivos.py
# Ajuste o caminho dentro do arquivo ou importe e chame a função em outro script.
```

- Testar renomeação em lote:

```bash
python3 renomar_arquivos.py
# Ajuste o caminho e prefixo dentro do arquivo ou importe a função em um script e chame com os parâmetros desejados.
```

- Testar backup automático (modo direto):

```bash
python3 automatizando_backups.py
```

- Testar extração de dados (ex.: notícias):

```bash
python3 extrair_dados_web.py
```

- Testar envio de e-mail / monitoramento de preço (requer credenciais):

1) Configure variáveis de ambiente (recomendado):

```bash
export EMAIL_USER='seu_email@gmail.com'
export EMAIL_PASS='SUA_SENHA_OU_APP_PASSWORD'
export EMAIL_DEST='destino@exemplo.com'
```

2) Execute script de monitoramento ou envio de e-mail diretamente (exemplos):

```bash
python3 envio_email.py         # usa variáveis de ambiente quando não passadas explicitamente
python3 monitorar_precos_online.py
```

Observação: os scripts de envio de e-mail aceitarão credenciais via parâmetros ou via variáveis de ambiente (variáveis preferenciais: EMAIL_USER, EMAIL_PASS, EMAIL_DEST).

Agendamento (Linux - cron)
- Editar crontab: `crontab -e`
- Exemplo: rodar um script todo dia às 2:30
```cron
30 2 * * * /usr/bin/python3 /caminho/para/automatizando_backups.py >> /var/log/backup.log 2>&1
```
