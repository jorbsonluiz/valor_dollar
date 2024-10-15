import json
import requests
from bs4 import BeautifulSoup

# URL do Google
url = "https://www.google.com/search?q=dollar&oq=dollar"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    texto = soup.text
    valor = texto.split("=")[1].split()[0]
    print(f"O dollar está {valor} Reais")

else:
    print(f"Ocorreu um erro ao fazer a requisição. Status code: {response.status_code}")
