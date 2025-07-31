# CVRP-CEC - Capacitated Vehicle Routing Problem

Este projeto implementa um algoritmo genético híbrido (HGS) para resolver o problema de roteamento de veículos com capacidade limitada (CVRP).

## 📋 Pré-requisitos

- **Compilador C++**: GCC ou Clang
- **Sistema Operacional**: Linux, macOS ou Windows (com WSL)
- **Memória**: Mínimo 4GB RAM recomendado
- **Python 3**: Para scripts de conversão e automação

## 🚀 Como Compilar e Executar

### Método 1: Script Automático (Recomendado)

```bash
# Compilar e executar em um comando
./compile_and_run.sh instancias_cvrplib/instance_1_cvrplib.txt solucao_1.txt -t 30
```

### Método 2: Compilação Manual

```bash
# 1. Navegar para o diretório do programa
cd Program

# 2. Compilar o programa
g++ -O3 -std=c++11 -o hgs *.cpp

# 3. Executar
./hgs <caminho_instancia> <caminho_solucao> [opções]
```

## 🎯 Exemplos de Uso

### Execução Básica
```bash
./compile_and_run.sh instancias_cvrplib/instance_1_cvrplib.txt solucao_1.txt
```

### Com Limite de Tempo
```bash
./compile_and_run.sh instancias_cvrplib/instance_1_cvrplib.txt solucao_1.txt -t 30
```

### Com Parâmetros Avançados
```bash
./compile_and_run.sh instancias_cvrplib/instance_1_cvrplib.txt solucao_1.txt -t 60 -seed 12345 -it 10000
```

### Executar Múltiplas Instâncias
```bash
# Executar todas as instâncias convertidas
for file in instancias_cvrplib/instance_*_cvrplib.txt; do
    ./compile_and_run.sh "$file" "solucao_$(basename "$file" .txt).txt" -t 30
done
```

## 📝 Parâmetros Disponíveis

| Parâmetro | Descrição | Padrão |
|-----------|-----------|---------|
| `-t <double>` | Limite de tempo em segundos | Sem limite |
| `-it <int>` | Número máximo de iterações sem melhoria | 20.000 |
| `-seed <int>` | Seed para reprodutibilidade | 0 |
| `-veh <int>` | Número máximo de veículos | Infinito |
| `-round <bool>` | Arredondar distâncias (0/1) | 1 |
| `-log <bool>` | Modo verbose (0/1) | 1 |

### Parâmetros Avançados

| Parâmetro | Descrição | Padrão |
|-----------|-----------|---------|
| `-nbGranular <int>` | Parâmetro de busca granular | 20 |
| `-mu <int>` | Tamanho mínimo da população | 25 |
| `-lambda <int>` | Tamanho da geração | 40 |
| `-nbElite <int>` | Número de indivíduos elite | 5 |
| `-nbClose <int>` | Número de soluções próximas | 4 |

## 📁 Estrutura de Arquivos

### Instâncias de Teste
- `instancias/` - Instâncias originais (formato simplificado)
- `instancias_cvrplib/` - Instâncias convertidas (formato CVRPLIB)
- `instancias/instance_1_cvrplib.txt` - Exemplo de instância no formato correto

### Scripts de Automação
- `compile_and_run.sh` - Script principal para compilar e executar
- `convert_instances.py` - Converte instâncias para formato CVRPLIB
- `j1_run.py` - Script de automação para múltiplas execuções

## 🔧 Scripts de Conversão

### Converter Instâncias para Formato CVRPLIB
```bash
# Converter todas as instâncias
python3 convert_instances.py
```

### Formato das Instâncias
As instâncias devem seguir o formato CVRPLIB:
```
NAME : instance_name
COMMENT : Description
TYPE : CVRP
DIMENSION : 8
EDGE_WEIGHT_TYPE : EUC_2D
CAPACITY : 28
NODE_COORD_SECTION
1 0 0
2 65 0
...
DEMAND_SECTION
1 0
2 9
...
DEPOT_SECTION
1
EOF
```

## 📊 Saídas do Programa

O programa gera dois arquivos de saída:
1. **Arquivo de solução**: Contém as rotas encontradas
2. **Arquivo de progresso**: `*.PG.csv` - Progresso da busca

### Exemplo de Saída
```
Route #1: 5 6 2 1 4
Route #2: 3 7
Cost 415
```

## 🐛 Solução de Problemas

### Erro de Compilação
```bash
# Se houver erro de compilação, tente:
g++ -O3 -std=c++11 -Wall -o hgs *.cpp
```

### Erro de Execução
- Verifique se o arquivo de instância existe
- Certifique-se de que o diretório de saída tem permissões de escrita
- Use `-log 1` para ver mensagens detalhadas

### Problemas de Memória
- Reduza o número de iterações com `-it`
- Use limite de tempo com `-t`
- Reduza parâmetros como `-mu` e `-lambda`

## 📈 Análise de Resultados

### Scripts de Análise
- `Scripts/extract_tables.py` - Extrai tabelas de resultados
- `Scripts/exploratory_analisys.ipynb` - Análise exploratória
- `Scripts/getBestElites&Experiments.R` - Análise estatística

## 🚀 Guia Rápido

1. **Primeira execução**:
   ```bash
   # Converter instâncias
   python3 convert_instances.py
   
   # Executar primeira instância
   ./compile_and_run.sh instancias_cvrplib/instance_1_cvrplib.txt solucao_1.txt -t 30
   ```

2. **Executar todas as instâncias**:
   ```bash
   for file in instancias_cvrplib/instance_*_cvrplib.txt; do
       ./compile_and_run.sh "$file" "solucao_$(basename "$file" .txt).txt" -t 60
   done
   ```

3. **Verificar resultados**:
   ```bash
   ls -la solucao_*.txt
   cat solucao_1.txt
   ```

## 🤝 Contribuição

Para contribuir com o projeto:
1. Faça um fork do repositório
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 📞 Suporte

Se você encontrar problemas:
1. Verifique se todos os pré-requisitos estão instalados
2. Teste com uma instância simples primeiro
3. Use o modo verbose (`-log 1`) para debug
4. Consulte os logs de erro gerados

---

**Desenvolvido para pesquisa em Federated Learning para CVRP**
