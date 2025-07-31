# import os
# import random

# # Configurações
# num_cenarios = 4  # Número de cenários
# num_escolhas = 5  # Número de escolhas por cenário
# base_dir = "/Users/jvmaues/Documents/Estudos/Mestrado/optimization/HGS-CVRP/Instances/CVRP" 
# saida_dir = "/Users/jvmaues/Documents/Estudos/Mestrado/optimization/HGS-CVRP/Instances_part"

# # Criação do diretório de saída
# os.makedirs(saida_dir, exist_ok=True)

# # Lista de arquivos .txt no diretório base
# arquivos = [arquivo for arquivo in os.listdir(base_dir) if arquivo.endswith(".vrp")]

# print(len(arquivos))

# if not arquivos:
#     print("Nenhum arquivo .vrp encontrado no diretório base.")
#     exit()

# def dividir_lista_aleatoriamente(lista, n):
#     # Embaralha a lista para garantir aleatoriedade
#     random.shuffle(lista)
    
#     # Divide a lista em n partes iguais ou quase iguais
#     tamanho_particao = len(lista) // n
#     resto = len(lista) % n  # Elementos restantes que serão distribuídos
    
#     particoes = []
#     inicio = 0
    
#     for i in range(n):
#         # Adiciona elementos extras para compensar o resto
#         fim = inicio + tamanho_particao + (1 if resto > 0 else 0)
#         particoes.append(lista[inicio:fim])
#         inicio = fim
#         if resto > 0:
#             resto -= 1

#     return particoes

# # Gerar partições e organizar os arquivos
# for cenario in range(2, num_cenarios + 2):
#     for escolha in range(1, num_escolhas + 1):
#         # Definir o número de partições para o cenário atual
#         num_particoes = cenario

#         # Criar subdiretórios para o cenário e escolha atual
#         subdiretorio = os.path.join(saida_dir, f"cenario_{cenario}_{escolha}")
#         os.makedirs(subdiretorio, exist_ok=True)

#         # Inicializar as partições
#         # particoes = {i: [] for i in range(num_particoes)}

#         # Distribuir os arquivos aleatoriamente pelas partições
#         particoes = dividir_lista_aleatoriamente(arquivos, cenario)

#         # Salvar os arquivos nas respectivas partições
#         for particao, lista_arquivos in enumerate(particoes):
#             particao_dir = os.path.join(subdiretorio, f"particao_{particao + 1}")
#             os.makedirs(particao_dir, exist_ok=True)

#             for arquivo in lista_arquivos:
#                 origem = os.path.join(base_dir, arquivo)
#                 destino = os.path.join(particao_dir, arquivo)
#                 print("destino: ", destino)
#                 print("origem: ", origem)
#                 os.link(origem, destino)  # Cria um link simbólico para o arquivo
                
# print(f"Arquivos organizados em {num_cenarios} cenários com {num_escolhas} escolhas diferentes cada.")


# import os
# import random

# # Configurações
# num_cenarios = 4  # Número de cenários
# num_escolhas = 5  # Número de escolhas por cenário
# base_dir = "/Users/jvmaues/Documents/Estudos/Mestrado/optimization/HGS-CVRP/Instances/CVRP" 
# saida_dir = "/Users/jvmaues/Documents/Estudos/Mestrado/optimization/HGS-CVRP/Instances_part"

# # Criação do diretório de saída
# os.makedirs(saida_dir, exist_ok=True)

# # Lista de arquivos .txt no diretório base
# arquivos = [arquivo for arquivo in os.listdir(base_dir) if arquivo.endswith(".vrp")]

# print(len(arquivos))

# if not arquivos:
#     print("Nenhum arquivo .vrp encontrado no diretório base.")
#     exit()

# def dividir_lista_aleatoriamente(lista, n):
#     # Embaralha a lista para garantir aleatoriedade
#     random.shuffle(lista)
    
#     # Divide a lista em n partes iguais ou quase iguais
#     tamanho_particao = len(lista) // n
#     resto = len(lista) % n  # Elementos restantes que serão distribuídos
    
#     particoes = []
#     inicio = 0
    
#     for i in range(n):
#         # Adiciona elementos extras para compensar o resto
#         fim = inicio + tamanho_particao + (1 if resto > 0 else 0)
#         particoes.append(lista[inicio:fim])
#         inicio = fim
#         if resto > 0:
#             resto -= 1

#     return particoes

# # Gerar partições e organizar os arquivos
# for cenario in range(2, num_cenarios + 2):
#     for escolha in range(1, num_escolhas + 1):
#         # Definir o número de partições para o cenário atual
#         num_particoes = cenario

#         # Criar subdiretórios para o cenário e escolha atual
#         subdiretorio = os.path.join(saida_dir, f"cenario_{cenario}_{escolha}")
#         os.makedirs(subdiretorio, exist_ok=True)

#         # Inicializar as partições
#         particoes = dividir_lista_aleatoriamente(arquivos, cenario)

#         # Salvar os arquivos nas respectivas partições
#         for particao, lista_arquivos in enumerate(particoes):
#             particao_dir = os.path.join(subdiretorio, f"particao_{particao + 1}")
#             os.makedirs(particao_dir, exist_ok=True)

#             # Caminho do arquivo .txt para salvar os nomes
#             txt_path = os.path.join(particao_dir, "instances.txt")

#             with open(txt_path, "w") as txt_file:
#                 for arquivo in lista_arquivos:
#                     origem = os.path.join(base_dir, arquivo)
#                     destino = os.path.join(particao_dir, arquivo)
#                     txt_file.write(f"{destino}\n")  # Salva o caminho no .txt
#                     os.link(origem, destino)  # Cria um link simbólico para o arquivo

# print(f"Arquivos organizados em {num_cenarios} cenários com {num_escolhas} escolhas diferentes cada.")


# import os
# import random

# # Configurações
# num_k = [3, 5, 7]  # Número de agentes (Empresas)
# tamanho_c = [10, 15, 20] # Número de instâncias alocado para cada empresa
# num_j = 3  # Número de vezes que o conjunto será sorteado
# #num_i = 3  #Divisao para paralelizar no terminal

# base_dir = "/Users/jvmaues/Documents/Estudos/Mestrado/optimization/HGS-CVRP/Instances/CVRP"
# saida_dir = "/Users/jvmaues/Documents/Estudos/Mestrado/optimization/HGS-CVRP/Instances_part"

# # Criação do diretório de saída
# os.makedirs(saida_dir, exist_ok=True)

# # Lista de arquivos .vrp no diretório base
# arquivos = [arquivo for arquivo in os.listdir(base_dir) if arquivo.endswith(".vrp")]

# print(len(arquivos))

# if not arquivos:
#     print("Nenhum arquivo .vrp encontrado no diretório base.")
#     exit()

# def dividir_lista_aleatoriamente(lista, n):
#     # Embaralha a lista para garantir aleatoriedade
#     random.shuffle(lista)
    
#     # Divide a lista em n partes iguais ou quase iguais
#     tamanho_particao = 10
#     #resto = len(lista) % n  # Elementos restantes que serão distribuídos
    
#     particoes = []
#     inicio = 0
    
#     for i in range(n):
#         # Adiciona elementos extras para compensar o resto
#         fim = inicio + tamanho_particao + (1 if resto > 0 else 0)
#         particoes.append(lista[inicio:fim])
#         inicio = fim
#         if resto > 0:
#             resto -= 1

#     return particoes

# # Gerar partições e organizar os arquivos
# for cenario in range(2, num_cenarios + 2):
#     for escolha in range(1, num_escolhas + 1):
#         # Definir o número de partições para o cenário atual
#         num_particoes = cenario

#         # Inicializar as partições
#         particoes = dividir_lista_aleatoriamente(arquivos, cenario)

#         # Salvar os arquivos nas respectivas partições
#         for particao, lista_arquivos in enumerate(particoes):
#             # Nome do arquivo .txt para salvar os nomes
#             txt_name = f"cenario_{cenario}_{escolha}_particao_{particao + 1}_instances.txt"
#             txt_path = os.path.join(saida_dir, txt_name)

#             with open(txt_path, "w") as txt_file:
#                 for arquivo in lista_arquivos:
#                     origem = os.path.join(base_dir, arquivo)
#                     txt_file.write(f"{origem}\n")  # Salva o caminho no .txt

# print(f"Arquivos organizados em {num_cenarios} cenários com {num_escolhas} escolhas diferentes cada.")


import os
import random

base_dir = "/Users/jvmaues/Documents/Estudos/Mestrado/optimization/HGS-CVRP/Instances/CVRP"
saida_dir = "/Users/jvmaues/Documents/Estudos/Mestrado/optimization/HGS-CVRP/J1"

# Criação do diretório de saída
os.makedirs(saida_dir, exist_ok=True)

# Lista de arquivos .vrp no diretório base
arquivos = [arquivo for arquivo in os.listdir(base_dir) if arquivo.endswith(".vrp")]

if not arquivos:
    print("Nenhum arquivo .vrp encontrado no diretório base.")
    exit()

num_k = [3, 5, 7]  # Número de agentes
tamanho_c = [10, 15, 18]  # Número de instâncias por agente

# Iterar sobre valores de num_k
for k_idx, k in enumerate(num_k, start=1):
    # Embaralhar lista de arquivos para cada índice de k
    random.shuffle(arquivos)

    for c in tamanho_c:
        # Criar diretório específico para KxCy
        dir_nome = f"K{k}C{c}"
        dir_path = os.path.join(saida_dir, dir_nome)
        os.makedirs(dir_path, exist_ok=True)

        # Cópia da lista de arquivos para garantir completude para este valor de C
        arquivos_restantes = arquivos.copy()

        # Checar se há arquivos suficientes para a configuração atual
        if len(arquivos_restantes) < k * c:
            print(f"Não há arquivos suficientes para K={k}, C={c}. Ignorando esta configuração.")
            break

        # Selecionar k grupos de c arquivos sem sobreposição para este valor de C
        for i in range(k):
            # Selecionar c arquivos únicos da lista restante
            subset = random.sample(arquivos_restantes, c)
            # Remover os arquivos selecionados da lista de arquivos restantes
            arquivos_restantes = [arq for arq in arquivos_restantes if arq not in subset]

            # Criar o arquivo .txt com o nome KxExCy
            txt_nome = f"K{k}E{i + 1}C{c}.txt"
            txt_path = os.path.join(dir_path, txt_nome)

            with open(txt_path, "w") as txt_file:
                for arquivo in subset:
                    caminho_completo = os.path.join(base_dir, arquivo)
                    txt_file.write(f"{caminho_completo}\n")

