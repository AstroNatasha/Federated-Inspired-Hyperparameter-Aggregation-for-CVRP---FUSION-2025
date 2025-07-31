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

  # Armazenando os experimentos
  best_config <- getFinalElites(iraceResults, n=1)
  best_id <- as.character(best_config$.ID.)
  all_exp <- iraceResults$experiments[, best_id]
  # Transformar vetor em lista
  all_exp <- as.list(all_exp)

  #Armzenar melhor configuração
  elite_config <- getFinalElites(file_path, n=0)

  #Concatenar listas
  result <- append(elite_config, all_exp)
  
  # Obter o nome base do arquivo (sem extensão)
  file_name <- tools::file_path_sans_ext(basename(file_path))
  
  write.csv(result, file = paste0(dir_path, "/", file_name,"_bestConfig.csv"))
  
  message(paste("Processado:", file_path))
}

# Percorrer todos os arquivos e processar
lapply(files, process_file)

message("Processamento concluído!")

