from pathlib import Path
import streamlit as st

# ---------------------------------------------------------
# 1. CONFIGURACIÓN INICIAL DE LA PÁGINA
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ian González | Backend Developer Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------
# 2. ESTILOS CSS PERSONALIZADOS (Diseño Moderno)
# ---------------------------------------------------------
st.markdown(
    """
    <style>
    /* Fondo principal y fuentes */
    .stApp {
        background-color: #0E1117;
    }
    
    /* Títulos y Subtítulos con degradado */
    .gradient-header {
        font-weight: 800;
        background: linear-gradient(90deg, #00ADB5 0%, #393E46 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }

    /* Tarjetas de Métricas Personalizadas */
    .metric-card {
        background-color: #1E232A;
        border: 1px solid #30363D;
        border-radius: 10px;
        padding: 1.2rem;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Badges de Tecnologías */
    .tech-badge {
        display: inline-block;
        background-color: #262730;
        color: #00ADB5;
        border: 1px solid #00ADB5;
        border-radius: 15px;
        padding: 3px 10px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-right: 5px;
        margin-top: 5px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# 3. DATOS DE PROYECTOS (Lógica de Datos Decoupled)
# ---------------------------------------------------------
PROYECTOS = [
    {
        "nombre": "AI-Powered Server Diagnostics",
        "categoria": "Backend / IA",
        "descripcion": "Análisis automatizado y diagnóstico de logs de servidores Apache y políticas SELinux mediante inteligencia artificial.",
        "tecnologias": ["Python", "AI APIs", "Linux", "Log Parsing"],
        "link": "https://github.com/iangonzalezv200509/igv",
        "destacado": True,
    },
    {
        "nombre": "Data Analytics Interactive Platform",
        "categoria": "Data / Analytics",
        "descripcion": "Plataforma web interactiva para procesamiento de estructuras de datos masivas y métricas estadísticas en tiempo real.",
        "tecnologias": ["Python", "Streamlit", "Pandas", "NumPy"],
        "link": "https://github.com/iangonzalezv200509/igv",
        "destacado": False,
    },
]

# ---------------------------------------------------------
# 4. BARRA LATERAL (Sidebar & Branding)
# ---------------------------------------------------------
with st.sidebar:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=90
    )
    st.title("Ian González")
    st.caption("🚀 Junior Backend Software Engineer")
    st.write("📍 Argentina")

    st.markdown("---")

    seccion = st.radio(
        "Navegación del sitio:",
        [
            "🏠 Sobre Mí",
            "🛠️ Habilidades Técnicas",
            "📂 Proyectos",
            "📬 Contacto",
        ],
    )

    st.markdown("---")

    # Gestión de descarga de CV con Pathlib
    cv_path = Path("CV digital IGV.pdf")
    if cv_path.exists():
        with open(cv_path, "rb") as pdf_file:
            st.download_button(
                label="📄 Descargar CV Profesional",
                data=pdf_file,
                file_name="CV_Ian_Gonzalez_Backend.pdf",
                mime="application/pdf",
                use_container_width=True,
            )
    else:
        st.warning("⚠️ Archivo 'CV digital IGV.pdf' no encontrado.")

# ---------------------------------------------------------
# 5. SECCIÓN 1: SOBRE MÍ
# ---------------------------------------------------------
if seccion == "🏠 Sobre Mí":
    st.markdown(
        "<h1 class='gradient-header'>Ian González</h1>", unsafe_allow_html=True
    )
    st.subheader("Backend Software Engineer & Problem Solver")

    col_perfil, col_metrics = st.columns([2, 1], gap="large")

    with col_perfil:
        st.markdown("""
        Desarrollador de software enfocado en **arquitectura backend**, desarrollo en **Python**, y gestión eficiente de **bases de datos SQL**. 
        
        Apasionado por la optimización de código, automatización de procesos y el diagnóstico de infraestructura de servidores. Experiencia práctica construyendo herramientas interactivas, integración de APIs y gestión de entornos virtuales en entornos de desarrollo modernos (`Git`, `VS Code`, `PowerShell`).
        """)

        st.markdown("### 🎯 Objetivos Clave")
        st.markdown("""
        - 🔹 Diseñar e implementar APIs RESTful escalables y robustas.
        - 🔹 Optimizar consultas a bases de datos relacionales.
        - 🔹 Continuar integrando servicios de Inteligencia Artificial al diagnóstico de software.
        """)

    with col_metrics:
        st.markdown("### Métricas de Impacto")

        st.markdown(
            """
        <div class='metric-card'>
            <h2 style='color:#00ADB5; margin:0;'>5+</h2>
            <p style='margin:0; font-size:0.9rem;'>Proyectos Desarrollados</p>
        </div>
        <br>
        <div class='metric-card'>
            <h2 style='color:#00ADB5; margin:0;'>100%</h2>
            <p style='margin:0; font-size:0.9rem;'>Código Modular en Python</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

# ---------------------------------------------------------
# 6. SECCIÓN 2: HABILIDADES TÉCNICAS
# ---------------------------------------------------------
elif seccion == "🛠️ Habilidades Técnicas":
    st.markdown(
        "<h1 class='gradient-header'>Habilidades Técnicas</h1>",
        unsafe_allow_html=True,
    )
    st.write(
        "Herramientas y tecnologías que utilizo para la construcción de software backend:"
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.subheader("Core Backend & Lenguajes")

        st.write("**Python 3 (Avanzado)**")
        st.progress(85)
        st.caption(
            "Estructuras de datos, POO, Manejo de excepciones, Modularización."
        )

        st.write("**SQL & Bases de Datos Relacionales**")
        st.progress(75)
        st.caption(
            "Consultas complejas, diseño de esquemas, relaciones y filtrado."
        )

        st.write("**Data Analysis (Pandas / NumPy)**")
        st.progress(70)
        st.caption("Manipulación, limpieza y estructuración de sets de datos.")

    with col2:
        st.subheader("Herramientas & Entornos")

        st.write("**Control de Versiones (Git & GitHub)**")
        st.progress(85)
        st.caption("Flujos de trabajo con ramas, merges y despliegues remotos.")

        st.write("**Entornos de Desarrollo (VS Code / Virtualenv)**")
        st.progress(90)
        st.caption("Configuración de virtual environments, pip, PowerShell.")

        st.write("**Diagnóstico & Servidores (Linux / Apache)**")
        st.progress(65)
        st.caption("Análisis de logs de servidor y permisos/políticas SELinux.")

# ---------------------------------------------------------
# 7. SECCIÓN 3: PROYECTOS DESTACADOS
# ---------------------------------------------------------
elif seccion == "📂 Proyectos":
    st.markdown(
        "<h1 class='gradient-header'>Proyectos Destacados</h1>",
        unsafe_allow_html=True,
    )
    st.write(
        "Explora los desarrollos y casos de estudio que he publicado e implementado:"
    )

    # Filtros
    categorias = ["Todos", "Backend / IA", "Data / Analytics"]
    cat_seleccionada = st.pills(
        "Filtrar por categoría:", categorias, default="Todos"
    )

    st.markdown("---")

    # Renderizado de Tarjetas de Proyectos
    for p in PROYECTOS:
        if cat_seleccionada == "Todos" or p["categoria"] == cat_seleccionada:
            with st.container(border=True):
                col_info, col_link = st.columns([3, 1])

                with col_info:
                    st.subheader(p["nombre"])
                    st.write(p["descripcion"])

                    # Render de badges
                    badges_html = "".join(
                        [
                            f"<span class='tech-badge'>{tech}</span>"
                            for tech in p["tecnologias"]
                        ]
                    )
                    st.markdown(badges_html, unsafe_allow_html=True)

                with col_link:
                    st.write("")
                    st.write("")
                    st.link_button("🔗 Ver Código / Repo", p["link"])

# ---------------------------------------------------------
# 8. SECCIÓN 4: FORMULARIO DE CONTACTO
# ---------------------------------------------------------
elif seccion == "📬 Contacto":
    st.markdown(
        "<h1 class='gradient-header'>Contacto Directo</h1>",
        unsafe_allow_html=True,
    )
    st.write(
        "¿Tienes una propuesta laboral o consulta técnica? Envíame un mensaje directo:"
    )

    col_form, col_info = st.columns([2, 1], gap="large")

    with col_form:
        with st.form("form_contacto_profesional", clear_on_submit=True):
            nombre = st.text_input("Nombre completo")
            email = st.text_input("Correo electrónico")
            mensaje = st.text_area("Mensaje o Consulta", height=120)

            submitted = st.form_submit_button(
                "🚀 Enviar Mensaje", use_container_width=True
            )

            if submitted:
                if nombre and email and mensaje:
                    if "@" in email and "." in email:
                        st.toast("¡Mensaje enviado con éxito!", icon="✅")
                        st.success(
                            f"Gracias {nombre}, he recibido tu mensaje. Me pondré en contacto contigo a través de {email} a la brevedad."
                        )
                    else:
                        st.error(
                            "Por favor, ingresa un correo electrónico válido."
                        )
                else:
                    st.warning(
                        "Por favor, completa todos los campos requeridos antes de enviar."
                    )

    with col_info:
        st.subheader("Información de Contacto")
        st.write("📂 **GitHub:** [github.com/iangonzalezv200509](https://github.com/iangonzalezv200509)")
        st.write("💼 **Especialidad:** Backend Software Development")
        st.write("🌍 **Ubicación:** Argentina")