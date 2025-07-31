import os
import rpy2.robjects as robjects
from rpy2.robjects import r
from rpy2.robjects import pandas2ri

# Ativa a conversão automática entre R e Python
pandas2ri.activate()

# Diretórios de entrada e saída
input_dir = "/home/alobogiron/work/cvrp-cec/log_j3"  # Altere para o caminho correto
output_dir = "/home/alobogiron/work/cvrp-cec/logs_extraidos/"  # Altere para onde deseja salvar os TXT

# Garante que o diretório de saída existe
os.makedirs(output_dir, exist_ok=True)

# Lista todos os arquivos .Rdata no diretório
rdata_files = [f for f in os.listdir(input_dir) if f.endswith(".Rdata")]

# Inicializa o ambiente R e carrega o pacote irace
r('library(irace)')

# Função para salvar qualquer tipo de dado diretamente em TXT
def save_to_txt(file_path, data):
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(str(data))  # Armazena os dados brutos como texto puro
        print(f"Salvo: {file_path}")
    except Exception as e:
        print(f"Erro ao salvar {file_path}: {e}")

# Processa cada arquivo .Rdata
for rdata_file in rdata_files:
    rdata_path = os.path.join(input_dir, rdata_file)
    file_base_name = rdata_file.replace(".Rdata", "")  # Remove a extensão para evitar nomes longos
    print(f"Processando: {rdata_file}")

    try:
        # Carrega o arquivo .Rdata no ambiente R com read_logfile()
        r(f'iraceResults <- read_logfile("{rdata_path}")')

        # Obtém os nomes das variáveis carregadas
        variables = list(r('names(iraceResults)'))

        # Verifica se as variáveis existem antes de acessá-las
        experiments = r('iraceResults$experiments') if "experiments" in variables else None
        all_configurations = r('iraceResults$allConfigurations') if "allConfigurations" in variables else None
        scenario_names = list(r('names(iraceResults$scenario)')) if "scenario" in variables else []

        # Salva experiments.txt
        if experiments is not None:
            output_experiments = os.path.join(output_dir, f"{file_base_name}_experiments.txt")
            save_to_txt(output_experiments, experiments)

        # Salva allConfigurations.txt
        if all_configurations is not None:
            output_all_config = os.path.join(output_dir, f"{file_base_name}_allConfigurations.txt")
            save_to_txt(output_all_config, all_configurations)

        # Salva scenario_instances.txt acessando as instâncias corretamente
        if "instances" in scenario_names:
            num_instances = int(r('length(iraceResults$scenario$instances)')[0])  # 🔥 CORREÇÃO APLICADA!

            instances_list = [
                str(r(f'iraceResults$scenario$instances[[{i + 1}]]')[0])  # Acesso correto ao índice 1-based em R
                for i in range(num_instances)
            ]

            output_instances = os.path.join(output_dir, f"{file_base_name}_scenario_instances.txt")
            save_to_txt(output_instances, "\n".join(instances_list))

    except Exception as e:
        print(f"Erro ao processar {rdata_file}: {e}")

print("Processamento concluído!")
