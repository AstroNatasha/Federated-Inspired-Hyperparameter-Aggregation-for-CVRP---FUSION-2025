# Carregar o pacote irace
library(irace)

# Definir a lista de arquivos de instâncias
files_instances <- list.files(path = "/Users/jvmaues/Documents/Estudos/Mestrado/optimization/HGS-CVRP/Instances_part", full.names = TRUE)

# Verificar se há arquivos na lista
if (length(files_instances) == 0) {
  stop("Nenhum arquivo instances.txt foi encontrado no diretório especificado.")
}

# Definir o número de execuções
n_executions <- length(files_instances)

# Iterar sobre cada arquivo de instâncias e executar o irace
for (i in seq_along(files_instances)) {
  # Nome do arquivo atual
  instance_file <- files_instances[i]
  
  # Nome do log correspondente
  log_file <- paste0("irace_run_", i, ".log")
  
  # Criar o cenário para o irace
  scenario <- list(
    targetRunner = "target-runner.sh",  # O script que executa seu programa em C++
    targetEvaluator = NULL,             # Nenhum avaliador personalizado
    maxExperiments = 100,               # Orçamento total para experimentos
    instances = readLines(instance_file),  # Ler as instâncias do arquivo atual
    logFile = log_file,                 # Arquivo de log exclusivo para esta execução
    seed = 1234,                        # Semente para reprodutibilidade
    parameterFile = "parameters.txt",   # Arquivo definindo os parâmetros a serem ajustados
    firstTest = 5,                      # Número de avaliações na primeira iteração
    minNbSurvival = 1                   # Permitir que irace continue com menos configurações
    nbIterations = 5,                   # Optional: Set the number of iterations
    parallel = 4                         # Number of parallel runs
  )
  
  # Imprimir informações sobre a execução
  cat("\n=== Executando o irace para o arquivo:", instance_file, "===\n")
  
  # Executar o irace
  irace(scenario = scenario)
}

cat("\nTodas as execuções foram concluídas com sucesso.\n")

