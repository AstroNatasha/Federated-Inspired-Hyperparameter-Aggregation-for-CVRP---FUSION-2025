# 📊 Geração de CSV no Projeto CVRP-CEC

Este documento explica detalhadamente como os arquivos CSV são gerados e processados neste projeto de pesquisa em Federated Learning para CVRP.

## 🎯 Visão Geral

O projeto utiliza uma **pipeline completa** de geração de dados:
1. **Programa C++** gera dados brutos durante execução
2. **Scripts R** processam configurações e otimização
3. **Scripts Python** fazem análise final e extração

---

## 📁 Tipos de CSV Identificados

### 1. **CSV de Progresso da Busca** (`*.PG.csv`)

**Gerado por:** Programa C++ (função `exportSearchProgress`)

**Formato:**
```csv
instancia;seed;custo;tempo
/path/to/instance.txt;0;415;0.000107
```

**Exemplo real:**
```csv
/home/natasha/Downloads/cvrp-cec-main/instancias/instance_1_cvrplib.txt;0;415;0.000107
/home/natasha/Downloads/cvrp-cec-main/instancias_cvrplib/instance_2_cvrplib.txt;0;560;0.000125
```

**Código responsável:**
```cpp
// Em Program/Population.cpp
void Population::exportSearchProgress(std::string fileName, std::string instanceName)
{
    std::ofstream myfile(fileName);
    for (std::pair<clock_t, double> state : searchProgress)
        myfile << instanceName << ";" << params.ap.seed << ";" << state.second << ";" 
               << (double)state.first / (double)CLOCKS_PER_SEC << std::endl;
}
```

### 2. **CSV de Resultados de Experimentos** (`teste_result.csv`)

**Gerado por:** Scripts R (framework irace)

**Formato:**
```csv
"",".ID.","nbIterTraces","nbGranular","mu","lambda","nbElite","nbClose","nbIterPenaltyManagement","targetFeasible","penaltyIncrease","penaltyDecrease",".PARENT.","X1","X2","X3","X4","X5","X6","X7","X8","X9","X10","X11","X12","X13"
"1",6,"700","20","30","20","5","2","100","0.4","1.2","0.65",3,147397,27546,42157,66459,21245,1811,55539,27042,224094,74475,147490,27546,27047
```

**Conteúdo:**
- **Parâmetros do algoritmo:** nbIterTraces, nbGranular, mu, lambda, etc.
- **Resultados de instâncias:** X1, X2, X3... (custos das soluções)
- **Configurações:** ID, PARENT (para rastreamento)

### 3. **CSV de Análise de Dados** (`dados_media_j1.csv`, `custo_solucao_local.csv`)

**Gerado por:** Scripts Python de análise

**Formato:**
```csv
conjunto,media
K7E4C18J1,"{'X-n289-k60.vrp': '97691\n', 'X-n979-k58.vrp': '123920\n', 'CMT2.vrp': '846\n'...}"
K5E2C10J1,"{'Golden_20.vrp': '1897\n', 'X-n331-k15.vrp': '32397\n', 'X-n167-k10.vrp': '21335\n'...}"
```

**Conteúdo:**
- **Estatísticas por conjunto:** Médias de custos por configuração
- **Resultados por instância:** Custos individuais para cada instância de teste

---

## 🛠️ Fluxo Detalhado de Geração

### **Fase 1: Execução do Programa C++**

```bash
# Comando de execução
./compile_and_run.sh instancias_cvrplib/instance_1_cvrplib.txt solucao_1.txt -t 30
```

**Arquivos gerados:**
1. `solucao_1.txt` - Rotas encontradas
2. `solucao_1.txt.PG.csv` - Progresso da busca

**Código responsável em `Program/main.cpp`:**
```cpp
// Exportando a melhor solução
if (solver.population.getBestFound() != NULL)
{
    solver.population.exportCVRPLibFormat(*solver.population.getBestFound(), commandline.pathSolution);
    solver.population.exportSearchProgress(commandline.pathSolution + ".PG.csv", commandline.pathInstance);
}
```

### **Fase 2: Processamento com irace (R)**

**Script responsável:** `Scripts/getBestElites&Experiments.R`

```r
# Carrega biblioteca irace
library(irace)

# Processa cada arquivo .Rdata
process_file <- function(file_path) {
  iraceResults <- read_logfile(file_path)
  
  # Obtém melhor configuração
  best_config <- getFinalElites(iraceResults, n=1)
  best_id <- as.character(best_config$.ID.)
  all_exp <- iraceResults$experiments[, best_id]
  
  # Salva resultado em CSV
  write.csv(result, file = paste0(dir_path, "/", file_name,"_bestConfig.csv"))
}
```

**Arquivos processados:**
- `log_j1/irace_K3E1C10J1.Rdata`
- `log_j1/irace_K3E1C15J1.Rdata`
- ... (todos os arquivos .Rdata)

### **Fase 3: Análise com Python**

**Script responsável:** `Scripts/extract_tables.py`

```python
import rpy2.robjects as robjects
from rpy2.robjects import r

# Processa arquivos .Rdata
for rdata_file in rdata_files:
    r(f'iraceResults <- read_logfile("{rdata_path}")')
    
    # Extrai experiments
    experiments = r('iraceResults$experiments')
    
    # Salva em formato texto
    save_to_txt(output_experiments, experiments)
```

---

## 📊 Estrutura dos Diretórios de CSV

### **Diretórios de Logs:**
```
log_j1/          # Logs do experimento J1
├── irace_K3E1C10J1.Rdata
├── irace_K3E1C15J1.Rdata
├── teste_result.csv
└── logs_brutos/

log_j2/          # Logs do experimento J2
├── irace_*.Rdata
└── *.csv

log_j3/          # Logs do experimento J3
├── irace_*.Rdata
└── *.csv
```

### **Arquivos CSV Principais:**
```
├── solucao_*.txt.PG.csv          # Progresso da busca (gerado automaticamente)
├── custo_solucao_local.csv       # Custos das soluções locais
├── dados_media_j1.csv            # Médias do experimento J1
├── dados_media_j2.csv            # Médias do experimento J2
├── dados_media_j3.csv            # Médias do experimento J3
├── agg_table_majority_j3_1.csv   # Tabela agregada J3
└── majority_agg_j3_part3.csv     # Maioria agregada J3
```

---

## 🔧 Scripts de Processamento

### **1. Script R Principal** (`Scripts/getBestElites&Experiments.R`)

**Função:** Extrai melhores configurações dos logs irace

```r
# Importa biblioteca
library(irace)

# Processa arquivos .Rdata
files <- list.files(path = dir_path, pattern = "\\.Rdata$", full.names = TRUE)

# Função de processamento
process_file <- function(file_path) {
  iraceResults <- read_logfile(file_path)
  best_config <- getFinalElites(iraceResults, n=1)
  # ... processamento ...
  write.csv(result, file = paste0(dir_path, "/", file_name,"_bestConfig.csv"))
}
```

### **2. Script Python de Extração** (`Scripts/extract_tables.py`)

**Função:** Extrai dados de arquivos .Rdata para formato texto

```python
import rpy2.robjects as robjects
from rpy2.robjects import r

# Ativa conversão R-Python
pandas2ri.activate()

# Processa cada arquivo .Rdata
for rdata_file in rdata_files:
    r(f'iraceResults <- read_logfile("{rdata_path}")')
    
    # Extrai experiments
    experiments = r('iraceResults$experiments')
    
    # Salva em TXT
    save_to_txt(output_experiments, experiments)
```

### **3. Notebook de Geração** (`gerador_instancias.ipynb`)

**Função:** Gera instâncias de teste e dados de análise

```python
def generate_vrp_instance(num_clients, max_x, max_y, max_demand, vehicle_capacity):
    """Gera uma instância do VRP"""
    # ... geração de coordenadas e demandas ...
    return instance

def save_instance(instance, filename):
    """Salva a instância em arquivo de texto"""
    # ... salvamento em formato texto ...
```

---

## 📈 Pipeline Completa de Dados

### **Fluxo de Execução:**

```
1. Programa C++ Executa
   ↓
   Gera: solucao.txt + solucao.txt.PG.csv

2. irace Processa Logs
   ↓
   Gera: *.Rdata + teste_result.csv

3. Scripts R Extraem
   ↓
   Gera: *_bestConfig.csv

4. Scripts Python Analisam
   ↓
   Gera: dados_media_*.csv + custo_solucao_local.csv
```

### **Exemplo de Execução Completa:**

```bash
# 1. Executar programa
./compile_and_run.sh instancias_cvrplib/instance_1_cvrplib.txt solucao_1.txt -t 30

# 2. Verificar CSV gerado
cat solucao_1.txt.PG.csv
# Saída: /path/instance.txt;0;415;0.000107

# 3. Processar com R (se necessário)
Rscript Scripts/getBestElites\&Experiments.R

# 4. Analisar com Python
python3 Scripts/extract_tables.py
```

---

## 🎯 Formato dos Dados

### **CSV de Progresso** (Automático):
```csv
instancia;seed;custo;tempo
/path/instance.txt;0;415;0.000107
```

**Campos:**
- `instancia`: Caminho completo da instância
- `seed`: Seed usado para reprodutibilidade
- `custo`: Custo da melhor solução encontrada
- `tempo`: Tempo de execução em segundos

### **CSV de Configurações** (irace):
```csv
.ID.,nbIterTraces,nbGranular,mu,lambda,nbElite,nbClose,X1,X2,X3...
6,700,20,30,20,5,2,147397,27546,42157...
```

**Campos:**
- `.ID.`: Identificador da configuração
- `nbIterTraces`: Número de iterações entre traces
- `nbGranular`: Parâmetro de busca granular
- `mu`: Tamanho mínimo da população
- `lambda`: Tamanho da geração
- `nbElite`: Número de indivíduos elite
- `nbClose`: Número de soluções próximas
- `X1, X2, X3...`: Custos das soluções para cada instância

### **CSV de Análise** (Python):
```csv
conjunto,media
K7E4C18J1,"{'X-n289-k60.vrp': '97691\n', 'X-n979-k58.vrp': '123920\n'...}"
```

**Campos:**
- `conjunto`: Identificador do conjunto de configurações
- `media`: Dicionário com custos por instância

---

## 💡 Dicas de Uso

### **Para Gerar CSV de Progresso:**
```bash
# Executar programa (gera automaticamente)
./compile_and_run.sh instancia.txt solucao.txt -t 30

# Verificar CSV gerado
cat solucao.txt.PG.csv
```

### **Para Processar Logs irace:**
```bash
# Executar script R
Rscript Scripts/getBestElites\&Experiments.R

# Verificar resultados
ls -la log_j1/*.csv
```

### **Para Analisar Dados:**
```bash
# Executar script Python
python3 Scripts/extract_tables.py

# Verificar arquivos gerados
ls -la dados_media_*.csv
```

---

## 🔍 Troubleshooting

### **Problema: CSV não gerado**
```bash
# Verificar se programa executou corretamente
ls -la solucao_*.txt.PG.csv

# Verificar permissões
chmod +x compile_and_run.sh
```

### **Problema: Erro no R**
```r
# Instalar biblioteca irace se necessário
install.packages("irace")
library(irace)
```

### **Problema: Erro no Python**
```bash
# Instalar dependências
pip install rpy2 pandas numpy
```

---

## 📋 Resumo

O projeto CVRP-CEC utiliza uma **pipeline sofisticada** de geração de CSV:

1. **Programa C++** gera dados brutos de progresso
2. **Framework irace (R)** otimiza parâmetros e gera configurações
3. **Scripts Python** fazem análise final e extração

**Resultado:** Sistema completo de coleta, processamento e análise de dados para pesquisa em Federated Learning! 🎯

---

*Documento criado para facilitar o entendimento da geração de CSV no projeto CVRP-CEC* 