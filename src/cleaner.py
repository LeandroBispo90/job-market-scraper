import pandas as pd


def carregar_dados(caminho):
    
    df = pd.read_csv(caminho, sep=";")

    return df

df = carregar_dados("../data/processed/VAGAS.csv")
print(df.shape) 



def filtrar_vagas(df):
    palavras_chave = ["dados", "data", "analytics", "bi", "business intelligence", "sql", "python"]
    padrao = "|".join(palavras_chave)
    df_filtrado = df[df["cargo"].str.contains(padrao, case=False, na=False)]
    return df_filtrado  # ← dentro da função mas sem indentação extra

# fora da função
df_filtrado = filtrar_vagas(df)
print(df.shape)

def limpar_dados(df_filtrado):

    df_limpo = df_filtrado.drop_duplicates(subset=["cargo"], keep="first").copy()
    df_limpo["cargo"] = df_limpo["cargo"].str.strip()
    df_limpo["empresa"] = df_limpo["empresa"].str.strip()
    df_limpo["cidade"] = df_limpo["cidade"].str.replace(r'\s+', ' ', regex=True)
    df_limpo["cidade"] = df_limpo["cidade"].str.strip()
    df_limpo[["cidade", "estado"]] = df_limpo["cidade"].str.split(" / ", expand=True)

    return df_limpo

df_limpo = limpar_dados(df)
df_limpo.to_csv("../data/processed/vagas_limpo.csv", index=False, encoding="utf-8-sig", sep=";")

print(f"Total de vagas após limpeza: {len(df_limpo)}")