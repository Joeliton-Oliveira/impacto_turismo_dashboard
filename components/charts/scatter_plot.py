# components/charts/scatter_plot.py

import streamlit as st
import pandas as pd
import plotly.express as px


def exibir_grafico_dispersao(df: pd.DataFrame):
    """
    Exibe gráficos de dispersão relacionando percepção populacional e intensidade forte
    dos impactos turísticos, separados por percepção positiva e negativa.

    Args:
        df (pd.DataFrame): DataFrame filtrado.
    """
    if df.empty or "impacto_esperado" not in df.columns:
        st.info("⚠️ Nenhum dado disponível para o gráfico de dispersão.")
        return

    st.markdown("## Correlação: Percepção × Intensidade Forte")
    st.caption("Compara o quanto a percepção do público se alinha com a força real do impacto.")

    tab_pos, tab_neg = st.tabs(["✅ Percepção Positiva", "⚠️ Percepção Negativa"])

    # Mapeamento para simplificar lógica por aba
    configuracoes = [
        {
            "aba": tab_pos,
            "tipo": "positivo",
            "coluna_percepcao": "percepcao_positiva"
        },
        {
            "aba": tab_neg,
            "tipo": "negativo",
            "coluna_percepcao": "percepcao_negativa"
        }
    ]

    # Paleta acessível para daltônicos (Color Universal Design)
    paleta_acessivel = ["#0072B2", "#E69F00", "#009E73", "#D55E00", "#CC79A7", "#F0E442", "#999999"]

    for config in configuracoes:
        with config["aba"]:
            col_percepcao = config["coluna_percepcao"]

            if col_percepcao not in df.columns:
                st.warning(f"A coluna {col_percepcao} não foi encontrada.")
                continue

            df_foco = (
                df[df["impacto_esperado"] == config["tipo"]]
                .copy()
                .dropna(subset=[col_percepcao, "intensidade_forte"])
            )

            if df_foco.empty:
                st.warning(f"Nenhum dado disponível para percepção {config['tipo']}.")
                continue

            fig = px.scatter(
                df_foco,
                x=col_percepcao,
                y="intensidade_forte",
                size="intensidade_forte",
                color="cidade",
                trendline="ols",
                hover_data=["indicador", "cidade", col_percepcao, "intensidade_forte"],
                labels={
                    col_percepcao: "Percepção da População",
                    "intensidade_forte": "Intensidade Forte"
                },
                title=f"Correlação - Impactos {config['tipo'].capitalize()}s",
                color_discrete_sequence=paleta_acessivel
            )

            fig.update_layout(
                xaxis_title="Percepção da População",
                yaxis_title="Intensidade Forte",
                legend_title="Cidade",
                margin=dict(t=60, b=40),
                paper_bgcolor="#F1FBF5",
                plot_bgcolor="#F1FBF5"
            )

            st.plotly_chart(fig, use_container_width=True)