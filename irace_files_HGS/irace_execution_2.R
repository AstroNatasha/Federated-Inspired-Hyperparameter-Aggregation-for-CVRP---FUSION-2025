# # Start R and load irace
# library(irace)

# # Define the scenario with the suggested changes
# scenario <- list(
#   targetRunner = "target-runner.sh",    # The script that runs your C++ program
#   targetEvaluator = NULL,               # No custom evaluator script
#   maxExperiments = 100,                 # Total budget for experiments
#   instances = readLines("instances.txt"),  # Read instances from the file
#   logFile = "irace.log",                # Log file to record irace activity
#   seed = 1234,                          # Seed for reproducibility
#   parameterFile = "parameters.txt",     # File defining parameters to tune
#   #digits = 3,                           # Precision for numerical parameters
#   firstTest = 5,                        # Number of evaluations in the first iteration
#   minNbSurvival = 1,                     # Allow irace to proceed with fewer configurations
#   nbIterations = 5,                   # Optional: Set the number of iterations
#   parallel = 4                         # Number of parallel runs
# )

# # Confirm 'scenario' is defined
# print(scenario)

# # Run irace
# irace(scenario = scenario)

# # # Load the irace results
# # load("irace.Rdata")

# # # Get the best configurations
# # best_configs <- iraceResults$allConfigurations[iraceResults$allConfigurations$eliminated == 0, ]

# # # Print the best configurations
# # print(best_configs)

library(irace)

# Obter o argumento de linha de comando
args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 2) {
  stop("Por favor, forneça o caminho do arquivo de instâncias e o caminho para o log como argumentos.")
}
instances_file <- args[1]
log_file <- args[2]

# Verificar se o arquivo de instâncias existe
if (!file.exists(instances_file)) {
  stop(paste("O arquivo fornecido não foi encontrado:", instances_file))
}

# Definir o cenário
scenario <- list(
  targetRunner = "target-runner.sh",    # O script que executa seu programa em C++
  targetEvaluator = NULL,               # Sem script avaliador personalizado
  maxExperiments = 100,                 # Orçamento total para experimentos
  instances = readLines(instances_file),  # Lê instâncias do arquivo fornecido
  logFile = log_file,                   # Arquivo de log dinâmico
  seed = 1234,                          # Semente para reprodutibilidade
  parameterFile = "parameters.txt",     # Arquivo definindo parâmetros para ajuste
  firstTest = 5,                        # Número de avaliações na primeira iteração
  minNbSurvival = 1,                    # Prosseguir com menos configurações
  nbIterations = 5,                     # Número de iterações
  parallel = 4                          # Número de execuções paralelas
)

# Executar irace
irace(scenario = scenario)
