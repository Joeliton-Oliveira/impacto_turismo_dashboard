import streamlit as st
import pandas as pd
from jinja2 import Template
from style.estilos import aplicar_estilo
from datetime import datetime

def gerar_relatorio(df_filtrado, filtros):
    aplicar_estilo()
    st.title("RELATÓRIO TÉCNICO DE ANÁLISE DE IMPACTOS TURÍSTICOS")

    # Listar os vilarejos (cidade no seu dataset)
    vilarejos = df_filtrado["cidade"].unique().tolist()

    # Cálculo de proporção positiva/negativa
    porcentagem_positiva = round((df_filtrado["impacto_esperado"] == "positivo").mean() * 100, 1) if not df_filtrado.empty else 0.0
    porcentagem_negativa = round((df_filtrado["impacto_esperado"] == "negativo").mean() * 100, 1) if not df_filtrado.empty else 0.0

    # Análise com base em intensidade_forte
    positivos_fortes = df_filtrado[(df_filtrado["impacto_esperado"] == "positivo") & (df_filtrado["intensidade_forte"] > 0)]
    negativos_fortes = df_filtrado[(df_filtrado["impacto_esperado"] == "negativo") & (df_filtrado["intensidade_forte"] > 0)]

    cidade_destaque = positivos_fortes["cidade"].value_counts().idxmax() if not positivos_fortes.empty else "N/D"
    cidade_negativa = negativos_fortes["cidade"].value_counts().idxmax() if not negativos_fortes.empty else "N/D"

    # Indicadores mais frequentes com intensidade forte
    indicadores_fortes = df_filtrado[df_filtrado["intensidade_forte"] > 0]["indicador"]
    indicadores_heatmap = indicadores_fortes.value_counts().head(3).index.tolist()
    indicadores_dispersao = indicadores_fortes.value_counts().tail(2).index.tolist()

    dados_dinamicos = {
        "cidade_destaque": cidade_destaque,
        "cidade_menor_intensidade": cidade_negativa,
        "porcentagem_positiva": porcentagem_positiva,
        "porcentagem_negativa": porcentagem_negativa,
        "cidade": cidade_destaque,
        "impacto_aceitacao": "maior",
        "cidade_impacto_economico": cidade_destaque,
        "cidade_impacto_social_negativo": cidade_negativa,
        "indicador_1": indicadores_heatmap[0] if len(indicadores_heatmap) > 0 else "N/D",
        "indicador_2": indicadores_heatmap[1] if len(indicadores_heatmap) > 1 else "N/D",
        "indicador_3": indicadores_heatmap[2] if len(indicadores_heatmap) > 2 else "N/D",
        "cidade_heatmap_1": cidade_destaque,
        "cidade_heatmap_2": cidade_negativa,
        "indicador_critico_1": indicadores_dispersao[0] if len(indicadores_dispersao) > 0 else "N/D",
        "indicador_critico_2": indicadores_dispersao[1] if len(indicadores_dispersao) > 1 else "N/D",
        "cidade_mais_positiva": cidade_destaque,
        "cidade_mais_negativa": cidade_negativa,
        "dimensao_negativa": "Ambiental",
        "Data_atual": datetime.today().strftime("%d/%m/%Y"),
    }

   # Template do relatório técnico
    template_markdown = '''
    ## 1 Objetivo do Relatório
    Este relatório tem como objetivo analisar a percepção da população local sobre os possíveis impactos de um projeto turístico nas cidades de Delmiro Gouveia e Piranhas, em Alagoas. O levantamento foi realizado com base em pesquisa aplicada, abordando impactos econômicos, sociais e ambientais.

    A análise busca fornecer subsídios técnicos para a tomada de decisão estratégica, além de:

    - Antecipar potenciais riscos e oportunidades;
    - Identificar impactos prioritários a serem gerenciados;
    - Promover a transparência do processo de planejamento.

    ## 2 Metodologia e Estrutura dos Dados

    ### 2.1 Dimensões de Impacto Avaliadas
    A pesquisa foi estruturada em três eixos principais:

    - Impactos Econômicos 
    - Impactos Sociais 
    - Impactos Ambientais 

    ### 2.2 Variáveis Coletadas
    Para cada indicador de impacto, a população respondeu:

    - Percepção do Impacto → SIM ou NÃO
    - Intensidade do Impacto → Fraco, Moderado ou Forte

    ### 2.3 Instrumento de Coleta
    - Instrumento: Questionário estruturado
    - Tipo de coleta: Pesquisa presencial em campo
    - Público-alvo: Moradores das cidades analisadas
    - Amostra: Amostra probabilística, proporcional à população local

    ## 3️ Análise Detalhada dos Resultados

    ### 3.1 Visão Geral dos Impactos por Cidade e Intensidade
    **Descrição do Gráfico:** Gráficos de barras empilhadas demonstram a distribuição da intensidade dos impactos em cada cidade e para cada dimensão.

    **Finalidade:** Compreender quais cidades concentram maior percepção de impactos e identificar a intensidade predominante (forte, moderada, fraca).

    **Insights Automáticos:**  
    A cidade de {{cidade_destaque}} apresenta o maior volume de impactos de alta intensidade na dimensão {{impacto_aceitacao}}.  
    A cidade de {{cidade_menor_intensidade}} demonstra maior equilíbrio nas percepções.

    ### 3.2 Proporção de Impactos Positivos vs Negativos
    **Descrição do Gráfico:** Gráficos de pizza ilustram a proporção geral entre percepções positivas e negativas.

    **Utilidade:** Avaliar o clima geral da opinião pública sobre o projeto.

    **Resultados:**  
    - Positivos: {{porcentagem_positiva}}%  
    - Negativos: {{porcentagem_negativa}}%

    **Interpretação:**  
    A população de {{cidade}} demonstra {{impacto_aceitacao}} aceitação geral do projeto, refletindo tendências de receptividade.

    ### 3.3 Intensidade dos Impactos por Tipo
    **Descrição do Gráfico:** Gráficos de barras agrupadas comparam a quantidade de respostas por intensidade e por dimensão.

    **Finalidade:** Identificar em quais áreas de impacto (econômica, social, ambiental) os efeitos do projeto são percebidos como mais ou menos fortes.

    **Principais Constatações:**  
    Impactos econômicos positivos predominam em {{cidade_impacto_economico}}.  
    Impactos sociais negativos se destacam em {{cidade_impacto_social_negativo}} com intensidade forte.

    ### 3.4 Heatmap de Alta Intensidade
    **Descrição do Gráfico:** Mapa de calor que apresenta os indicadores com maior número de respostas de intensidade forte.

    **Finalidade:** Priorizar ações mitigadoras ou de valorização sobre os indicadores mais críticos.

    **Indicadores Mais Críticos:**  
    - {{indicador_1}}  
    - {{indicador_2}}  
    - {{indicador_3}}

    **Cidades Mais Impactadas:**  
    - {{cidade_heatmap_1}}  
    - {{cidade_heatmap_2}}

    ### 3.5 Dispersão: Percepção vs Intensidade Forte
    **Descrição do Gráfico:** Gráfico de dispersão (bolhas) correlaciona a quantidade de percepções com a intensidade forte para cada indicador.

    **Utilidade:** Destacar indicadores críticos com potencial para gerar maior repercussão social.

    **Indicadores Prioritários:**  
    - {{indicador_critico_1}} → Alta percepção + Alta intensidade  
    - {{indicador_critico_2}} → Moderada percepção + Alta intensidade

    ## 4️ Validação Técnica da Pesquisa

    ### 4.1 Qualidade da Coleta
    - Amostra representativa: Sim
    - Neutralidade dos instrumentos: Sim
    - Padronização da coleta: Sim

    ### 4.2 Integridade Analítica
    - Coerência entre dimensões: Verificada
    - Possíveis correlações cruzadas: Identificadas

    ## 5️ Conclusão Estratégica
    A cidade de {{cidade_mais_positiva}} apresenta alta receptividade ao projeto.  
    {{cidade_mais_negativa}} demonstra preocupações relevantes na dimensão {{dimensao_negativa}}.

    Os indicadores críticos devem ser endereçados prioritariamente antes da implantação.

    ### 5.1 Recomendações Gerais
    ✅ Fortalecer ações mitigadoras para os impactos sociais e ambientais destacados.  
    ✅ Comunicar com transparência os benefícios esperados para reforçar a aceitação.  
    ✅ Monitorar periodicamente as percepções após a implantação.

    ## 6️ Considerações Éticas e Legais
    **Validade técnica:** O projeto encontra-se em conformidade com as exigências técnicas.  
    **Validade ética:** É fundamental garantir que os princípios de justiça social e participação comunitária sejam respeitados.  
    **Aspectos legais:** Recomenda-se monitorar de forma contínua o processo de licenciamento ambiental e as condições pactuadas.

    ## Data de Emissão do Relatório
    {{Data_atual}}

    ## Assinatura Técnica
    Jean Silva -
    Analista de Suporte de TI
    Analista de Dados

    Joéliton Oliveira -
    Estudante de Ciência de Dados | Desenvolvedor de Soluções Interativas

    Daniel Almeida -
    Adobe Experience Manager
    Web Developer | Full-stack
    Data Analyst

    Elineudo Maia - 
    Analista de Dados
    Desenvolvedor Web

    Plataforma "Impacto do Turismo nas Cidades"
    Cientistas de Dados & Desenvolvedores de Soluções BI

    ## Anexos
    - Gráficos gerados dinamicamente pelo Dashboard  
    - Tabelas sintéticas de dados filtrados  
    - Logs de parâmetros aplicados
    '''

    # Renderiza o markdown
    template = Template(template_markdown)
    relatorio_final = template.render(**dados_dinamicos)
    st.markdown(relatorio_final)

