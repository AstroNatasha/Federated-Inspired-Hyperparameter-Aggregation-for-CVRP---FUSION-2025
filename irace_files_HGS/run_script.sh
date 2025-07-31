#!/bin/bash

# Diretório que contém os arquivos .txt
DIR_PATH=$1

# Verificar se o diretório foi fornecido e existe
if [ -z "$DIR_PATH" ]; then
  echo "Por favor, forneça o caminho para o diretório contendo os arquivos .txt."
  exit 1
fi

if [ ! -d "$DIR_PATH" ]; then
  echo "O diretório fornecido não existe: $DIR_PATH"
  exit 1
fi

# Listar todos os arquivos .txt no diretório
FILES=$(find "$DIR_PATH" -type f -name "*.txt")

# Caminho para o script em R
R_SCRIPT="irace_script.R"

# Verificar se o script em R existe
if [ ! -f "$R_SCRIPT" ]; then
  echo "O script R não foi encontrado: $R_SCRIPT"
  exit 1
fi

# Arquivo para salvar a saída de todas as execuções
OUTPUT_FILE="irace_execution_output.txt"
echo "Iniciando execução em $(date)" > "$OUTPUT_FILE"

# Loop pelos arquivos e executa o script R para cada arquivo
for FILE in $FILES; do
  BASENAME=$(basename "$FILE" .txt)       # Nome base do arquivo (sem extensão)
  LOG_FILE="irace_${BASENAME}.log"        # Arquivo de log específico para o arquivo
  echo "Executando irace com o arquivo de instâncias: $FILE" | tee -a "$OUTPUT_FILE"

  # Executar o script R e redirecionar a saída para o arquivo
  Rscript "$R_SCRIPT" "$FILE" "$LOG_FILE" >> "$OUTPUT_FILE" 2>&1

  echo "Finalizado: $FILE. Log salvo em $LOG_FILE" | tee -a "$OUTPUT_FILE"
done

echo "Execuções concluídas em $(date)" >> "$OUTPUT_FILE"
