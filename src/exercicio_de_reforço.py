import requests 

def verificar_site(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WIN64) cHROME/120.0.0.0"
    }
    resposta = requests.get(url, headers=headers)


    return f"O site {url} respondeu com status {resposta.status_code}"

print(verificar_site("https://www.wikipedia.org"))


 
 