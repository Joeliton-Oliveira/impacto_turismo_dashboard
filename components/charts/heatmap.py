# components/charts/heatmap.py

import streamlit as st
import pandas as pd
import plotly.express as px

def exibir_heatmap(df: pd.DataFrame):
    """
    Renderiza mapas de calor da intensidade forte dos impactos por cidade e indicador,
    separados por percepção (positivo e negativo).

    Args:
        df (pd.DataFrame): DataFrame filtrado.
    """
    if df.empty:
        st.info("Nenhum dado disponível para o mapa de calor.")
        return

    st.markdown("## 🌡️ Concentração dos Impactos (Heatmap)")

    for impacto in ["positivo", "negativo"]:
        st.markdown(f"### {impacto.capitalize()}")

        df_sub = df[df["impacto_esperado"] == impacto]

        if df_sub.empty:
            st.warning(f"Sem dados para impacto {impacto}.")
            continue

        # Agrupamento por cidade e indicador, somando intensidade forte
        df_heat = df_sub.groupby(["cidade", "indicador"])["intensidade_forte"].sum().reset_index()

        fig = px.density_heatmap(
            df_heat,
            x="indicador",
            y="cidade",
            z="intensidade_forte",
            color_continuous_scale="Plasma"
        )

        fig.update_layout(
        xaxis_tickangle=100,
        height=500,
        margin=dict(l=20, r=20, t=30, b=120),
        autosize=True,
        legend_title_text="Intensidade Forte"
        )

        st.plotly_chart(fig, use_container_width=True)
