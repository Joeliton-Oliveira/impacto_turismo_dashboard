import pandas as pd
import streamlit as st

@st.cache_data
def carregar_dados(caminho_arquivo="dados_organizados_embrapa.xlsx") -> pd.DataFrame:
    """
    Carrega os dados do arquivo Excel, padroniza os nomes das colunas e trata os campos de impacto.

    Args:
        caminho_arquivo (str): Caminho para o arquivo de dados. Default é o nome padrão esperado.

    Returns:
        pd.DataFrame: DataFrame com colunas limpas e campos normalizados.
    """
    df = pd.read_excel(caminho_arquivo)

    # Normaliza os nomes das colunas (snake_case)
    df.columns = [col.lower().strip().replace(" ", "_") for col in df.columns]

    # Padroniza valores textuais importantes
    if "tipo_impacto" in df.columns:
        df["tipo_impacto"] = df["tipo_impacto"].str.lower().str.capitalize()

    if "impacto_esperado" in df.columns:
        df["impacto_esperado"] = df["impacto_esperado"].str.lower()

    return df
