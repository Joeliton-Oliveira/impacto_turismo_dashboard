# main.py

import streamlit as st

# Importações internas (módulos do projeto)
from style.estilos import aplicar_estilo
from components.layout import exibir_cabecalho
from data.carregamento_dados import carregar_dados
from components.filtros import aplicar_filtros
from components.metricas import exibir_metricas
from components.charts.bar_chart import exibir_grafico_barras
from components.charts.pie_chart import exibir_grafico_pizza
from components.charts.heatmap import exibir_heatmap
from components.charts.scatter_plot import exibir_grafico_dispersao

# Configurações iniciais da página
st.set_page_config(
    page_title="Impacto do Turismo nas Cidades",
    layout="wide"
)

# Aplicação do tema visual
aplicar_estilo()

# Exibição do cabeçalho com logo e título
exibir_cabecalho()

# Carregamento dos dados
df = carregar_dados()


# Filtros e dados filtrados
df_filtrado, filtros = aplicar_filtros(df)

# Verifica se filtros essenciais foram aplicados
if not filtros["cidade"] or not filtros["tipo_impacto"] or df_filtrado.empty:
    st.info("Nenhum dado encontrado. Selecione ao menos uma cidade e um tipo de impacto para gerar os gráficos.")
else:
    # Exibição de métricas principais
    exibir_metricas(df_filtrado)

    # Geração dos gráficos
    exibir_grafico_barras(df_filtrado)
    exibir_grafico_pizza(df_filtrado)
    exibir_heatmap(df_filtrado)
    exibir_grafico_dispersao(df_filtrado)

    # Legenda visual
    st.markdown("### 🧾 Legenda Visual")
    st.markdown("- 🟦 **Positivo:** Impactos com expectativa ou resultado benéfico")
    st.markdown("- 🟧 **Negativo:** Impactos com expectativa ou resultado prejudicial")
    st.markdown("- ⚪ **Neutro:** Respostas intermediárias ou avaliativas (pode ser incluído se houver)")
