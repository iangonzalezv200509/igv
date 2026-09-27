import streamlit as st

# Configuración inicial de la página
st.set_page_config(
    page_title="Portafolio Profesional | Ian Gonzalez",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Estilos personalizados
css_custom = """
<style>
.main { padding-top: 1rem; }
.stProgress > div > div > div > div { background-color: #00ADB5; }
</style>
"""
st.markdown(css_custom, unsafe_allow_html=True)

# ---------------------------------------------------------
# SIDEBAR / MENÚ LATERAL
# ---------------------------------------------------------
with st.sidebar:
    st.title("👨‍💻 Ian González")
    st.caption("Backend Software Engineer")
    st.markdown("---")

    opcion = st.radio(
        "Navegación", ["Sobre mí", "Habilidades", "Proyectos", "Contacto"]
    )

    st.markdown("---")

    # Botón de descarga de CV
    try:
        with open("CV digital IGV.pdf", "rb") as file:
            st.download_button(
                label="📄 Descargar CV",
                data=file,
                file_name="CV digital IGV.pdf",
                mime="application/pdf",
                use_container_width=True,
            )
    except FileNotFoundError:
        st.caption("⚠️ No se encontró el archivo 'CV digital IGV.pdf'.")

# ---------------------------------------------------------
# SECCIÓN 1: SOBRE MÍ
# ---------------------------------------------------------
if opcion == "Sobre mí":
    st.header("Sobre Mí")
    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("Perfil")
        st.write(
            "Desarrollador enfocado en backend, desarrollo en Python, gestión de bases de datos SQL "
            "y arquitectura de software."
        )

    with col2:
        st.subheader("Métricas de Impacto")
        m1, m2 = st.columns(2)
        m1.metric(label="Proyectos Desplegados", value="5+")
        m2.metric(label="Lógica & Backend", value="Python / SQL")

# ---------------------------------------------------------
# SECCIÓN 2: HABILIDADES TÉCNICAS
# ---------------------------------------------------------
elif opcion == "Habilidades":
    st.header("Habilidades Técnicas")

    st.subheader("Lenguajes y Backend")
    st.write("Python")
    st.progress(85)

    st.write("SQL y Bases de Datos")
    st.progress(75)

    st.subheader("Herramientas y Entornos")
    st.write("Git / GitHub / VS Code / PowerShell")
    st.progress(80)

# ---------------------------------------------------------
# SECCIÓN 3: PROYECTOS CON FILTROS
# ---------------------------------------------------------
elif opcion == "Proyectos":
    st.header("Proyectos Destacados")

    proyectos = [
        {
            "nombre": "Diagnóstico de Servidores con IA",
            "categoria": "Backend / IA",
            "descripcion": "Análisis y diagnóstico automatizado de logs de servidores Apache y políticas SELinux.",
            "tecnologias": ["Python", "AI APIs"],
            "link": "https://github.com/iangonzalezv200509/igv",
        },
        {
            "nombre": "Aplicación Web de Análisis de Datos",
            "categoria": "Data / Streamlit",
            "descripcion": "Plataforma interactiva para procesamiento de datos utilizando Pandas y NumPy.",
            "tecnologias": ["Python", "Streamlit", "Pandas"],
            "link": "https://github.com/iangonzalezv200509/igv",
        },
    ]

    categorias = ["Todos", "Backend / IA", "Data / Streamlit"]
    filtro = st.selectbox("Filtrar por categoría:", categorias)

    st.markdown("---")

    for p in proyectos:
        if filtro == "Todos" or p["categoria"] == filtro:
            with st.expander(f"📌 {p['nombre']} - *{p['categoria']}*"):
                st.write(p["descripcion"])
                st.write(f"**Tecnologías:** {', '.join(p['tecnologias'])}")
                st.markdown(f"[Ver Repositorio]({p['link']})")

# ---------------------------------------------------------
# SECCIÓN 4: FORMULARIO DE CONTACTO
# ---------------------------------------------------------
elif opcion == "Contacto":
    st.header("Contacto Directo")

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
