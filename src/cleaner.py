import os
import pandas as pd
from exporter import exportar_csv 



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_PATH = os.path.join(BASE_DIR, "data", "raw", "VAGAS.csv")

def carregar_dados(caminho):
    df = pd.read_csv(caminho, sep=";")
    return df

def limpar_dados(df):
    # remove duplicatas por cargo + empresa
    df_limpo = df.drop_duplicates(subset=["cargo", "empresa"], keep="first").copy()
    
    # limpa textos
    df_limpo["cargo"] = df_limpo["cargo"].str.strip()
    df_limpo["empresa"] = df_limpo["empresa"].str.strip()
    
    # limpa e separa cidade e estado
    df_limpo["cidade"] = df_limpo["cidade"].str.replace(r'\s+', ' ', regex=True)
    df_limpo["cidade"] = df_limpo["cidade"].str.strip()
    df_limpo[["cidade", "estado"]] = df_limpo["cidade"].str.split(" / ", expand=True)
    
    # padroniza area
    df_limpo["area"] = df_limpo["area"].str.replace("-", " ").str.title()
    
    return df_limpo

# execução
df = carregar_dados(RAW_PATH)
print(f"Bruto: {df.shape}")

df_limpo = limpar_dados(df)
print(f"Limpo: {df_limpo.shape}")

PROCESSED_PATH = os.path.join(BASE_DIR, "data", "processed", "vagas_limpo.csv")
exportar_csv(df_limpo, PROCESSED_PATH)
print(f"Total de vagas após limpeza: {len(df_limpo)}")