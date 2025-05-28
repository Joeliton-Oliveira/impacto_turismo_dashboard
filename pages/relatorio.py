'''
import streamlit as st
import pandas as pd
from jinja2 import Template
from pathlib import Path
from utils.carregamento import carregar_dados



st.set_page_config(page_title="Relatório Dinâmico", layout="wide")
'''
import streamlit as st
import pandas as pd
from jinja2 import Template
from pathlib import Path
from utils.carregamento import carregar_dados
from style.estilos import aplicar_estilo

# ✅ Esta linha deve vir antes de qualquer comando Streamlit
st.set_page_config(page_title="Relatório Dinâmico", layout="wide")

# ✅ Agora sim, aplique o estilo
aplicar_estilo()


# Carrega o DataFrame principal
df = carregar_dados()

# Variáveis dinâmicas simuladas (você pode conectar com análise real dos dados)
dados_dinamicos = {
    "total_registros": len(df),
    "total_indicadores": df["indicador"].nunique(),
    "total_cidades": df["cidade"].nunique(),
    "percent_positivo": round((df["impacto_esperado"] == "positivo").mean() * 100, 1),
    "percent_negativo": round((df["impacto_esperado"] == "negativo").mean() * 100, 1),
    "cidade_destaque_positiva": "Delmiro",
    "top_indicadores_positivos": "Aumento de empregos formais, Identidade local",
    "cidade_destaque_negativa": "Ecqes2",
    "top_indicadores_negativos": "Ocupação desordenada, Erosão do solo",
    "tipo_impacto_dominante_negativo": "Ambiental",
    "tipo_impacto_mais_forte_positivo": "Social",
    "indicadores_destaque_positivo": "Cursos, Visibilidade, Empregos",
    "tipo_impacto_mais_forte_negativo": "Econômico",
    "indicadores_destaque_negativo": "Evasão de recursos, especulação",
    "cidade_mais_positiva_heatmap": "Delmiro",
    "indicador_positivo_heatmap_1": "Empregos formais",
    "indicador_positivo_heatmap_2": "Identidade local",
    "cidade_mais_negativa_heatmap": "Piranhas",
    "indicador_negativo_heatmap_1": "Resíduos",
    "indicador_negativo_heatmap_2": "Tráfego",
    "indicador_alinhado": "Empregos formais",
    "indicador_sensivel_sem_intensidade": "Resíduos turísticos",
    "indicador_forte_sem_percepcao": "Evasão fiscal",
    "insight_percepcao_geral": "A percepção é ligeiramente positiva, mas exige atenção.",
    "insight_discrepancias": "Há desalinhamento entre percepção e evidência em temas ambientais.",
    "cidade_foco_positivo": "Delmiro",
    "cidade_foco_negativo": "Ecqes2",
    "indicadores_com_desalinhamento": "Trânsito, resíduos, especulação"
}

# Template do relatório
template_markdown = '''
# 📝 Relatório de Análise Dinâmica — Impacto do Turismo nas Cidades

## 1. Introdução
Este relatório apresenta uma análise detalhada dos impactos do turismo nas cidades selecionadas. Com base em uma amostra de {{total_registros}} registros válidos, foram identificados {{total_indicadores}} indicadores distintos distribuídos entre {{total_cidades}} cidades.

## 2. Percepção Geral do Turismo
A percepção geral mostra que {{percent_positivo}}% dos impactos foram classificados como positivos, enquanto {{percent_negativo}}% foram considerados negativos.

> Insight: {{insight_percepcao_geral}}

## 3. Cidades com Maior Destaque
A cidade de {{cidade_destaque_positiva}} concentrou impactos positivos de alta intensidade, especialmente nos indicadores {{top_indicadores_positivos}}.

Já {{cidade_destaque_negativa}} se destacou negativamente nos indicadores {{top_indicadores_negativos}}, especialmente em {{tipo_impacto_dominante_negativo}}.

## 4. Análise por Tipo de Impacto
**Impactos Positivos**
- Mais forte em: {{tipo_impacto_mais_forte_positivo}}
- Destaques: {{indicadores_destaque_positivo}}

**Impactos Negativos**
- Mais intenso em: {{tipo_impacto_mais_forte_negativo}}
- Problemas: {{indicadores_destaque_negativo}}

## 5. Heatmap de Impactos Fortes
Os impactos positivos mais intensos aparecem em {{cidade_mais_positiva_heatmap}}, com:
- {{indicador_positivo_heatmap_1}}, {{indicador_positivo_heatmap_2}}

Impactos negativos intensos aparecem em {{cidade_mais_negativa_heatmap}}, como:
- {{indicador_negativo_heatmap_1}}, {{indicador_negativo_heatmap_2}}

## 6. Percepção vs Intensidade
- Alinhado: {{indicador_alinhado}}
- Sensível sem intensidade: {{indicador_sensivel_sem_intensidade}}
- Forte sem percepção: {{indicador_forte_sem_percepcao}}

> Insight: {{insight_discrepancias}}

## 7. Conclusão
Reforçar ações em {{cidade_foco_positivo}}. Atuar estrategicamente sobre {{cidade_foco_negativo}}. Ajustar comunicação sobre: {{indicadores_com_desalinhamento}}.

📌 Este relatório é gerado automaticamente a partir dos dados atuais.
'''

# Renderiza o relatório
template = Template(template_markdown)
relatorio_final = template.render(**dados_dinamicos)

# Exibe no Streamlit
st.markdown(relatorio_final)
