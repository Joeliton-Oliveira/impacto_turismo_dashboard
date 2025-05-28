import streamlit as st
import base64

# Caminho da imagem
imagem_path = "assets/embrapa.jpeg"

# Converte a imagem para base64
with open(imagem_path, "rb") as image_file:
    imagem_base64 = base64.b64encode(image_file.read()).decode()

# CSS para fundo com imagem em base64 e sem esconder a sidebar
st.markdown(
    f"""
    <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{imagem_base64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .block-container {{
            padding: 0 !important;
            margin: 0 !important;
        }}
        header, footer {{
            display: none !important;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Mantém a altura da tela
st.markdown("<div style='height:100vh'></div>", unsafe_allow_html=True)
