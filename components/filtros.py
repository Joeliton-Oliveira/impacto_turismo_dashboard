# components/filtros.py

import streamlit as st
import pandas as pd

def aplicar_filtros(df: pd.DataFrame):
    """
    Aplica filtros interativos sobre o DataFrame com base em cidade, impacto, intensidade e indicadores.
    
    Args:
        df (pd.DataFrame): Conjunto de dados completo.

    Returns:
        df_filtrado (pd.DataFrame): Dados após aplicação dos filtros.
        dict: Dicionário com os valores dos filtros aplicados.
    """
    filtros = {}

    # Filtro por cidade
    filtros["cidade"] = st.multiselect("Selecione a(s) cidade(s):", sorted(df["cidade"].dropna().unique()))

    # Filtro por tipo de impacto
    filtros["tipo_impacto"] = st.multiselect("Tipo de Impacto:", sorted(df["tipo_impacto"].dropna().unique()))

    # Filtro por percepção do impacto
    filtros["impacto_esperado"] = st.multiselect("Impacto Esperado:", sorted(df["impacto_esperado"].dropna().unique()))

    # Filtros por indicadores agrupados por tipo e percepção
    st.markdown("### Indicadores por Tipo de Impacto e Percepção")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Econômico")
        filtros["eco_positivo"] = st.multiselect("Positivos (Econômico):",
            sorted(df[(df.tipo_impacto == "Econômico") & (df.impacto_esperado == "positivo")]["indicador"].dropna().unique()))
        filtros["eco_negativo"] = st.multiselect("Negativos (Econômico):",
            sorted(df[(df.tipo_impacto == "Econômico") & (df.impacto_esperado == "negativo")]["indicador"].dropna().unique()))
    with col2:
        st.subheader("Social")
        filtros["soc_positivo"] = st.multiselect("Positivos (Social):",
            sorted(df[(df.tipo_impacto == "Social") & (df.impacto_esperado == "positivo")]["indicador"].dropna().unique()))
        filtros["soc_negativo"] = st.multiselect("Negativos (Social):",
            sorted(df[(df.tipo_impacto == "Social") & (df.impacto_esperado == "negativo")]["indicador"].dropna().unique()))
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Ambiental")
        filtros["amb_positivo"] = st.multiselect("Positivos (Ambiental):",
            sorted(df[(df.tipo_impacto == "Ambiental") & (df.impacto_esperado == "positivo")]["indicador"].dropna().unique()))
    with col4:
        st.subheader("")
        filtros["amb_negativo"] = st.multiselect("Negativos (Ambiental):",
            sorted(df[(df.tipo_impacto == "Ambiental") & (df.impacto_esperado == "negativo")]["indicador"].dropna().unique()))

    # Intensidade dos impactos
    filtros["intensidade"] = st.multiselect("Intensidade:", ["fraco", "moderado", "forte"])

    # Aplicação dos filtros ao DataFrame
    df_filtrado = df.copy()

    if filtros["cidade"]:
        df_filtrado = df_filtrado[df_filtrado["cidade"].isin(filtros["cidade"])]

    if filtros["tipo_impacto"]:
        df_filtrado = df_filtrado[df_filtrado["tipo_impacto"].isin(filtros["tipo_impacto"])]

    if filtros["impacto_esperado"]:
        df_filtrado = df_filtrado[df_filtrado["impacto_esperado"].isin(filtros["impacto_esperado"])]

    # Filtro geral por indicadores
    indicadores_selecionados = filtros["eco_positivo"] + filtros["eco_negativo"] + \
                                filtros["soc_positivo"] + filtros["soc_negativo"] + \
                                filtros["amb_positivo"] + filtros["amb_negativo"]
    if indicadores_selecionados:
        df_filtrado = df_filtrado[df_filtrado["indicador"].isin(indicadores_selecionados)]

    return df_filtrado, filtros
