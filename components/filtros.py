import streamlit as st
import pandas as pd

def aplicar_filtros(df):
    st.sidebar.markdown("## 🎯 Filtros Interativos")

    # Inicialização segura com valores padrão
    if "filtro_cidades" not in st.session_state:
        st.session_state["filtro_cidades"] = df["cidade"].unique().tolist()

    if "filtro_tipo_impacto" not in st.session_state:
        st.session_state["filtro_tipo_impacto"] = df["tipo_impacto"].unique().tolist()

    if "filtro_intensidade" not in st.session_state:
        st.session_state["filtro_intensidade"] = ["fraco", "moderado", "forte"]

    if "filtro_percepcao" not in st.session_state:
        st.session_state["filtro_percepcao"] = ["positivo", "negativo"]

    # Filtros interativos vinculados ao session_state
    st.sidebar.multiselect("🏙️ Cidades:", 
        options=sorted(df["cidade"].unique()), 
        key="filtro_cidades")

    st.sidebar.multiselect("📂 Tipo de Impacto:", 
        options=sorted(df["tipo_impacto"].unique()), 
        key="filtro_tipo_impacto")

    st.sidebar.multiselect("🔥 Intensidade:", 
        options=["fraco", "moderado", "forte"], 
        key="filtro_intensidade")

    st.sidebar.multiselect("💬 Percepção do Impacto:", 
        options=["positivo", "negativo"], 
        key="filtro_percepcao")


def aplicar_filtros(df: pd.DataFrame):
    """
    Aplica filtros interativos organizados na barra lateral, incluindo:
    - Cidades
    - Tipo de impacto
    - Intensidade (fraco, moderado, forte)
    - Percepção do impacto
    - Indicadores organizados por tipo/percepção

    Args:
        df (pd.DataFrame): DataFrame com os dados brutos.

    Returns:
        df_filtrado (pd.DataFrame): Dados filtrados conforme seleção.
        dict_filtros (dict): Dicionário com os filtros aplicados.
    """
    with st.sidebar:
        st.header("🎯 Filtros Interativos")

        # 1. Filtro por cidade
        cidades = st.multiselect("🌍 Cidades:", sorted(df["cidade"].dropna().unique()))

        # 2. Filtro por tipo de impacto
        tipos_impacto = st.multiselect("📂 Tipo de Impacto:", sorted(df["tipo_impacto"].dropna().unique()))

        # 3. Filtro por intensidade de impacto
        st.markdown("#### 🔥 Nível de Intensidade")
        intensidade_opcoes = ["fraco", "moderado", "forte"]
        intensidades = st.multiselect("Intensidade:", intensidade_opcoes, default=[])

        # 4. Filtro por percepção (positivo ou negativo)
        percepcoes = st.multiselect("💬 Percepção do Impacto:", sorted(df["impacto_esperado"].dropna().unique()))

        # 5. Filtros por indicadores agrupados
        st.markdown("#### 🧭 Indicadores por Categoria")

        def indicadores_por_categoria(tipo, esperado):
            return sorted(df[
                (df["tipo_impacto"] == tipo) & 
                (df["impacto_esperado"] == esperado)
            ]["indicador"].dropna().unique())

        indicadores_econ_pos = st.multiselect("💰 Econômico Positivo", indicadores_por_categoria("Econômico", "positivo"))
        indicadores_econ_neg = st.multiselect("💸 Econômico Negativo", indicadores_por_categoria("Econômico", "negativo"))
        indicadores_soc_pos  = st.multiselect("🤝 Social Positivo", indicadores_por_categoria("Social", "positivo"))
        indicadores_soc_neg  = st.multiselect("🚧 Social Negativo", indicadores_por_categoria("Social", "negativo"))
        indicadores_amb_pos  = st.multiselect("🌱 Ambiental Positivo", indicadores_por_categoria("Ambiental", "positivo"))
        indicadores_amb_neg  = st.multiselect("♻️ Ambiental Negativo", indicadores_por_categoria("Ambiental", "negativo"))

    # Aplicação dos filtros no DataFrame
    df_filtrado = df.copy()

    if cidades:
        df_filtrado = df_filtrado[df_filtrado["cidade"].isin(cidades)]

    if tipos_impacto:
        df_filtrado = df_filtrado[df_filtrado["tipo_impacto"].isin(tipos_impacto)]

    # Aplicar filtro por intensidade (mantém registros com valor > 0 nas colunas de intensidade)
    intensidade_cols = {
        "fraco": "intensidade_fraco",
        "moderado": "intensidade_moderado",
        "forte": "intensidade_forte"
    }

    if intensidades:
        filtros_int = [df[df[col] > 0] for col in [intensidade_cols[i] for i in intensidades]]
        df_filtrado = pd.concat([df_filtrado] + filtros_int).drop_duplicates()

    if percepcoes:
        df_filtrado = df_filtrado[df_filtrado["impacto_esperado"].isin(percepcoes)]

    # Consolidar todos os indicadores selecionados
    indicadores_escolhidos = (
        indicadores_econ_pos + indicadores_econ_neg +
        indicadores_soc_pos  + indicadores_soc_neg +
        indicadores_amb_pos  + indicadores_amb_neg
    )

    if indicadores_escolhidos:
        df_filtrado = df_filtrado[df_filtrado["indicador"].isin(indicadores_escolhidos)]

    # Dicionário com os filtros aplicados
    dict_filtros = {
        "cidade": cidades,
        "tipo_impacto": tipos_impacto,
        "intensidade": intensidades,
        "impacto_esperado": percepcoes,
        "indicadores": indicadores_escolhidos
    }

    return df_filtrado, dict_filtros
