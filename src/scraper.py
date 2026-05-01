import requests 
from bs4 import BeautifulSoup

def buscar_vagas(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WIN64) cHROME/120.0.0.0"
    }
    resposta = requests.get(url, headers=headers)
    soup = BeautifulSoup(resposta.text, "html.parser") #Tratando url (HTML)

    return soup

def extrair_vagas(soup):

    resposta = soup.find_all("li", class_=["vaga odd", "vaga even"])

    return resposta



def extrair_detalhes(vagas):

    for vaga in vagas:
        cargo = vaga.find("a", class_="link-detalhes-vaga")
        print(cargo.text.strip())




url = "https://www.vagas.com.br/vagas-de-analista-de-dados"
soup = buscar_vagas(url)
vagas = extrair_vagas(soup)
print(len(vagas))  # quantas vagas encontrou
extrair_detalhes(vagas)