# 📊 Impacto do Turismo nas Cidades

Dashboard analítico desenvolvido em **Python + Streamlit** com foco na **avaliação dos impactos sociais, econômicos e ambientais do turismo** em diferentes municípios. Estruturado com **Clean Architecture**, modularização funcional e visualização estratégica para ambientes corporativos, acadêmicos e governamentais.

---

## 🧰 Tecnologias Utilizadas

- [Python 3.12](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Plotly Express](https://plotly.com/python/)
- [Pandas](https://pandas.pydata.org/)
- Arquitetura modular (Clean Code)

---

## 🎯 Funcionalidades do Dashboard

- ✅ Filtros interativos por cidade, tipo de impacto, percepção e intensidade
- 📈 Gráficos profissionais:
  - Barras empilhadas por cidade, tipo e intensidade
  - Pizza (donut) com percepção global
  - Heatmaps por indicador e cidade
  - Dispersão de percepção x intensidade
- 🧠 Métricas executivas (total de registros, cidades, indicadores)
- 🎨 Tema escuro personalizado e visual corporativo

---

## 🗂 Estrutura Modular

impacto_turismo_dashboard/
├── main.py                        # Ponto de entrada da aplicação
├── assets/                        # Arquivos estáticos (imagens, logos)
│   └── logo_embrapa.png
├── data/                          # Camada de dados (input e pré-processamento)
│   └── carregamento_dados.py
├── style/                         # Camada de estilo visual
│   └── estilos.py
└── components/                    # Componentes visuais e funcionais
    ├── layout.py                 # Logo, título e cabeçalho animado
    ├── filtros.py               # Filtros interativos (multiselects)
    ├── metricas.py              # KPIs principais (total de registros, cidades, indicadores)
    └── charts/                  # Gráficos e visualizações
        ├── bar_chart.py         # Gráficos de barras empilhadas
        ├── pie_chart.py         # Gráfico de pizza (percepção global)
        ├── heatmap.py           # Mapas de calor (impacto por cidade e indicador)
        └── scatter_plot.py      # Gráficos de dispersão (percepção vs intensidade)
