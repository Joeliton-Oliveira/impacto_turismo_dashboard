# components/charts/heatmap.py

import streamlit as st
import pandas as pd
import plotly.express as px


def exibir_heatmap(df: pd.DataFrame):
    """
    Exibe mapas de calor com a soma da intensidade forte por indicador e cidade,
    separados por tipo de percepção (positivo/negativo).

    Args:
        df (pd.DataFrame): DataFrame filtrado.
    """
    if df.empty or "impacto_esperado" not in df.columns:
        st.info("⚠️ Nenhum dado disponível para o mapa de calor.")
        return

    st.markdown("## Mapa de Calor de Intensidade Forte")
    st.caption("Visualização da concentração dos impactos mais intensos, por cidade e indicador.")

    aba_pos, aba_neg = st.tabs(["✅ Positivo", "⚠️ Negativo"])

    for impacto, aba in zip(["positivo", "negativo"], [aba_pos, aba_neg]):
        with aba:
            df_sub = df[df["impacto_esperado"] == impacto]

            if df_sub.empty:
                st.warning(f"Nenhum dado disponível para impacto {impacto}.")
                continue

            df_heat = (
                df_sub.groupby(["cidade", "indicador"])["intensidade_forte"]
                .sum()
                .reset_index()
            )

            fig = px.density_heatmap(
                df_heat,
                x="cidade",
                y="indicador",
                z="intensidade_forte",
                color_continuous_scale="Cividis",
                title=f"Impactos {impacto.capitalize()}s",
                text_auto=True,
                nbinsx=len(df_heat["cidade"].unique()),
                nbinsy=len(df_heat["indicador"].unique())
            )

            fig.update_layout(
                xaxis_title="Cidade",
                yaxis_title="Indicador",
                margin=dict(t=60, b=40),
                coloraxis_colorbar=dict(title="Intensidade Forte"),
                paper_bgcolor="#F1FBF5",
                plot_bgcolor="#F1FBF5"
            )

            fig.update_traces(hovertemplate="Cidade: %{x}<br>Indicador: %{y}<br>Intensidade Forte: %{z}<extra></extra>")

            st.plotly_chart(fig, use_container_width=True)
