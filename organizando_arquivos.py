# Este script verifica todos os arquivos na pasta de "downloads", identifica o tipo de cada um e move para a pasta correta.

import os
import shutil

def organizar_arquivos(diretorio):
    # Dicionario com categoria e extensões
    categorias = {
        'Imagens': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documentos': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx', '.ppt'],
        'Videos': ['.mp4', '.avi', '.mov', '.mkv', '.flv'],
        'Musicas': ['.mp3', '.wav', '.ogg', '.flac'],
        'Arquivos_Comprimidos': ['.zip', '.rar', '.tar', '.gz'],
        'Scripts': ['.py', '.js', '.sh', '.bat']
    }

    # Criar pastas se não existirem
    for categoria in categorias:
        os.makedirs(os.path.join(diretorio, categoria), exist_ok=True)

    # Percorrer todos os arquivos
    for arquivo in os.listdir(diretorio):
        # Ignorar pastas
        if os.path.isdir(os.path.join(diretorio, arquivo)):
            # Ignorar diretórios
            continue

        # Obter extensão do arquivo
        extensao = os.path.splitext(arquivo)[1].lower()

        # Mover para a pasta correspondente
        for categoria, extensoes in categorias.items():
            if extensao in extensoes:
                shutil.move(
                    os.path.join(diretorio, arquivo),
                    os.path.join(diretorio, categoria, arquivo)
                )
                break

if __name__ == '__main__':
    # Exemplo de uso
    organizar_arquivos('/caminho/para/seu/diretorio')
