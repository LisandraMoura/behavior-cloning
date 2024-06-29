import pandas as pd
import os

# Carregue o driving_log original
df = pd.read_csv('DataAndLoader/driving_log2.csv', header=None)
df.columns = ['image_path', 'angle']

# Caminho base para as novas imagens
nova_pasta_base = 'C:\\Users\\moura\\Searches\\behavior-cloning\\DataAndLoader\\IMG'

# Substitua o caminho das imagens
df['image_path'] = df['image_path'].apply(lambda x: os.path.join(nova_pasta_base, os.path.basename(x.strip())))

# Salve o novo CSV
df.to_csv('todososdados.csv', index=False)

# Verifique as primeiras linhas do novo CSV
df.head()
