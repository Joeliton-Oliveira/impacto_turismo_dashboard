# components/layout.py

import streamlit as st
import base64

def imagem_para_base64(caminho_arquivo: str) -> str:
    """
    Converte a imagem da logo para base64 para renderização inline no Streamlit.

    Args:
        caminho_arquivo (str): Caminho do arquivo da imagem.

    Returns:
        str: String codificada em base64.
    """
    with open(caminho_arquivo, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

def exibir_cabecalho(caminho_logo="assets/logo_embrapa.png", largura=300):
    """
    Exibe a logo centralizada com animação e o título do dashboard.

    Args:
        caminho_logo (str): Caminho para o arquivo da logo.
        largura (int): Largura da imagem em pixels.
    """
    tipo_arquivo = "gif" if caminho_logo.endswith(".gif") else "png"
    logo_base64 = imagem_para_base64(caminho_logo)

    st.markdown(
        f"""
        <div style="display: flex; justify-content: center; align-items: center; height: 200px; margin-top: -10px; margin-bottom: 20px;">
        <img src="data:image/{tipo_arquivo};base64,{logo_base64}" width="{largura}">
        </div>
        """,
        unsafe_allow_html=True
    )
    

    st.title("Impacto do Turismo nas Cidades")