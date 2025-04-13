
import streamlit as st
import pandas as pd

# Cargar la estrategia completa desde archivo Excel
@st.cache_data
def cargar_datos():
    return pd.read_excel("Estrategia_Torneos_Slowplay_OOP.xlsx")

# Interfaz principal
def main():
    st.title("Guía Rápida de Estrategia Postflop - Torneos")

    df = cargar_datos()

    # Filtros
    tipo_mano = st.selectbox("Tipo de Mano", sorted(df["Tipo de Mano"].unique()))
    textura_board = st.selectbox("Textura del Board", sorted(df["Textura del Board"].unique()))
    situacion_preflop = st.selectbox("Situación Preflop", sorted(df["Situación Preflop"].unique()))
    posicion_hero = st.selectbox("Tu Posición", sorted(df["Posición del Hero"].unique()))
    posicion_villano = st.selectbox("Posición del Villano", sorted(df["Posición del Villano"].unique()))
    tipo_rival = st.selectbox("Tipo de Rival", sorted(df["Tipo de Rival"].unique()))

    # Filtro de DataFrame
    resultado = df[
        (df["Tipo de Mano"] == tipo_mano) &
        (df["Textura del Board"] == textura_board) &
        (df["Situación Preflop"] == situacion_preflop) &
        (df["Posición del Hero"] == posicion_hero) &
        (df["Posición del Villano"] == posicion_villano) &
        (df["Tipo de Rival"] == tipo_rival)
    ]

    if not resultado.empty:
        st.subheader("📋 Estrategia Recomendada")
        st.write("**Equity Aproximada:**", resultado.iloc[0]["Equity Aproximada"])
        st.write("**Rango del Rival:**", resultado.iloc[0]["Rango Estimado Rival"])
        st.write("**Rango de Defensa Preflop:**", resultado.iloc[0]["Rango Defensa Preflop"])
        st.write("**Acción en Flop:**", resultado.iloc[0]["Acción Flop"])
        st.write("**Acción en Turn:**", resultado.iloc[0]["Acción Turn"])
        st.write("**Acción en River:**", resultado.iloc[0]["Acción River"])
        st.write("**Si el Villano Resube:**", resultado.iloc[0]["Si Villano Resube"])
        st.write("**Sizing recomendado:**", resultado.iloc[0]["Sizing si Resubes"])
        st.write("**Contra Slowplay:**", resultado.iloc[0]["Contra Slowplay"])
        st.write("**Estrategia OOP:**", resultado.iloc[0]["Estrategia OOP"])
        st.write("**Consejo Multiway:**", resultado.iloc[0]["Consejo Multiway"])
    else:
        st.warning("No se encontró una coincidencia exacta. Prueba con otra combinación.")

if __name__ == "__main__":
    main()
