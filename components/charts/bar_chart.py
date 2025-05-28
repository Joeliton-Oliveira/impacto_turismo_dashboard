# components/charts/bar_chart.py

import streamlit as st
import pandas as pd
import plotly.express as px

color_map = {
    "intensidade_fraco": "#0072B2",     # Azul escuro (Color Universal Design)
    "intensidade_moderado": "#E69F00",  # Laranja vibrante
    "intensidade_forte": "#D55E00"      # Vermelho escuro (contrastante com laranja)
}



def exibir_grafico_barras(df: pd.DataFrame):
    """
    Exibe gráficos de barras empilhadas por cidade, para cada combinação de:
    - tipo_impacto (Econômico, Social, Ambiental)
    - impacto_esperado (Positivo ou Negativo)

    Args:
        df (pd.DataFrame): DataFrame filtrado.
    """
    if df.empty or "cidade" not in df.columns:
        st.warning("⚠️ Nenhum dado disponível para exibição dos gráficos.")
        return

    st.markdown("## 🏙️ Comparação de Intensidades por Cidade")
    st.caption("Volume de respostas por tipo de impacto e percepção populacional.")

    tipos = sorted(df["tipo_impacto"].dropna().unique())
    percepcoes = ["positivo", "negativo"]
    intensidades = ["intensidade_fraco", "intensidade_moderado", "intensidade_forte"]

    for tipo in tipos:
        for percepcao in percepcoes:
            dados = df[(df["tipo_impacto"] == tipo) & (df["impacto_esperado"] == percepcao)]

            if dados.empty:
                continue

            dados_agrupados = (
                dados.groupby("cidade")[intensidades]
                .sum()
                .reset_index()
                .sort_values("cidade")
            )

            fig = px.bar(
                dados_agrupados,
                x="cidade",
                y=intensidades,
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
