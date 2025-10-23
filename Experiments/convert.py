import csv
import pandas as pd

input_file = 'processamento.txt'
output_file = 'tabela_processamento.csv'

rows = []
with open(input_file, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('Fonte'):
            continue
        parts = line.split(',')
        if len(parts) == 5:
            # Troca ponto por vírgula nos números
            for i in range(1, 5):
                parts[i] = parts[i].replace('.', ',')
            rows.append(parts)

header = ['Fonte', 'Processamento', 'Consulta', 'Total', 'Linhas']
with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(header)
    writer.writerows(rows)

print(f'Tabela exportada para {output_file}')

