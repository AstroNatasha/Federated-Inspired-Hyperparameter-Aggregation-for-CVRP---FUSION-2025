#!/usr/bin/env python3
"""
Script para converter instâncias do formato simplificado para o formato CVRPLIB
"""

import os
import math

def convert_instance(input_file, output_file):
    """Converte uma instância do formato simplificado para CVRPLIB"""
    
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    # Ler dados da instância
    nb_clients = int(lines[0].strip())
    
    # Ler coordenadas e demandas
    coords = []
    demands = []
    
    for i in range(1, nb_clients + 1):
        parts = lines[i].strip().split()
        if len(parts) >= 4:
            node_id = int(parts[0])
            x = float(parts[1])
            y = float(parts[2])
            demand = float(parts[3])
            
            coords.append((node_id, x, y))
            demands.append((node_id, demand))
    
    # Calcular capacidade do veículo (soma das demandas / número de veículos estimado)
    total_demand = sum(demand for _, demand in demands)
    vehicle_capacity = math.ceil(total_demand / 2)  # Estimativa simples
    
    # Escrever no formato CVRPLIB
    with open(output_file, 'w') as f:
        f.write(f"NAME : {os.path.basename(input_file).replace('.txt', '')}\n")
        f.write(f"COMMENT : Converted from simplified format\n")
        f.write(f"TYPE : CVRP\n")
        f.write(f"DIMENSION : {nb_clients}\n")
        f.write(f"EDGE_WEIGHT_TYPE : EUC_2D\n")
        f.write(f"CAPACITY : {vehicle_capacity}\n")
        f.write(f"NODE_COORD_SECTION\n")
        
        # Escrever coordenadas (depósito primeiro)
        depot_coords = coords[0]  # Assumir que o primeiro é o depósito
        f.write(f"1 {depot_coords[1]:.0f} {depot_coords[2]:.0f}\n")
        
        for i in range(1, nb_clients):
            node_id, x, y = coords[i]
            f.write(f"{i+1} {x:.0f} {y:.0f}\n")
        
        f.write(f"DEMAND_SECTION\n")
        
        # Escrever demandas (depósito primeiro)
        depot_demand = demands[0][1]
        f.write(f"1 {depot_demand:.0f}\n")
        
        for i in range(1, nb_clients):
            node_id, demand = demands[i]
            f.write(f"{i+1} {demand:.0f}\n")
        
        f.write(f"DEPOT_SECTION\n")
        f.write(f"1\n")
        f.write(f"EOF\n")
    
    print(f"✅ Instância convertida: {input_file} -> {output_file}")

def main():
    """Função principal"""
    print("🔄 Convertendo instâncias para formato CVRPLIB...")
    
    # Criar diretório para instâncias convertidas
    output_dir = "instancias_cvrplib"
    os.makedirs(output_dir, exist_ok=True)
    
    # Converter todas as instâncias
    for i in range(1, 11):  # instance_1.txt até instance_10.txt
        input_file = f"instancias/instance_{i}.txt"
        output_file = f"{output_dir}/instance_{i}_cvrplib.txt"
        
        if os.path.exists(input_file):
            convert_instance(input_file, output_file)
        else:
            print(f"⚠️  Arquivo não encontrado: {input_file}")
    
    print(f"\n📁 Instâncias convertidas salvas em: {output_dir}/")
    print("💡 Use as instâncias com sufixo '_cvrplib' para executar o programa")

if __name__ == "__main__":
    main() 