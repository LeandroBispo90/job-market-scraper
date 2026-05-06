import pandas as pd
import os


def exportar_csv(df, caminho):
    """
    Exporta um DataFrame para CSV.
    Cria o diretório automaticamente se não existir.
    """
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    df.to_csv(caminho, index=False, encoding="utf-8-sig", sep=";")
    print(f"✅ CSV salvo em: {caminho} ({len(df)} linhas)")


def exportar_excel(df, caminho):
    """
    Exporta um DataFrame para Excel (.xlsx).
    Cria o diretório automaticamente se não existir.
    """
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    df.to_excel(caminho, index=False)
    print(f"✅ Excel salvo em: {caminho} ({len(df)} linhas)")