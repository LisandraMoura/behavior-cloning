import pandas as pd
import os

# Caminho do arquivo CSV original
caminho_csv_original = 'DataAndLoader/driving_log2.csv'

# Carregue o driving_log original
df = pd.read_csv(caminho_csv_original, header=None)
df.columns = ['center', 'left', 'right', 'steer', 'acceleration', 'breaking', 'speed']

# Caminho base para as novas imagens
nova_pasta_base = 'C:\\Users\\moura\\Searches\\behavior-cloning\\DataAndLoader\\IMG'

# Função para atualizar os caminhos das imagens
def atualizar_caminho_imagem(caminho_antigo):
    return os.path.join(nova_pasta_base, os.path.basename(caminho_antigo.strip()))

# Atualize o caminho das imagens para cada coluna de câmera
df['center'] = df['center'].apply(atualizar_caminho_imagem)
df['left'] = df['left'].apply(atualizar_caminho_imagem)
df['right'] = df['right'].apply(atualizar_caminho_imagem)

# Salve o novo CSV com as colunas atualizadas
df.to_csv('todososdados.csv', index=False)

# Verifique as primeiras linhas do novo CSV para confirmar as mudanças
print(df.head())
