# 📦 Importação de bibliotecas
import pandas as pd
import numpy as np
import unicodedata
import gdown
import re

# Configurações para visualização
pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)

# Função para normalizar textos para snake_case
def normalizar_texto(texto):
    if isinstance(texto, str):
        texto = texto.strip().lower()
        texto = unicodedata.normalize('NFKD', texto)
        texto = texto.encode('ASCII', 'ignore').decode('utf-8')
        texto = re.sub(r'\s+', '_', texto)
        return texto
    return texto

# Função para capitalizar nome de cidade mantendo letras minúsculas restantes
def capitalizar_cidade(cidade):
    if isinstance(cidade, str):
        cidade = cidade.strip().lower()
        return cidade.capitalize()
    return cidade

# Função para identificar posições dos blocos em uma aba
chaves_blocos = {
    'economico': 'impactos econômicos',
    'social': 'impactos sociais',
    'ambiental': 'impactos ambientais'
}

def detectar_blocos(df):
    linha_referencia = df.iloc[2].fillna("")
    posicoes = {}

    for tipo, chave in chaves_blocos.items():
        for i, valor in enumerate(linha_referencia):
            if isinstance(valor, str) and chave in valor.lower():
                posicoes[tipo] = i
                break

    return posicoes

# Função para extrair e transpor blocos horizontalizados em tidy data
def extrair_bloco_tidy(df, posicao_inicio, tipo_impacto, nome_cidade):
    df_dados = df.iloc[10:].copy()
    df_dados.reset_index(drop=True, inplace=True)

    colunas_bloco = df.columns[posicao_inicio:posicao_inicio + 16]
    bloco = df_dados[colunas_bloco].copy()
    bloco.columns = range(bloco.shape[1])

    dados_formatados = []

    for i in range(0, bloco.shape[1], 8):
        sub = bloco.iloc[:, i:i+8]
        if sub.shape[1] < 7:
            continue

        colunas_tidy = [
            'indicador',
            'percepcao_positiva',
            'percepcao_negativa',
            'intensidade_fraco',
            'intensidade_moderado',
            'intensidade_forte',
            'descartar1', 'descartar2'
        ][:sub.shape[1]]

        sub.columns = colunas_tidy
        sub = sub.drop(columns=[c for c in sub.columns if "descartar" in c])
        sub = sub.dropna(how='all')

        sub['tipo_impacto'] = tipo_impacto.strip().capitalize()
        sub['cidade'] = capitalizar_cidade(nome_cidade)
        sub['impacto_esperado'] = 'Positivo' if i == 0 else 'Negativo'

        dados_formatados.append(sub)

    return pd.concat(dados_formatados, ignore_index=True) if dados_formatados else pd.DataFrame()

# 🧹 Função de limpeza e padronização final
def limpar_e_padronizar(df):
    df = df.copy()
    df = df[df['indicador'].notna()]

    padroes_invalidos = [
        "TOTAL DAS 3 DIMENSÕES", "TOTAL DAS 3 DIMENSOES", "IMPACTOS POSITIVOS",
        "IMPACTOS NEGATIVOS", "SIM", "NÃO", "NAO", "TOTAL", "TOTAL GERAL", "INDICADOR", "nan"
    ]
    df['indicador'] = df['indicador'].astype(str).str.strip()
    df = df[~df['indicador'].str.upper().apply(lambda x: any(p in x for p in padroes_invalidos))]
    df = df[~df['indicador'].str.fullmatch(r'\d+')]

    df['cidade'] = df['cidade'].apply(capitalizar_cidade)
    df['cidade'] = df['cidade'].replace({
        "amas": "Amas", "ecqes2": "Ecqes2", "acqes2": "Ecqes2", "Acqes2": "Ecqes2",
        "pontal": "Pontal", "terra caída": "Terra Caida", "Terra caida": "Terra Caida",
        "terra caida": "Terra Caida", "pov preguiça": "Povpreguiça", "pov.preguiça": "Povpreguiça",
        "preguiça": "Povpreguiça", "Consolidado pov.preguiça": "Povpreguiça",
        "São cristóvão": "São Cristóvão", "sao cristovao": "São Cristóvão",
        "delmiro": "Delmiro", "piranhas": "Piranhas"
    })

    df['tipo_impacto'] = df['tipo_impacto'].str.lower().replace({
        "economico": "Econômico", "ambiental": "Ambiental", "social": "Social"
    })

    df['impacto_esperado'] = df['impacto_esperado'].str.lower().replace({
        "positivo": "Positivo", "negativo": "Negativo"
    })

    colunas_numericas = ['percepcao_positiva', 'percepcao_negativa',
                         'intensidade_fraco', 'intensidade_moderado', 'intensidade_forte']
    for col in colunas_numericas:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    colunas_finais = [
        'cidade', 'tipo_impacto', 'impacto_esperado', 'indicador',
        'percepcao_positiva', 'percepcao_negativa',
        'intensidade_fraco', 'intensidade_moderado', 'intensidade_forte'
    ]
    df = df[colunas_finais]
    df = df.drop_duplicates()
    df = df.dropna(how='all', subset=colunas_numericas)

    return df

# 🚀 Função principal para atualizar os dados
def atualizar_dados():
    print("🔄 Iniciando atualização dos dados...")

    file_id = "1siB_W8YSXP8G0Y9BCuPoNoE7GcRtrTNr"
    url = f"https://drive.google.com/uc?id={file_id}"
    caminho_arquivo = "Indicadoresv18_piranhas_e_delmiro.xlsx"

    gdown.download(url, caminho_arquivo, quiet=False)
    abas_dict = pd.read_excel(caminho_arquivo, sheet_name=None)

    dfs_formatados = []

    for nome_aba, df in abas_dict.items():
        if "consolidado" not in nome_aba.lower():
            continue

        nome_limpo = nome_aba.strip().lower().replace("consolidado", "").replace(".", "").strip()
        nome_limpo = re.sub(r'\s+', ' ', nome_limpo)  # ✅ CORREÇÃO do warning (usar raw string)
        cidade = capitalizar_cidade(nome_limpo)

        posicoes_blocos = detectar_blocos(df)

        blocos = []
        for tipo, posicao in posicoes_blocos.items():
            bloco_tidificado = extrair_bloco_tidy(df, posicao, tipo, cidade)
            blocos.append(bloco_tidificado)

        df_cidade = pd.concat(blocos, ignore_index=True)
        dfs_formatados.append(df_cidade)

    df_geral = pd.concat(dfs_formatados, ignore_index=True)
    df_limpo = limpar_e_padronizar(df_geral)

    # ✅ CORRIGIDO → salvar SEM subpasta (evita o seu OSError)
    caminho_saida = "dados_organizados_embrapa.xlsx"
    df_limpo.to_excel(caminho_saida, index=False)

    print(f"✅ Dados atualizados e salvos em {caminho_saida}")
