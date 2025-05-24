# components/charts/bar_chart.py

import streamlit as st
import pandas as pd
import plotly.express as px

# Paleta institucional padronizada
color_map = {
    "intensidade_fraco": "#3b82f6",      # Azul
    "intensidade_moderado": "#10b981",  # Verde
    "intensidade_forte": "#ef4444"      # Vermelho
}

def exibir_grafico_barras(df: pd.DataFrame):
    """
    Renderiza gráficos de barras empilhadas por cidade, divididos por tipo de impacto
    (econômico, social, ambiental) e percepção (positivo/negativo).

    Args:
        df (pd.DataFrame): DataFrame já filtrado.
    """
    if df.empty or "cidade" not in df.columns:
        st.info("Nenhum dado disponível para os gráficos de barras.")
        return

    st.markdown("## 🏙️ Comparações por Cidade")

    tipos_impacto = sorted(df["tipo_impacto"].dropna().unique())

    for impacto in tipos_impacto:
        for esperado in ["positivo", "negativo"]:
            df_filtro = df[(df.tipo_impacto == impacto) & (df.impacto_esperado == esperado)]

            if df_filtro.empty:
                continue

            # Agrupamento por cidade e intensidade
            df_grouped = df_filtro.groupby("cidade")[["intensidade_fraco", "intensidade_moderado", "intensidade_forte"]].sum().reset_index()
            df_melt = df_grouped.melt(id_vars="cidade", var_name="intensidade", value_name="respostas")

            # Gráfico
            fig = px.bar(
                df_melt,
                x="cidade",
                y="respostas",
                color="intensidade",
                color_discrete_map=color_map,
                barmode="stack",
                title=f"Impactos {impacto} {esperado.capitalize()}s por Cidade"
            )
            fig.update_layout(bargap=0.5)

            st.plotly_chart(fig, use_container_width=True)
