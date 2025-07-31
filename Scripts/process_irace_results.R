#Importa lib
library(irace)

# Diretório contendo os arquivos .Rdata
dir_path <- "/home/administrador/giron/labotim/cvrp-cec/logs_brutos"  # Altere para o diretório correto

# Listar todos os arquivos .Rdata no diretório
files <- list.files(path = dir_path, pattern = "\\.Rdata$", full.names = TRUE)

# Função para processar cada arquivo
process_file <- function(file_path) {
  # Carregar o arquivo .Rdata
  iraceResults <- read_logfile(file_path)
  
  # Verificar se iraceResults existe no ambiente carregado
  if (!exists("iraceResults")) {
    message(paste("O arquivo", file_path, "não contém 'iraceResults'. Pulando..."))
    return(NULL)
  }
  
  # Obter o nome base do arquivo (sem extensão)
  file_name <- tools::file_path_sans_ext(basename(file_path))
  
  # Criar os arquivos CSV
  write.table(iraceResults$experiments, file = paste0(dir_path, "/", file_name, "_experiments.csv"), row.names = FALSE, col.names = TRUE)
  write.csv(iraceResults$allConfigurations, file = paste0(dir_path, "/", file_name, "_allConfigurations.csv"), row.names = FALSE)
  write.csv(iraceResults$scenario$instances, file = paste0(dir_path, "/", file_name,"_instances.csv"), row.names = FALSE)
  
  message(paste("Processado:", file_path))
}

# Percorrer todos os arquivos e processar
lapply(files, process_file)

message("Processamento concluído!")

