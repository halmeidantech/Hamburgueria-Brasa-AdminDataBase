import streamlit as st
from src.db import consultar

# st.title("Painel Brasa & Pão!")
# st.write("Nosso painel irá nascer a partir daqui")

# st.dataframe(consultar("SELECT * FROM Produtos"))

st.set_page_config(page_title="Brasa & Pão - Painel SQL", layout="wide")

st.navigation([
    st.Page("paginas/inicio.py", title="inicio", default=True),
    st.Page("paginas/nivel_1.py", title="Nivel 1 - Aquecimento"),
    st.Page("paginas/nivel_2.py", title="Nivel 2 - Join"),
    st.Page("paginas/nivel_3.py", title="Nivel 3 - Desafio")
]).run()