import requests
from bs4 import BeautifulSoup


def buscar_pagina(url):


    resposta = requests.get(url) #Guardando url 
    soup = BeautifulSoup(resposta.text, "html.parser") #Tratando url (HTML)
    titulo = soup.find("title") #Extraindo o título após o tratamento, espeficamente da TAG <>title<> usada no HTML
    
    return titulo.text

print(buscar_pagina("https://www.google.com"))

