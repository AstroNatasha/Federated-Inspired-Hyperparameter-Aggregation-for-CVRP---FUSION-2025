import numpy as np
import pandas as pd

# Definir o caminho do arquivo
file_path = 'irace_K3E1C10J1_experiments.txt'

# Ler os dados do arquivo ignorando caracteres não numéricos
with open(file_path, 'r') as file:
    data = []
    for line in file:
        # Remover colchetes e dividir os números
        line = line.strip().replace('[', '').replace(']', '')
        if line:
            row = [float(x) if x.lower() != 'nan' else np.nan for x in line.split()]
            data.append(row)

# Criar DataFrame
df = pd.DataFrame(data)

# Salvar como CSV
csv_path = 'irace_experiments.csv'
df.to_csv(csv_path, index=False, header=False)

print(f'Dados exportados com sucesso para {csv_path}')

