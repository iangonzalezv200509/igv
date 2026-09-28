import streamlit as st

# 1. Configuración de la página
st.set_page_config(
    page_title="Ian González Viña - Backend Software Engineer",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Estilos CSS adaptados a tonos claros y verdes con bordes redondeados
st.markdown("""
    <style>
    /* Fondo general claro */
    .stApp {
        background-color: #FAF8F5;
        color: #111827;
        font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
    }
    
    /* Fondo e Integración del Sidebar */
    [data-testid="stSidebar"] {
        background-color: #F3EFEA;
        border-right: 1px solid #E2DCD5;
    }
    
    .profile-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        margin-bottom: 20px;
    }

    .profile-title {
        font-size: 1.35rem !important;
        font-weight: 700 !important;
        color: #111827 !important;
        width: 100%;
        text-align: center;
        margin-bottom: 15px;
    }

    .profile-name {
        font-size: 1.35rem !important;
        font-weight: 700 !important;
        color: #111827 !important;
        margin-top: 14px;
        margin-bottom: 2px;
    }

    .profile-role {
        font-size: 1.05rem !important;
        font-weight: 600 !important;
        color: #059669 !important;
        margin-bottom: 4px;
    }

    .profile-location {
        font-size: 1rem !important;
        color: #4B5563 !important;
    }

    /* Encabezado Principal Arriba de Todo */
    .main-header {
        font-size: 3.2rem;
        font-weight: 800;
        color: #111827;
        letter-spacing: -0.5px;
        margin-top: 0px;
        margin-bottom: 0px;
        line-height: 1.1;
    }
    
    .sub-header {
        font-size: 1.4rem;
        font-weight: 600;
        color: #059669;
        margin-bottom: 20px;
    }

    /* Rediseño de pestañas con bordes completamente redondeados */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: #EFEAE4;
        padding: 8px;
        border-radius: 30px !important;
        border: 1px solid #E2DCD5;
        margin-bottom: 25px;
    }

    .stTabs [data-baseweb="tab"] {
        height: 44px;
        background-color: transparent !important;
        border: none !important;
        border-radius: 20px !important;
        color: #1F2937 !important;
        font-size: 1.05rem !important;
        font-weight: 700 !important;
        padding: 0px 22px !important;
        transition: all 0.2s ease;
    }

    .stTabs [aria-selected="true"] {
        background-color: #10B981 !important;
        color: #FFFFFF !important;
        border-radius: 20px !important;
        box-shadow: 0 4px 10px rgba(16, 185, 129, 0.25) !important;
    }

    /* Píldoras de código */
    code {
        background-color: #ECFDF5 !important;
        color: #065F46 !important;
        border: 1px solid #A7F3D0 !important;
        padding: 3px 8px !important;
        border-radius: 6px !important;
        font-weight: 600 !important;
    }

    p, li, span {
        font-size: 1.15rem !important;
        color: #1F2937 !important;
        line-height: 1.6;
    }

    h4 {
        font-size: 1.5rem !important;
        font-weight: 700 !important;
        color: #111827 !important;
    }

    /* Tarjetas de métricas */
    .metric-card {
        background-color: #FFFFFF;
        border: 1px solid #E5E7EB;
        border-left: 5px solid #10B981;
        border-radius: 12px;
        padding: 22px;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.03);
    }
    
    .metric-value {
        font-size: 2.8rem;
        font-weight: 800;
        color: #059669;
    }
    
    .metric-label {
        font-size: 1.05rem;
        color: #374151;
        margin-top: 5px;
        font-weight: 600;
    }
    
    /* Botón de descarga de CV */
    .stDownloadButton > button {
        width: 100%;
        background-color: #10B981 !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 14px 20px !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        box-shadow: 0 4px 10px rgba(16, 185, 129, 0.25) !important;
        transition: all 0.2s ease !important;
    }
    
    .stDownloadButton > button:hover {
        background-color: #059669 !important;
        color: #FFFFFF !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar (Perfil centrado)
with st.sidebar:
    st.markdown('<p class="profile-title">Perfil Profesional</p>', unsafe_allow_html=True)
    
    col_a, col_img, col_b = st.columns([1, 4, 1])
    with col_img:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", use_container_width=True)
    
    st.markdown("""
        <div class="profile-container">
            <div class="profile-name">Ian González Viña</div>
            <div class="profile-role">Backend Software Engineer</div>
            <div class="profile-location">📍 Argentina</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    st.download_button(
        label="📄 Descargar CV Profesional",
        data="Contenido del CV...",
        file_name="CV_Ian_Gonzalez_Vina.pdf",
        mime="application/pdf"
    )

# 4. Encabezado Principal (Ubicado ARRIBA DE TODO)
st.markdown('<p class="main-header">Ian González Viña</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Backend Software Engineer & Problem Solver</p>', unsafe_allow_html=True)

# 5. Pestañas Redondeadas (Ubicadas DEBAJO del encabezado principal)
tab1, tab2, tab3, tab4 = st.tabs([
    "Resumen Profesional", 
    "Habilidades Técnicas", 
    "Proyectos Destacados", 
    "Contacto"
])

st.divider()

# 6. Contenido según la pestaña seleccionada
with tab1:
    col_main, col_metrics = st.columns([2.2, 1], gap="large")

    with col_main:
        st.markdown("#### Sobre Mí")
        st.write("""
        Desarrollador de software enfocado en **arquitectura backend**, desarrollo en **Python**, 
        y gestión eficiente de **bases de datos SQL**.
        
        Apasionado por la optimización de código, automatización de procesos y el diagnóstico 
        de infraestructura de servidores. Experiencia práctica construyendo herramientas interactivas, 
        integración de APIs y gestión de entornos virtuales en entornos de desarrollo modernos (`Git`, `VS Code`, `PowerShell`).
        """)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("#### Objetivos Clave")
        
        st.markdown("""
        * **Diseño e implementación:** APIs RESTful escalables, seguras y robustas.
        * **Optimización:** Consultas avanzadas a bases de datos relacionales.
        * **Integración:** Incorporación de servicios de Inteligencia Artificial para diagnóstico y análisis de software.
        """)

    with col_metrics:
        st.markdown("#### Métricas de Impacto")
        
        st.markdown("""
            <div class="metric-card">
                <div class="metric-value">5+</div>
                <div class="metric-label">Proyectos Desarrollados</div>
            </div>
            <br>
            <div class="metric-card">
                <div class="metric-value">100%</div>
                <div class="metric-label">Código Modular en Python</div>
            </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown("#### Competencias y Tecnologías Core")
    st.write("• **Lenguajes:** Python, SQL, Bash / PowerShell")
    st.write("• **Frameworks & Herramientas:** Streamlit, Pandas, NumPy, Git, GitHub")
    st.write("• **Entornos & Despliegue:** Virtualenv, Streamlit Cloud, Linux Server Diagnostics")

with tab3:
    st.markdown("#### Portafolio de Proyectos Backend")
    st.info("Visualización e interacción con proyectos recientes en producción.")

with tab4:
    st.markdown("#### Información de Contacto")
    st.write("Para oportunidades profesionales o colaboraciones de desarrollo backend:")
    st.write("• **Email:** iangonzalezv2005@gmail.com")
    st.write("• **GitHub:** https://github.com/iangonzalezv200509/igv")
    st.write("• **LinkedIn:** https://www.linkedin.com/in/ian-gonzalez-vi%C3%B1a200509/")