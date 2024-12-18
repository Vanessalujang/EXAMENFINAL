# -*- coding: utf-8 -*-
"""EXAMEN FINAL.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JjISgrsvKo_7aS8iwPEqMNk2_F-GgfZN

##TRABAJO FINAL VALOR VPN

##Vanessa Lujan
##Alison Mazo
#Susana Cano
"""

#pip install streamlit

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configuración del título
st.title("Cálculo del Valor Presente Neto (VPN)")

# Entradas de usuario en el sidebar
with st.sidebar:
    st.header("Datos de entrada")
    inversion_inicial = st.number_input("Inversión inicial:", value=-10000.0)  # Inversión inicial
    tasa_descuento = st.slider("Tasa de descuento (%)", min_value=0.0, max_value=20.0, value=8.0) / 100  # Tasa de descuento (8%)
    años = st.number_input("Número de años:", min_value=1, max_value=10, value=5)  # Número de años

    # Entrada de flujos de caja (valores fijos para el ejemplo)
    flujos = []
    for i in range(int(años)):
        flujo = st.number_input(f"Flujo de caja para el año {i+1}:", value=2000.0)
        flujos.append(flujo)

# Cálculo del VPN
vpn = inversion_inicial + sum([flujos[i] / (1 + tasa_descuento)**(i + 1) for i in range(len(flujos))])
st.write(f"**Valor Presente Neto (VPN):** ${vpn:,.2f}")

# Gráfico de flujos de caja
st.subheader("Visualización de Flujos de Caja")
fig, ax = plt.subplots()
ax.bar(range(1, int(años) + 1), flujos, color="blue")
ax.set_xlabel("Años")
ax.set_ylabel("Flujo de Caja")
st.pyplot(fig)
