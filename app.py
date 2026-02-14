import streamlit as st
import random
import matplotlib.pyplot as plt

st.set_page_config(page_title="LotoLab PRO")

st.title("🧬 LotoLab PRO - Rafael")

modalidade = st.selectbox("Escolha a modalidade:", ["Mega-Sena", "Lotofácil"])

if modalidade == "Mega-Sena":
    LIMITE = 60
    TAMANHO = 6
else:
    LIMITE = 25
    TAMANHO = 15

def gerar_jogo():
    return sorted(random.sample(range(1, LIMITE+1), TAMANHO))

if st.button("🚀 Gerar Jogos Inteligentes"):
    jogos = [gerar_jogo() for _ in range(5)]

    st.subheader("🎯 Jogos Gerados:")
    for j in jogos:
        st.write(j)

    numeros = []
    for j in jogos:
        numeros.extend(j)

    fig = plt.figure()
    plt.hist(numeros)
    st.pyplot(fig)
