@echo off
setlocal

:: Vai para a pasta onde este .bat está
cd /d "%~dp0"

:: Verifica se o ambiente virtual ja existe
if not exist "venv\" (
    echo Ambiente virtual nao encontrado. Criando...

    :: Cria o ambiente virtual
    python -m venv venv
    if errorlevel 1 (
        echo Erro ao criar o ambiente virtual. Abortando.
        exit /b 1
    )

    :: Ativa o ambiente e instala as dependencias
    call venv\Scripts\activate
    if exist requirements.txt (
        echo Instalando dependencias...
        pip install -r requirements.txt
    ) else (
        echo Arquivo requirements.txt nao encontrado!
    )
) else (
    echo Ambiente virtual encontrado.
    call venv\Scripts\activate
)

:: Executa o Streamlit
start "" streamlit run main.py

exit
