# components/charts/pie_chart.py

import streamlit as st
import pandas as pd
import plotly.express as px


def exibir_grafico_pizza(df: pd.DataFrame):
    """
    Exibe a proporção total de percepções positivas vs negativas em formato de gráfico de pizza.
    Também exibe gráfico de barras agrupadas com total de intensidade por tipo de impacto.

    Args:
        df (pd.DataFrame): DataFrame filtrado.
    """
    if df.empty or "impacto_esperado" not in df.columns:
        st.info("⚠️ Nenhum dado disponível para o gráfico de percepção global.")
        return

    st.markdown("## Percepção Global dos Impactos")
    st.caption("Distribuição entre percepções positivas e negativas sobre o turismo.")

    # Gráfico de Pizza (Donut)
    df_pizza = df["impacto_esperado"].value_counts().reset_index()
    df_pizza.columns = ["impacto_esperado", "quantidade"]

    fig_pizza = px.pie(
        df_pizza,
        names="impacto_esperado",
        values="quantidade",
        hole=0.4,
        color="impacto_esperado",
        color_discrete_map={"positivo": "#0072B2", "negativo": "#E69F00"},
    )

    fig_pizza.update_layout(
        margin=dict(t=20, b=20),
        paper_bgcolor="#F1FBF5",
        plot_bgcolor="#F1FBF5"
    )

    fig_pizza.update_layout(
        margin=dict(t=20, b=20),
        paper_bgcolor="#F1FBF5",
        plot_bgcolor="#F1FBF5"
    )
    st.plotly_chart(fig_pizza, use_container_width=True)

    # Gráfico de Barras por Tipo de Impacto
    st.markdown("## Intensidade Total por Tipo de Impacto")
    st.caption("Soma das intensidades fraco, moderado e forte para cada dimensão analisada.")

    intensidades = ["intensidade_fraco", "intensidade_moderado", "intensidade_forte"]
    df_barras = (
        df.groupby("tipo_impacto")[intensidades]
        .sum()
        .reset_index()
        .sort_values("tipo_impacto")
    )

    fig_barras = px.bar(
        df_barras,
        x="tipo_impacto",
        y=intensidades,
        barmode="group",
        labels={"value": "Intensidade Total", "tipo_impacto": "Tipo de Impacto"},
        text_auto=True,
        color_discrete_map={
        "intensidade_fraco": "#0072B2",     # Azul escuro
        "intensidade_moderado": "#E69F00",  # Laranja vibrante
        "intensidade_forte": "#D55E00"      # Vermelho escuro acessível
        }
    )

    fig_barras.update_layout(
        xaxis_title="Tipo de Impacto",
        yaxis_title="Total de Respostas",
        legend_title="Nível de Intensidade",
        margin=dict(t=40, b=40),
        paper_bgcolor="#F1FBF5",
        plot_bgcolor="#F1FBF5"
    )

    st.plotly_chart(fig_barras, use_container_width=True)
