import csv
import json

# cria uma lista vazia para armazenar os dados
data = []

# abre o arquivo csv
with open('example.csv', 'r', encoding='utf-8') as file:
    # cria um DictReader para ler o arquivo csv
    csv_reader = csv.DictReader(file)
    # itera sobre as linhas do arquivo csv
    for row in csv_reader:
        data.append(row)

# converte a lista para json
json_data = json.dumps(data)

# salva o json em um arquivo
with open('data.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_data)

