import os
import shutil
from math import ceil

# Diretório base
j1_dir = "J1"
j1_run_dir = "J1_RUN"
output_dirs = [os.path.join(j1_run_dir, f"Part{i+1}") for i in range(3)]

# Criar o diretório J1_RUN se não existir
os.makedirs(j1_run_dir, exist_ok=True)

# Listar todos os arquivos .txt em J1 e subdiretórios
txt_files = []
for root, _, files in os.walk(j1_dir):
    for file in files:
        if file.endswith(".txt"):
            txt_files.append(os.path.join(root, file))

# Copiar todos os arquivos para J1_RUN
for file in txt_files:
    shutil.copy(file, os.path.join(j1_run_dir, os.path.basename(file)))

# Listar todos os arquivos agora em J1_RUN
all_files = [file for file in os.listdir(j1_run_dir) if file.endswith(".txt")]

# Garantir que existam arquivos suficientes para dividir
if len(all_files) < 3:
    print("Não há arquivos suficientes para dividir em 3 partes.")
    exit()

# Dividir arquivos em 3 partes iguais
num_files = len(all_files)
files_per_part = ceil(num_files / 3)

# Criar os diretórios de saída
for output_dir in output_dirs:
    os.makedirs(output_dir, exist_ok=True)

# Distribuir os arquivos entre as 3 pastas
for i, file in enumerate(all_files):
    target_dir = output_dirs[i // files_per_part]  # Selecionar a pasta correspondente
    shutil.copy(os.path.join(j1_run_dir, file), os.path.join(target_dir, file))

print("Arquivos copiados e organizados em 3 pastas dentro de J1_RUN.")
