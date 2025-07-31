#!/bin/bash

# Script para compilar e executar o programa CVRP
# Uso: ./compile_and_run.sh [instancia] [solucao] [opcoes]

echo "=== CVRP-CEC Compilador e Executor ==="
echo ""

# Verificar se estamos no diretório correto
if [ ! -d "Program" ]; then
    echo "❌ Erro: Execute este script no diretório raiz do projeto"
    echo "   Diretório atual: $(pwd)"
    echo "   Diretório Program não encontrado"
    exit 1
fi

# Salvar o diretório raiz
ROOT_DIR=$(pwd)

# Navegar para o diretório Program
cd Program

echo "🔨 Compilando o programa..."

# Tentar compilar com diferentes flags
if g++ -O3 -std=c++11 -o hgs *.cpp 2>/dev/null; then
    echo "✅ Compilação bem-sucedida!"
elif g++ -O3 -std=c++11 -Wall -o hgs *.cpp 2>/dev/null; then
    echo "✅ Compilação bem-sucedida (com warnings)"
else
    echo "❌ Erro na compilação. Verifique se o GCC está instalado."
    echo "   Comando para instalar GCC no Ubuntu/Debian:"
    echo "   sudo apt-get install build-essential"
    exit 1
fi

# Verificar se o executável foi criado
if [ ! -f "hgs" ]; then
    echo "❌ Erro: Executável 'hgs' não foi criado"
    exit 1
fi

echo "🎯 Executável criado: ./hgs"
echo ""

# Se foram passados argumentos, executar o programa
if [ $# -ge 2 ]; then
    echo "🚀 Executando o programa..."
    
    # Converter caminhos para caminhos absolutos se necessário
    INSTANCE_PATH="$1"
    SOLUTION_PATH="$2"
    
    # Se o caminho da instância não é absoluto, converter para relativo ao diretório raiz
    if [[ ! "$INSTANCE_PATH" = /* ]]; then
        INSTANCE_PATH="$ROOT_DIR/$INSTANCE_PATH"
    fi
    
    # Se o caminho da solução não é absoluto, colocar no diretório raiz
    if [[ ! "$SOLUTION_PATH" = /* ]]; then
        SOLUTION_PATH="$ROOT_DIR/$SOLUTION_PATH"
    fi
    
    echo "   Instância: $INSTANCE_PATH"
    echo "   Solução: $SOLUTION_PATH"
    echo "   Opções: ${@:3}"
    echo ""
    
    # Executar o programa
    ./hgs "$INSTANCE_PATH" "$SOLUTION_PATH" "${@:3}"
    
    if [ $? -eq 0 ]; then
        echo ""
        echo "✅ Execução concluída com sucesso!"
        echo "📁 Arquivos gerados:"
        ls -la "$SOLUTION_PATH"* 2>/dev/null || echo "   Nenhum arquivo de saída encontrado"
    else
        echo ""
        echo "❌ Erro durante a execução"
    fi
else
    echo "💡 Para executar o programa, use:"
    echo "   ./compile_and_run.sh <instancia> <solucao> [opcoes]"
    echo ""
    echo "📝 Exemplos:"
    echo "   ./compile_and_run.sh instancias/instance_1.txt solucao_1.txt"
    echo "   ./compile_and_run.sh instancias/instance_1.txt solucao_1.txt -t 30"
    echo "   ./compile_and_run.sh instancias/instance_1.txt solucao_1.txt -it 10000 -seed 12345"
    echo ""
    echo "📋 Parâmetros disponíveis:"
    echo "   -t <tempo>     : Limite de tempo em segundos"
    echo "   -it <iter>     : Número máximo de iterações"
    echo "   -seed <seed>   : Seed para reprodutibilidade"
    echo "   -veh <veh>     : Número máximo de veículos"
    echo "   -log <0/1>     : Modo verbose"
fi

echo ""
echo "=== Fim do script ===" 