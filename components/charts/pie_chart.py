# components/charts/pie_chart.py

import streamlit as st
import pandas as pd
import plotly.express as px

def exibir_grafico_pizza(df: pd.DataFrame):
    """
    Renderiza um gráfico de pizza (do tipo donut) para mostrar a distribuição
    de percepções (positivo vs. negativo) no conjunto de dados filtrado.

    Args:
        df (pd.DataFrame): DataFrame já filtrado.
    """
    if df.empty or "impacto_esperado" not in df.columns:
        st.info("Nenhum dado disponível para o gráfico de percepção global.")
        return

    st.markdown("## 🧭 Percepção Global dos Impactos")

    df_pizza = df["impacto_esperado"].value_counts().reset_index()
    df_pizza.columns = ["impacto_esperado", "quantidade"]

    fig = px.pie(
        df_pizza,
        names="impacto_esperado",
        values="quantidade",
        hole=0.4,
        color_discrete_sequence=["#10b981", "#ef4444"]  # Verde (positivo), Vermelho (negativo)
    )

    st.plotly_chart(fig, use_container_width=True)
