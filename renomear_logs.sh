#!/bin/bash

# Renomeia todos os arquivos .log para .Rdata
for file in *.log; do
    mv "$file" "${file%.log}J3.Rdata"
done

echo "Renomeação concluída."

