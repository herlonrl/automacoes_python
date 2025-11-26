# Script para automatizar backups.

import shutil
import datetime
import os

def fazer_backup(pasta_origem, pasta_destino):
    # Criar nome da pasta com data atual
    data_atual = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_backup = f'backup_{data_atual}'
    caminho_backup = os.path.join(paste_destino, nome_backup)
    
    # Criar pasta de nome_backup
    os.makedirs(caminho_backup, exist_ok=True)
    
    # Copiar arquivos
    for item in os.listdir(pasta_origem):
        caminho_completo = os.path.join(pasta_origem, item)
        if os.path.isfile(caminho_completo):
            shutil.copy2(caminho_completo, caminho_backup)
        elif os.path.isdir(caminho_completo):
            shutil.copytree(caminho_completo, os.path.join(caminho_backup, item))
        # Mensagem final após cópia de todos os itens
        print(f'Backup concluído: {caminho_backup}')


    if __name__ == '__main__':
        # Exemplo de execução direta (ajuste os caminhos antes de usar)
        fazer_backup('/caminho/para/pasta_origem', '/caminho/para/pasta_destino')


# Exemplo de uso
fazer_backup('/caminho/para/pasta_origem', '/caminho/para/pasta_destino')
