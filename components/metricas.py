import streamlit as st
import pandas as pd

def exibir_metricas(df: pd.DataFrame):
    """
    Exibe a visão geral numérica simplificada dos dados:
    - Total de registros válidos
    - Número de cidades com dados
    - Número de indicadores únicos
    """
    st.markdown("## Visão Geral dos Dados")
    st.caption("Resumo numérico simplificado dos dados filtrados.")
    st.markdown("---")

    total_registros = len(df)
    total_cidades = df["cidade"].nunique()
    total_indicadores = df["indicador"].nunique()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total de Registros", total_registros)
    with col2:
        st.metric("Total de Cidades", total_cidades)
    with col3:
        st.metric("Indicadores Únicos", total_indicadores)
