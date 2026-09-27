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
   st.set_page_config(
    page_title="Portafolio Profesional",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
    
    css_custom = """
<style>
.main { padding-top: 1rem; }
.stProgress > div > div > div > div { background-color: #00ADB5; }
</style>
"""
st.markdown(css_custom, unsafe_allow_html=True)
    
    try: 
        with open("cv.pfd", "rb") as file:
            st.download_button(label="📄Descargar CV", data=file, file_name="CV digital IGV", mime="aplicattion/pdf", use_container_width=True)
        except FileNotFoundError:
            st.caption("⚠️ Sube tu `cv.pdf` al directorio raíz para habilitar la descarga.")
            
if opcion == "Sobre mi":
    st.header("Sobre mi")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Perfil")
        st.write("Desarrollador enfocado en backend, arquitectura de software y desarrollo de herramientas de diagnóstico e integración de APIs.")
        
        with col2:
            st.subheader("Metricas de impacto")
            m1, m2 = st.columns(2)
            m1.metric(label="Proyectos desplegados", value="5+")
            m2.metric(label="Lógica y Backend", value="Phyton / SQL")
            
elif == opcion "Habilidades":
    st.header("Habilidades tecnicas")
    
    st.subheader("Lenguajes y Backend")
    st.write("Phyton")
    st.progress(85)
    
    st.write("SQL Y Bases de Datos")
    st.progress(75)
    
    st.subheader("Herramientas y Entornos")
    st.write("Git / Github / VSCode / PowerShell")
    st.progress(80)
    
elif opcion == "Proyectos":
    st.header("Proyectos destacados")
    proyectos = 
    [{"nombre": "Diagnóstico de Servidores con IA",
            "categoria": "Backend / IA",
            "descripcion": "Análisis y diagnóstico automatizado de logs de servidores Apache y políticas SELinux.",
            "tecnologias": ["Python", "AI APIs"],
            "link": "https://github.com/iangonzalezv200509/igv"} , {"nombre": "Aplicación Web de Análisis de Datos",
            "categoria": "Data / Streamlit",
            "descripcion": "Plataforma interactiva para procesamiento de datos utilizando Pandas y NumPy.",
            "tecnologias": ["Python", "Streamlit", "Pandas"],
            "link": "https://github.com/iangonzalezv200509/igv"}]
    
    categorias = ["Todos", "Backend / IA", "Data / Streamlit"]
    filtro = st.selectbox("Filtrar por categoria:", categorias)
    
    st.markdown("---")
    
    for p in Proyectos:
        if filtro == "Todos" or p["categoria"] == filtro:
            with st.expander(f"📌 {p['nombre']} - *{p['categoria']}*"):
                st.write(p["descripcion"])
                st.write(f"**Tecnologías:** {', '.join(p['tecnologias'])}")
                st.markdown(f"[Ver Repositorio]({p['link']})")
                
elif opcion == "Contacto":
    st.header("Contacto directo")
    
    with st.form("form_contacto"):
        nombre = st.text_input("Nombre completo")
        email = st.text_input("Correo electrónico")
        mensaje = st.text_area("Mensaje")
        
        enviado = st.form_submit_button("Enviar Mensaje")
        if enviado:
            if nombre and email and mensaje:
                st.success("¡Gracias por contactarme! Te responderé a la brevedad.")
            else:
                st.warning("Por favor, completa todos los campos del formulario.")
                