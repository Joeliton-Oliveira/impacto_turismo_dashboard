# components/charts/scatter_plot.py

import streamlit as st
import pandas as pd
import plotly.express as px

def exibir_grafico_dispersao(df: pd.DataFrame):
    """
    Gera dois gráficos de dispersão (um para percepção positiva e outro negativa)
    relacionando os valores reais de percepção com a intensidade forte dos impactos.

    Args:
        df (pd.DataFrame): DataFrame filtrado.
    """
    if df.empty:
        st.info("Nenhum dado disponível para o gráfico de dispersão.")
        return

    st.markdown("## 🎯 Correlação: Percepção vs Intensidade Forte")

    # --- Gráfico 1: Percepção Positiva ---
    st.markdown("### Percepção Positiva")

    if "percepcao_positiva" in df.columns:
        df_pos = df[df["impacto_esperado"] == "positivo"].copy()
        df_pos = df_pos[df_pos["percepcao_positiva"].notnull()]
        df_pos["intensidade_forte"] = df_pos["intensidade_forte"].fillna(0)

        if not df_pos.empty:
            fig_pos = px.scatter(
                df_pos,
                x="percepcao_positiva",
                y="intensidade_forte",
                size="intensidade_forte",
                color="cidade",
                hover_name="indicador",
                title="Percepção Positiva vs Intensidade Forte",
                labels={
                    "percepcao_positiva": "Percepção Positiva",
                    "intensidade_forte": "Intensidade Forte"
                }
            )
            st.plotly_chart(fig_pos, use_container_width=True)
        else:
            st.warning("Sem dados disponíveis para percepção positiva.")
    else:
        st.warning("Coluna 'percepcao_positiva' não encontrada no DataFrame.")

    # --- Gráfico 2: Percepção Negativa ---
    st.markdown("### Percepção Negativa")

    if "percepcao_negativa" in df.columns:
        df_neg = df[df["impacto_esperado"] == "negativo"].copy()
        df_neg = df_neg[df_neg["percepcao_negativa"].notnull()]
        df_neg["intensidade_forte"] = df_neg["intensidade_forte"].fillna(0)

        if not df_neg.empty:
            fig_neg = px.scatter(
                df_neg,
                x="percepcao_negativa",
                y="intensidade_forte",
                size="intensidade_forte",
                color="cidade",
                hover_name="indicador",
                title="Percepção Negativa vs Intensidade Forte",
                labels={
                    "percepcao_negativa": "Percepção Negativa",
                    "intensidade_forte": "Intensidade Forte"
                }
            )
            st.plotly_chart(fig_neg, use_container_width=True)
        else:
            st.warning("Sem dados disponíveis para percepção negativa.")
    else:
        st.warning("Coluna 'percepcao_negativa' não encontrada no DataFrame.")
