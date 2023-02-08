import requests
from bs4 import BeautifulSoup


# Enviar uma solicitação HTTP para o website
url = 'https://doentesporfutebol.com.br/guiadejogos/'
response = requests.get(url)

# Analisar o HTML retornado
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrar todas as divs com a classe "content"
content_divs = soup.find_all('div', class_='elementor-widget-container')

# Abrir o arquivo para escrita

collected_data = ""
# Imprimir o texto de cada div
for div in content_divs:
    collected_data += div.text

#print(collected_data)

# --------------------------------------------------------------------------------
# Savar em text
with open("data.txt", "w",encoding='utf-8') as file:
    file.write(collected_data)

# --------------------------------------------------------------------------------
# Savar em CSV

import csv

# abrindo o arquivo
with open("example.csv", "w", newline="", encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    # escrevendo os dados no arquivo
    csv_writer.writerows(collected_data)