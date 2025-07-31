import subprocess
import pandas as pd

def run_hgs(df):
    parametros = ['nbIterTraces', 'nbGranular', 'mu', 'lambda', 'nbElite', 'nbClose',
                  'nbIterPenaltyManagement', 'targetFeasible', 'penaltyIncrease', 'penaltyDecrease']
    custos = []
    
    for _, row in df.iterrows():
        # Extrai os valores dos parâmetros
        valores = {param: row[param] for param in parametros}
        path_inst = row['instancia']

        nbIterTraces = valores['nbIterTraces']
        nbGranular = valores['nbGranular']
        mu = valores['mu']
        lambda_ = valores['lambda']  # 'lambda' é reservado, por isso usamos 'lambda_'
        nbElite = valores['nbElite']
        nbClose = valores['nbClose']
        nbIterPenaltyManagement = valores['nbIterPenaltyManagement']
        targetFeasible = valores['targetFeasible']
        penaltyIncrease = valores['penaltyIncrease']
        penaltyDecrease = valores['penaltyDecrease']
        

        ## GIRO PELO AMOR DE DEUS TROCA ESSE PATH PELO DO SEU COMPUTADOR /Users/jvmaues/Documents/Estudos/Mestrado/optimization/HGS-CVRP/build/hgs

        # Monta o comando
        comando = f'/Users/jvmaues/Documents/Estudos/Mestrado/optimization/HGS-CVRP/build/hgs {path_inst} mySolution_test.sol -log 0 -seed 1 -t 30 -nbIterTraces {nbIterTraces} -nbGranular {nbGranular} -mu {mu} -lambda {lambda_} -nbElite {nbElite} -nbClose {nbClose} -nbIterPenaltyManagement {nbIterPenaltyManagement} -targetFeasible {targetFeasible} -penaltyIncrease {penaltyIncrease} -penaltyDecrease {penaltyDecrease}'

        
        # Executa o comando
        processo = subprocess.run(comando, shell=True, capture_output=True, text=True)
        print(f"Instância: {path_inst}")
        print("stdout:", processo.stdout)
        print("stderr:", processo.stderr)
        
        # Processa a saída
        try:
            value_resp = int(processo.stdout.strip())
        except ValueError:
            value_resp = None  # Caso haja erro na conversão
        
        custos.append(value_resp)
    
    # Adiciona a nova coluna ao dataframe
    df['custo'] = custos
    return df

if __name__ == "__main__":
    df_agg_j3 = pd.read_csv("agg_table_j3.csv")
    df_renned_j2 = run_hgs(df_agg_j3)
    df_renned_j2.to_csv("runned_agg_j3.csv")