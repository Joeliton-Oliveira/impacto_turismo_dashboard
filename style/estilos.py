import streamlit as st

def aplicar_estilo():
    """
    Aplica o tema institucional Embrapa em tons de verde claro, azul e laranja acessíveis,
    com consistência visual para toda a interface Streamlit.
    """
    st.markdown("""
        <style>
            /* Fonte Inter (peso 400, 600, 700) */
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

            html, body, [class*="css"] {
                font-family: 'Inter', sans-serif;
                font-size: 14px;
                background-color: #E6F4EA;
                color: #003399;
            }

            /* Fundo da App */
            .stApp {
                background-color: #E6F4EA;
                color: #003399;
            }

            /* Container principal */
            .block-container {
                padding: 1rem 2rem;
                background-color: #E6F4EA;
            }

            /* Barra lateral */
            section[data-testid="stSidebar"] {
                background-color: #F1FBF5 !important;
            }

            /* Barra superior (Deploy) */
            header[data-testid="stHeader"] {
                background-color: #F1FBF5 !important;
            }

            /* Títulos */
            h1, h2, h3, h4 {
                font-weight: 700;
                color: #003399;
                border-bottom: 1px solid #B6E3C5;
                padding-bottom: 0.4rem;
                margin-top: 1.5rem;
            }

            /* Botões */
            .stButton > button {
                background-color: #009933;
                color: white;
                border-radius: 10px;
                font-weight: bold;
                transition: 0.2s ease-in-out;
            }

            .stButton > button:hover {
                background-color: #007722;
                color: #ffffff;
            }

            .stButton > button:active {
                background-color: #00661a;
                border-color: #004d13;
            }

            /* Estilo de métricas */
            div[data-testid="stMetric"] {
                background-color: #F5F5F5;
                padding: 10px;
                border: 1px solid #D0D0D0;
                border-radius: 8px;
                color: #003399;
            }

            /* Texto da sidebar */
            .css-1d391kg, .css-18e3th9 {
                color: #003399 !important;
            }
        </style>
    """, unsafe_allow_html=True)
