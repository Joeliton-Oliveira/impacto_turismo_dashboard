import pandas as pd

def carregar_dados(caminho_arquivo="dados_organizados_embrapa.xlsx") -> pd.DataFrame:
    """
    Carrega e padroniza os dados da planilha principal.

    Parâmetros:
        caminho_arquivo (str): Caminho do arquivo Excel com os dados.
    
    Retorno:
        pd.DataFrame: DataFrame padronizado e pronto para análise.
    """
    df = pd.read_excel(caminho_arquivo)

    # Padronização de colunas
    df.columns = [col.lower().strip().replace(" ", "_") for col in df.columns]

    # Ajustes nos valores
    df["tipo_impacto"] = df["tipo_impacto"].str.lower().str.strip()
    df["impacto_esperado"] = df["impacto_esperado"].str.lower().str.strip()
    df["cidade"] = df["cidade"].str.strip().str.capitalize()

    return df
