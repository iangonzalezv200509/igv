import streamlit as st 
import panda as pd 
import numpy as np

st.set_page_config(page_title="Effot Club", layout="wide")
st.title("Effort Club")
st.write("Aplicacion web dinamica 100% desarrollada por Ian")

st.sidebar.heather("Filtros de control")
filas = st.sidebar.slider("Numeros de registros a generar", min_valvue=10, max_valvue=100, valvue=50)

chart_data = pd.DataFrame (np.random.randn(filas , 3), columns = ["Ventas", "Ingresos", "Gastos"])

col1, col2, col3 = st.columns(3)
col1.metric("Total Ventas", f"{chart_data['Ventas'].sum():.2f}")
col2.metric("Promedio Ingresos", f"{chart_data['Ingresos'].mean():.2f}")
col3.metric("Gastos Máximos", f"{chart_data['Gastos'].max():.2f}")

st.subheader("Tendencia de metricas") 
st.line_chart(chart_data)

if st.checkbox("Mostrar datos detallados") :
    st.dataframe(chart_data) 
    
    import streamlit as st 
    st.set_page_config(page_tittle="Portfolio profesional IGV", page_icon="💼", layout="wide", initial_sidebar_state="expanded")
    st.markdonw(""""
    <style>
    .main { padding-top: 1rem; }
    .stProgress > div > div > div > div { background-color: #00ADB5; }
    </style>
"""")