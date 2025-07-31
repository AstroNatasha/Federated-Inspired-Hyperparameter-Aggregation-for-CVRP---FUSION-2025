# 🚀 Instruções Rápidas - CVRP-CEC

## Como Rodar o Programa

### 1. Primeira Vez (Configuração)
```bash
# Converter instâncias para formato correto
python3 convert_instances.py

# Testar com uma instância
./compile_and_run.sh instancias_cvrplib/instance_1_cvrplib.txt solucao_teste.txt -t 10
```

### 2. Execução Normal
```bash
# Executar uma instância
./compile_and_run.sh instancias_cvrplib/instance_1_cvrplib.txt solucao_1.txt -t 30

# Executar todas as instâncias
for file in instancias_cvrplib/instance_*_cvrplib.txt; do
    ./compile_and_run.sh "$file" "solucao_$(basename "$file" .txt).txt" -t 60
done
```

### 3. Verificar Resultados
```bash
# Ver arquivos gerados
ls -la solucao_*.txt

# Ver uma solução
cat solucao_1.txt
```

## 📋 Parâmetros Principais

| Parâmetro | Descrição | Exemplo |
|-----------|-----------|---------|
| `-t <tempo>` | Limite de tempo (segundos) | `-t 30` |
| `-it <iter>` | Máximo de iterações | `-it 10000` |
| `-seed <seed>` | Seed para reprodutibilidade | `-seed 12345` |
| `-veh <veh>` | Número máximo de veículos | `-veh 5` |

## 📁 Arquivos Importantes

- `compile_and_run.sh` - Script principal
- `convert_instances.py` - Converte instâncias
- `instancias_cvrplib/` - Instâncias prontas para usar
- `solucao_*.txt` - Resultados gerados

## ⚠️ Problemas Comuns

1. **Erro de compilação**: Verifique se o GCC está instalado
2. **Arquivo não encontrado**: Use caminhos absolutos ou relativos corretos
3. **Formato de instância**: Use as instâncias convertidas em `instancias_cvrplib/`

## 💡 Dicas

- Comece com `-t 10` para testes rápidos
- Use `-seed 12345` para resultados reprodutíveis
- Para instâncias grandes, aumente o tempo limite
- Verifique sempre se os arquivos de saída foram gerados 