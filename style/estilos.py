# style/estilos.py

import streamlit as st

def aplicar_estilo():
    """
    Aplica o tema visual escuro e personalizado ao Streamlit, com animação e fontes.
    Essa função deve ser chamada logo após a configuração inicial da página.
    """
    st.markdown("""
        <style>
            /* Fonte Inter (peso 400, 600, 700) */
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

            /* Base */
            html, body, [class*="css"] {
                font-family: 'Inter', sans-serif;
                font-size: 14px;
                background-color: #0f172a;
                color: #f8fafc;
            }

            h1, h2, h3 {
                font-weight: 700;
                border-bottom: 1px solid #334155;
                padding-bottom: 0.4rem;
                margin-top: 1.5rem;
            }

            .stApp {
                background-color: #0f172a;
                color: #f8fafc;
            }

            /* Animação de logo */
            @keyframes bounce {
                0%   { transform: translateY(0); }
                50%  { transform: translateY(-10px); }
                100% { transform: translateY(0); }
            }

            /* Botões e selects */
            .stButton > button, .stMultiSelect > div {
                background-color: #1e293b;
                color: #f8fafc;
                border: 1px solid #334155;
                border-radius: 6px;
                transition: 0.2s ease-in-out;
            }

            .stButton > button:hover {
                background-color: #334155;
                color: #ffffff;
                border-color: #475569;
            }

            .stButton > button:active {
                background-color: #0f172a;
                border-color: #1e293b;
            }
        </style>
    """, unsafe_allow_html=True)
