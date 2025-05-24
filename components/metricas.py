# components/metricas.py

import streamlit as st
import pandas as pd

def exibir_metricas(df: pd.DataFrame):
    """
    Exibe as métricas principais de resumo do dashboard:
    - Total de registros
    - Total de cidades únicas
    - Total de indicadores únicos

    Args:
        df (pd.DataFrame): DataFrame já filtrado.
    """
    st.markdown("## 📈 Visão Geral dos Dados")
    st.caption("Resumo numérico dos dados filtrados: total de respostas, abrangência geográfica e diversidade de indicadores.")
    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📂 Total de Registros", len(df))

    with col2:
        st.metric("🌍 Total de Cidades", df["cidade"].nunique())

    with col3:
        st.metric("📌 Indicadores Únicos", df["indicador"].nunique())
