#!/bin/bash

# Script para fazer upload do projeto CVRP-CEC para GitHub
# Uso: ./upload_to_github.sh

echo "🚀 Preparando upload para GitHub..."
echo ""

# Verificar se git está instalado
if ! command -v git &> /dev/null; then
    echo "❌ Git não está instalado. Instale com:"
    echo "   sudo apt-get install git"
    exit 1
fi

# Verificar se estamos no diretório correto
if [ ! -f "README.md" ] || [ ! -d "Program" ]; then
    echo "❌ Execute este script no diretório raiz do projeto CVRP-CEC"
    exit 1
fi

# Inicializar git (se não estiver inicializado)
if [ ! -d ".git" ]; then
    echo "📁 Inicializando repositório Git..."
    git init
fi

# Adicionar todos os arquivos
echo "📦 Adicionando arquivos ao Git..."
git add .

# Fazer commit inicial
echo "💾 Fazendo commit inicial..."
git commit -m "Initial commit: Federated-Inspired Hyperparameter Aggregation for CVRP (FUSION-2025)

- Added comprehensive README.md in Portuguese
- Added quick instructions (INSTRUCOES_RAPIDAS.md)
- Added CSV generation documentation (GERACAO_CSV.md)
- Added automation scripts (compile_and_run.sh, convert_instances.py)
- Converted instances to CVRPLIB format
- Added complete project structure and documentation
- Research project for FUSION-2025 conference"

echo ""
echo "✅ Projeto preparado para upload!"
echo ""
echo "📋 Próximos passos:"
echo "1. Repositório criado: Federated-Inspired-Hyperparameter-Aggregation-for-CVRP---FUSION-2025"
echo "2. Execute os comandos que aparecerão abaixo"
echo "3. Siga as instruções do GitHub"
echo ""

# Mostrar comandos para conectar ao GitHub
echo "🔗 Comandos para conectar ao GitHub:"
echo ""
echo "git remote add origin https://github.com/AstroNatasha/Federated-Inspired-Hyperparameter-Aggregation-for-CVRP---FUSION-2025.git"
echo "git branch -M main"
echo "git push -u origin main"
echo ""
echo "🎯 Execute os comandos acima para fazer o upload!" 