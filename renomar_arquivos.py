# Script para renomear todos os arquivos de uma pasta para um formato padronizado com numeração sequencial.

import os

def renomear_arquivos(diretorio, prefixo, iniciar_em=1, extensoes_permitidas=None):
    """Renomeia todos os arquivos em um diretório para um formato padronizado.

    extensoes_permitidas: lista/tuple de strings como ['.jpg', '.png'] para filtrar somente certos tipos de arquivo.
    """
    # Listar arquivos
    arquivos = [f for f in os.listdir(diretorio) if os.path.isfile(os.path.join(diretorio, f))]
    
    # Aplicar filtro de extensões permitido, se fornecido
    if extensoes_permitidas:
        arquivos = [f for f in arquivos if os.path.splitext(f)[1].lower() in [e.lower() for e in extensoes_permitidas]]
    
    # Ordenar arquivos (opcional)
    arquivos.sort()
    
    # Renomear arquivos
    contador = iniciar_em
    for arquivo in arquivos:
        # Obter extensão
        extensao = os.path.splitext(arquivo)[1]
        
        # Criar novo nome
        novo_nome = f'{prefixo}_{contador:03d}{extensao}'
        
        # Renomear arquivo
        os.rename(
            os.path.join(diretorio, arquivo),
            os.path.join(diretorio, novo_nome)
        )
        
        contador += 1
        
    print(f'Renomeação concluída. {len(arquivos)} arquivos renomeados.')


if __name__ == '__main__':
    # Exemplo de uso
    renomear_arquivos('/caminho/para/seu/diretorio', 'foto', 1)
    
# Exemplo de uso
renomear_arquivos('/caminho/para/seu/diretorio', 'foto', 1)
