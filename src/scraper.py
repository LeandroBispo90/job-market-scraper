import requests 
import pandas as pd
from bs4 import BeautifulSoup
from exporter import exportar_csv 



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
    # 1. listas vazias 
    cargos = []
    empresas = []
    cidades = []
    niveis = []

    for vaga in vagas:
        # 2. extraindo dados
        cargo = vaga.find("a", class_="link-detalhes-vaga")
        texto_cargo = cargo.text.strip() if cargo else "Não informado"


        empresa = vaga.find("span", class_="emprVaga")
        texto_empresa = empresa.text.strip() if empresa else "Não informado"

        cidade = vaga.find("div", class_="vaga-local")
        if cidade:
        # pega só o texto direto, ignorando tags filhas
            texto_cidade = list(cidade.stripped_strings)[0] if len(list(cidade.stripped_strings)) > 0 else "Não informado"
        else:
            texto_cidade = "Não informado"

        nivel_vaga = vaga.find("span", class_="nivelVaga")
        texto_nivel_vaga = nivel_vaga.text.strip() if nivel_vaga else "Não informado"

        

        # 3. adicionando o que foi extraído nas listas
        cargos.append(texto_cargo)
        empresas.append(texto_empresa)
        cidades.append(texto_cidade)
        niveis.append(texto_nivel_vaga)

        
    # 4. Retornar DataFrame
    import pandas as pd
    df = pd.DataFrame({
        "cargo": cargos,
        "empresa": empresas,
        "cidade": cidades,
        "nivel": niveis
    })

    return df
        
urls = {
    "analista-de-dados": "https://www.vagas.com.br/vagas-de-analista-de-dados",
    "engenheiro-de-software": "https://www.vagas.com.br/vagas-de-engenheiro-de-software",
    "devops": "https://www.vagas.com.br/vagas-de-devops",
    "marketing": "https://www.vagas.com.br/vagas-de-marketing",
    "vendas": "https://www.vagas.com.br/vagas-de-vendas",
    "financeiro": "https://www.vagas.com.br/vagas-de-financeiro",
    "logistica": "https://www.vagas.com.br/vagas-de-logistica",
    "recursos-humanos": "https://www.vagas.com.br/vagas-de-recursos-humanos",
    "administrativo": "https://www.vagas.com.br/vagas-de-administrativo",
    "enfermagem": "https://www.vagas.com.br/vagas-de-enfermagem",
}

todos_dfs = []

for area, url in urls.items():
    print(f"Coletando: {area}")
    soup = buscar_vagas(url)
    vagas = extrair_vagas(soup)
    df = extrair_detalhes(vagas)
    df["area"] = area  # adiciona coluna area
    todos_dfs.append(df)

df_final = pd.concat(todos_dfs, ignore_index=True)
print(df_final.shape)

df_final = pd.concat(todos_dfs, ignore_index=True)
exportar_csv(df_final, "../data/raw/VAGAS.csv")
