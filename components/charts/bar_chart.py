import streamlit as st
import pandas as pd
import plotly.express as px

color_map = {
    "intensidade_fraco": "#0072B2",     # Azul escuro
    "intensidade_moderado": "#E69F00",  # Laranja vibrante
    "intensidade_forte": "#D55E00"      # Vermelho escuro
}

intensidade_cols = {
    "fraco": "intensidade_fraco",
    "moderado": "intensidade_moderado",
    "forte": "intensidade_forte"
}

def exibir_grafico_barras(df: pd.DataFrame, filtros: dict):
    """
    Exibe gráficos de barras empilhadas, respeitando filtro de intensidade.

    Args:
        df (pd.DataFrame): DataFrame filtrado.
        filtros (dict): Filtros aplicados.
    """

    # Se não tiver intensidade selecionada → não plota
    if not filtros.get("intensidade"):
        st.info("ℹ️ Selecione ao menos um nível de intensidade para exibir os gráficos.")
        return

    st.markdown("## Comparação de Intensidades por Cidade")
    st.caption("Volume de respostas por tipo de impacto e percepção populacional.")

    tipos = sorted(df["tipo_impacto"].dropna().unique())
    percepcoes = ["positivo", "negativo"]

    colunas_intensidade_ativas = [intensidade_cols[i] for i in filtros["intensidade"]]

    for tipo in tipos:
        for percepcao in percepcoes:
            dados = df[(df["tipo_impacto"] == tipo) & (df["impacto_esperado"] == percepcao)]

            if dados.empty:
                continue

            dados_agrupados = (
                dados.groupby("cidade")[colunas_intensidade_ativas]
                .sum()
                .reset_index()
                .sort_values("cidade")
            )

            # Ordena as intensidades da menor soma para a maior
            somas = dados_agrupados[colunas_intensidade_ativas].sum()
            colunas_ordenadas = somas.sort_values().index.tolist()

            fig = px.bar(
                dados_agrupados,
                x="cidade",
                y=colunas_ordenadas,
                title=f"{tipo} - Impactos {percepcao.capitalize()}s",
                labels={"value": "Nível de Intensidade", "cidade": "Cidade"},
                text_auto=True,
                color_discrete_map=color_map
            )

            fig.update_layout(
                barmode="stack",
                xaxis_title="Cidade",
                yaxis_title="Quantidade de Registros",
                legend_title="Intensidade",
                margin=dict(t=60, b=40),
                paper_bgcolor="#F1FBF5",
                plot_bgcolor="#F1FBF5"
            )

            st.plotly_chart(fig, use_container_width=True)
