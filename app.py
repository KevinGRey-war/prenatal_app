# =========================================================
# 🌸 VIDA NUEVA PREMIUM UI 8.0 FINAL
# =========================================================

import streamlit as st
import random
import base64
import os
import html
import sqlite3

# =========================================================
# 💾 ALMACENAMIENTO DEL RANKING
# =========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RANKING_DB_PATH = os.getenv(
    "RANKING_DB_PATH",
    os.path.join(BASE_DIR, "ranking.db")
)
RANKING_STORAGE_VERSION = 2

SUPABASE_URL = os.getenv("SUPABASE_URL", "").strip()
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "").strip()


def crear_cliente_supabase():
    """Activa el ranking en la nube solo si hay credenciales configuradas."""

    if not SUPABASE_URL or not SUPABASE_KEY:
        return None

    try:
        from supabase import create_client

        return create_client(SUPABASE_URL, SUPABASE_KEY)
    except Exception:
        return None


db = crear_cliente_supabase()

# =========================================================
# ⚙️ CONFIG
# =========================================================

st.set_page_config(
    page_title="Vida Nueva Premium",
    page_icon="🤰",
    layout="wide"
)

# =========================================================
# 🖼️ LOGO
# =========================================================

def get_base64_image(image_path):

    try:

        if os.path.exists(image_path):

            with open(image_path, "rb") as img:

                return base64.b64encode(img.read()).decode()

    except:

        return None

img_base64 = get_base64_image("tuvn.png")

bg_base64 = get_base64_image("prenatal_bg.png")

# =========================================================
# 🎨 CSS
# =========================================================

st.markdown("""

<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800;900&display=swap');

:root{
    --ink:#24324B;
    --muted:#697386;
    --pink:#EC4899;
    --pink-soft:#FCE7F3;
    --violet:#7C3AED;
    --teal:#0F766E;
    --surface:#FFFFFF;
    --line:#E8DFF0;
    --shadow:0 18px 45px rgba(117, 65, 130, 0.12);
}

html, body, [class*="css"]{
    font-family:'Poppins',sans-serif;
}

.stApp{
    background:
        radial-gradient(circle at 8% 5%, rgba(236,72,153,0.13), transparent 30%),
        radial-gradient(circle at 95% 0%, rgba(20,184,166,0.12), transparent 28%),
        linear-gradient(135deg, #FFF8FC 0%, #F7FBFF 50%, #F9F5FF 100%);
    color:var(--ink);
}

header, #MainMenu, footer{
    visibility:hidden;
}

/* El panel administrativo se abre únicamente desde el botón de acceso. */
[data-testid="stSidebar"],
[data-testid="stSidebarCollapsedControl"]{
    display:none;
}

.block-container{
    max-width:1120px;
    padding:clamp(0.7rem, 1.7vw, 1.2rem) 1.5rem 1.5rem;
}

[data-testid="stVerticalBlock"]{
    gap:0.75rem;
}

.main-card{
    background:rgba(255,255,255,0.86);
    border:1px solid rgba(232,223,240,0.95);
    border-radius:28px;
    padding:34px;
    box-shadow:var(--shadow);
    backdrop-filter:blur(10px);
}

.login-logo-wrap{
    display:flex;
    justify-content:center;
    margin:0 auto 8px;
}

.login-logo{
    width:clamp(200px, 22vw, 280px);
    max-width:100%;
    background:white;
    border-radius:12px;
    box-shadow:0 12px 30px rgba(36,50,75,0.06);
}

.brand-title{
    text-align:center;
    font-size:clamp(2.35rem, 4.2vw, 3.35rem);
    color:var(--ink);
    font-weight:900;
    line-height:1.08;
    margin:4px 0 4px;
}

.brand-subtitle{
    text-align:center;
    color:var(--violet);
    margin:0 0 12px;
    font-size:1.35rem;
    font-weight:700;
}

.login-note{
    background:rgba(255,255,255,0.82);
    border:1px solid var(--line);
    border-left:6px solid var(--pink);
    border-radius:18px;
    color:var(--ink);
    font-weight:800;
    line-height:1.45;
    padding:17px 22px;
    margin:0 0 10px;
    box-shadow:0 12px 30px rgba(36,50,75,0.06);
}

.login-note span{
    color:var(--muted);
    display:block;
    font-size:1rem;
    font-weight:700;
    margin-top:4px;
}

.screen-title{
    color:var(--ink);
    font-size:2.25rem;
    font-weight:900;
    line-height:1.15;
    margin:0 0 10px;
}

.screen-caption{
    color:var(--muted);
    font-size:1rem;
    font-weight:600;
    margin-bottom:24px;
}

div[data-testid="stTextInput"],
div[data-testid="stSelectbox"]{
    width:100% !important;
    margin-bottom:0.35rem !important;
}

div[data-testid="stTextInput"] label,
div[data-testid="stSelectbox"] label,
.stRadio > label{
    color:var(--ink) !important;
    font-weight:800 !important;
    font-size:1rem !important;
    letter-spacing:0 !important;
    margin-bottom:0.35rem !important;
}

div[data-testid="stTextInput"] label,
div[data-testid="stSelectbox"] label{
    justify-content:center !important;
    text-align:center !important;
}

div[data-testid="stTextInput"] label p,
div[data-testid="stSelectbox"] label p{
    width:100%;
    text-align:center !important;
}

div[data-testid="stTextInput"] input{
    background:transparent !important;
    color:var(--ink) !important;
    border:none !important;
    border-radius:0 !important;
    height:72px !important;
    min-height:72px !important;
    font-size:1.16rem !important;
    font-weight:800 !important;
    padding:0 20px !important;
    box-shadow:none !important;
    outline:none !important;
}

div[data-testid="stTextInputRootElement"],
div[data-baseweb="input"]{
    background:linear-gradient(180deg, #FFFFFF 0%, #FFFBFD 100%) !important;
    border:1px solid #E4D7EA !important;
    border-radius:20px !important;
    min-height:74px !important;
    height:74px !important;
    box-shadow:0 12px 30px rgba(36,50,75,0.08) !important;
    outline:none !important;
    display:flex !important;
    align-items:center !important;
    overflow:hidden !important;
}

div[data-testid="stTextInputRootElement"]:focus-within,
div[data-baseweb="input"]:focus-within{
    border-color:var(--pink) !important;
    box-shadow:0 0 0 4px rgba(236,72,153,0.12), 0 16px 34px rgba(236,72,153,0.12) !important;
    transform:translateY(-1px);
}

div[data-baseweb="base-input"]{
    border:none !important;
    background:transparent !important;
    box-shadow:none !important;
    height:100% !important;
    width:100% !important;
    display:flex !important;
    align-items:center !important;
}

div[data-testid="stTextInput"] input::placeholder{
    color:#B2A9BA !important;
    opacity:1 !important;
    font-weight:700 !important;
}

div[data-testid="stTextInput"] input:focus{
    border:none !important;
    outline:none !important;
    box-shadow:none !important;
}

div[data-baseweb="select"]{
    min-height:74px !important;
    height:74px !important;
    border-radius:20px !important;
    border:1px solid #E4D7EA !important;
    background:linear-gradient(180deg, #FFFFFF 0%, #FFFBFD 100%) !important;
    display:flex !important;
    align-items:center !important;
    box-shadow:0 12px 30px rgba(36,50,75,0.08) !important;
    transition:border-color 0.15s ease, box-shadow 0.15s ease, transform 0.15s ease;
}

div[data-testid="stSelectbox"]{
    position:relative;
}

div[data-baseweb="select"]:hover{
    border-color:#F4A7CF !important;
    transform:translateY(-1px);
    box-shadow:0 16px 34px rgba(236,72,153,0.12) !important;
}

div[data-baseweb="select"]:focus-within{
    border-color:var(--pink) !important;
    box-shadow:0 0 0 4px rgba(236,72,153,0.12), 0 16px 34px rgba(236,72,153,0.12) !important;
}

div[data-baseweb="select"] > div{
    background:transparent !important;
    border:none !important;
    border-radius:18px !important;
    color:var(--ink) !important;
}

div[data-baseweb="select"] div{
    color:var(--ink) !important;
}

div[data-baseweb="select"] span{
    font-size:1.16rem !important;
    font-weight:800 !important;
    color:var(--ink) !important;
}

div[data-baseweb="select"] svg{
    color:var(--pink) !important;
}

div.stButton > button{
    background:linear-gradient(135deg, var(--pink), #F973B7) !important;
    color:white !important;
    border:none !important;
    border-radius:20px !important;
    min-height:74px !important;
    font-size:1.13rem !important;
    font-weight:900 !important;
    letter-spacing:0 !important;
    width:100%;
    margin-top:0.1rem;
    box-shadow:0 16px 34px rgba(236,72,153,0.30);
    transition:transform 0.15s ease, box-shadow 0.15s ease, filter 0.15s ease;
}

div.stButton > button:hover{
    transform:translateY(-1px);
    filter:saturate(1.06);
    box-shadow:0 16px 34px rgba(236,72,153,0.34);
}

div.stButton > button:active{
    transform:translateY(0);
}

.admin-access-copy{
    max-width:560px;
    margin:14px auto 10px;
    padding:16px 20px;
    text-align:center;
    color:var(--muted);
    background:rgba(255,255,255,0.82);
    border:1px solid rgba(201,162,39,0.34);
    border-radius:20px;
    box-shadow:0 12px 30px rgba(36,50,75,0.08);
}

.admin-access-copy strong{
    display:block;
    color:var(--ink);
    font-size:1.04rem;
    margin-bottom:4px;
}

.admin-access-copy span{
    display:block;
    font-size:0.94rem;
    line-height:1.45;
}

.st-key-abrir_panel_admin{
    width:min(100%, 480px);
    margin:0 auto 18px;
}

.st-key-abrir_panel_admin button{
    min-height:66px !important;
    background:linear-gradient(135deg, #991B1B, #C62828 55%, #E23D55) !important;
    border:1px solid rgba(201,162,39,0.75) !important;
    border-radius:18px !important;
    box-shadow:0 15px 30px rgba(153,27,27,0.24), 0 0 0 4px rgba(201,162,39,0.08) !important;
}

.st-key-abrir_panel_admin button:hover{
    background:linear-gradient(135deg, #7F1D1D, #B91C1C 55%, #D92F4C) !important;
    box-shadow:0 18px 34px rgba(153,27,27,0.30), 0 0 0 4px rgba(201,162,39,0.14) !important;
}

[data-testid="stMetric"]{
    background:rgba(255,255,255,0.9);
    border:1px solid var(--line);
    border-radius:20px;
    padding:16px 18px;
    box-shadow:0 10px 28px rgba(36,50,75,0.07);
}

[data-testid="stHorizontalBlock"]{
    gap:1.15rem;
}

[data-testid="stMetricLabel"]{
    color:var(--muted);
    font-weight:800;
}

[data-testid="stMetricValue"]{
    font-size:2rem;
    font-weight:900;
    color:var(--pink);
}

.stProgress > div > div > div > div{
    background:linear-gradient(90deg, var(--pink), var(--teal));
}

.question-card{
    background:rgba(255,255,255,0.92);
    border:1px solid var(--line);
    border-radius:28px;
    padding:30px;
    box-shadow:var(--shadow);
    margin-top:14px;
    margin-bottom:15px;
}

.question-title{
    font-size:clamp(1.45rem, 3vw, 2rem);
    font-weight:900;
    color:var(--ink);
    line-height:1.28;
    margin-bottom:24px;
}

.quiz-instruction{
    display:flex;
    align-items:center;
    gap:10px;
    width:fit-content;
    margin:0 0 14px;
    padding:10px 14px;
    border-radius:14px;
    background:#FFF7E1;
    border:1px solid #E7C766;
    color:#6B4F00;
    font-size:0.98rem;
    font-weight:900;
    user-select:none;
    pointer-events:none;
}

.stRadio [data-testid="stWidgetLabel"]{
    display:none !important;
}

.stRadio div[role="radiogroup"] > label{
    background:white;
    border:2px solid #EEE7F2;
    border-radius:16px;
    padding:14px 16px !important;
    margin-bottom:12px;
    width:100%;
    font-size:1rem !important;
    font-weight:800 !important;
    color:var(--ink) !important;
    box-shadow:0 6px 18px rgba(36,50,75,0.04);
    transition:border-color 0.15s ease, background 0.15s ease, transform 0.15s ease;
}

.stRadio div[role="radiogroup"] > label p{
    color:var(--ink) !important;
    font-weight:800 !important;
}

.stRadio div[role="radiogroup"] > label:hover{
    border-color:var(--pink);
    background:#FFF4FA;
    transform:translateX(2px);
}

.stRadio div[role="radiogroup"] > label:has(input:checked){
    border-color:var(--pink);
    background:#FFF4FA;
    box-shadow:0 0 0 3px rgba(236,72,153,0.12);
}

.side-card{
    background:rgba(255,255,255,0.92);
    border:1px solid var(--line);
    border-radius:22px;
    padding:22px;
    box-shadow:0 12px 32px rgba(36,50,75,0.08);
    margin-top:14px;
    margin-bottom:12px;
}

.quiz-side{
    background:rgba(255,255,255,0.84);
    border:1px solid var(--line);
    border-radius:22px;
    padding:18px 20px;
    box-shadow:0 12px 32px rgba(36,50,75,0.08);
    color:var(--ink);
    font-weight:800;
}

.quiz-side p{
    margin:0 0 10px;
}

.side-card p{
    color:var(--ink);
    font-weight:800;
    margin-bottom:10px;
}

.success-box,
.error-box{
    padding:18px 20px;
    border-radius:18px;
    font-weight:800;
    font-size:1rem;
    margin:18px 0 6px;
}

.success-box{
    background:#FFF7D6;
    border-left:6px solid #C9A227;
    color:#6B4F00;
}

.error-box{
    background:#FFF0F0;
    border-left:6px solid #DC2626;
    color:#8A1F1F;
}

.ranking-row{
    background:white;
    border:1px solid var(--line);
    border-radius:18px;
    padding:14px 18px;
    margin-bottom:10px;
    box-shadow:0 8px 22px rgba(36,50,75,0.06);
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:16px;
    font-weight:800;
}

.ranking-points{
    color:var(--pink);
    white-space:nowrap;
}

@media (max-width: 768px){
    .block-container{
        padding:0.75rem 0.85rem 1.25rem;
        max-width:100%;
    }

    .brand-title{
        font-size:2.25rem;
        line-height:1.15;
        margin-top:8px;
    }

    .brand-subtitle{
        font-size:1.15rem;
        margin-bottom:14px;
    }

    .main-card,
    .question-card{
        padding:22px;
        border-radius:22px;
    }

    div[data-testid="stTextInputRootElement"],
    div[data-baseweb="input"],
    div[data-baseweb="select"]{
        min-height:64px !important;
        height:64px !important;
        border-radius:18px !important;
    }

    div[data-testid="stTextInput"] input{
        height:62px !important;
        min-height:62px !important;
        font-size:1.08rem !important;
    }

    div.stButton > button{
        min-height:64px !important;
        border-radius:18px !important;
    }

    [data-testid="stMetricValue"]{
        font-size:1.55rem;
    }

    .question-title{
        font-size:1.35rem;
        margin-top:10px;
    }

    .stRadio div[role="radiogroup"] > label{
        min-height:54px;
        display:flex !important;
        align-items:center;
    }
}

@media (max-width: 420px){
    .brand-title{
        font-size:2rem;
    }

    [data-testid="stMetric"]{
        padding:12px 14px;
    }

    [data-testid="stMetricValue"]{
        font-size:1.35rem;
    }

    .ranking-row{
        align-items:flex-start;
        flex-direction:column;
        gap:4px;
    }
}

</style>

""", unsafe_allow_html=True)

if bg_base64:

    st.markdown(f"""

    <style>

    .stApp{{
        background:
            linear-gradient(90deg, rgba(255,248,252,0.82) 0%, rgba(247,251,255,0.72) 48%, rgba(249,245,255,0.58) 100%),
            url("data:image/png;base64,{bg_base64}") center center / cover fixed !important;
    }}

    @media (max-width: 768px){{
        .stApp{{
            background:
                linear-gradient(180deg, rgba(255,248,252,0.88) 0%, rgba(247,251,255,0.80) 55%, rgba(249,245,255,0.70) 100%),
                url("data:image/png;base64,{bg_base64}") center top / cover fixed !important;
        }}
    }}

    </style>

    """, unsafe_allow_html=True)

# =========================================================
# 🔊 VOZ
# =========================================================

def hablar(texto):

    texto = texto.replace("'", "")

    st.components.v1.html(f"""

    <script>

    window.speechSynthesis.cancel();

    var msg = new SpeechSynthesisUtterance('{texto}');

    msg.lang = 'es-ES';

    msg.rate = 0.95;

    msg.pitch = 1.1;

    speechSynthesis.speak(msg);

    </script>

    """, height=0)

# =========================================================
# 📚 PREGUNTAS
# =========================================================

BANCO = {
    "Primer trimestre": [
        {"q": "¿Qué suplemento ayuda a prevenir defectos del tubo neural durante las primeras etapas del embarazo?", "opts": ["Ácido fólico", "Hierro", "Calcio"], "corr": "Ácido fólico", "bien": "Correcto. El ácido fólico ayuda a prevenir defectos del cerebro y la columna del bebé, especialmente cuando se inicia antes de la concepción.", "mal": "La respuesta correcta es ácido fólico. El hierro y el calcio también son importantes, pero cumplen otras funciones."},
        {"q": "¿Cuál es la recomendación más segura sobre el consumo de alcohol durante el embarazo?", "opts": ["Evitarlo por completo", "Limitarlo a una copa con las comidas", "Consumir únicamente cerveza o vino"], "corr": "Evitarlo por completo", "bien": "Correcto. No se conoce una cantidad ni un momento seguros para consumir alcohol durante el embarazo.", "mal": "La respuesta correcta es evitarlo por completo. Ningún tipo de bebida alcohólica se considera segura durante el embarazo."},
        {"q": "Si una embarazada usa un medicamento recetado desde antes del embarazo, ¿qué debe hacer?", "opts": ["Revisar el tratamiento con el personal de salud", "Suspenderlo inmediatamente por cuenta propia", "Continuarlo sin informar en el control prenatal"], "corr": "Revisar el tratamiento con el personal de salud", "bien": "Correcto. El profesional debe valorar los beneficios y riesgos antes de iniciar, cambiar o suspender un medicamento.", "mal": "La respuesta correcta es revisar el tratamiento con el personal de salud; suspenderlo o continuarlo sin valoración puede ser perjudicial."},
        {"q": "¿Cuándo se recomienda realizar el primer control prenatal?", "opts": ["Tan pronto se confirma o sospecha el embarazo", "Después de terminar el primer trimestre", "Cuando comienzan los movimientos del bebé"], "corr": "Tan pronto se confirma o sospecha el embarazo", "bien": "Excelente. El control prenatal temprano permite identificar necesidades y riesgos desde el inicio.", "mal": "La respuesta correcta es tan pronto se confirma o sospecha el embarazo; no es necesario esperar a sentir movimientos."},
        {"q": "¿Cuál de estos síntomas puede ser una molestia habitual del primer trimestre?", "opts": ["Náuseas leves", "Sangrado vaginal abundante", "Pérdida repentina de la visión"], "corr": "Náuseas leves", "bien": "Correcto. Las náuseas leves son frecuentes; el sangrado abundante o los cambios visuales requieren valoración.", "mal": "La respuesta correcta es náuseas leves. Los otros síntomas son señales de alarma y no deben considerarse molestias normales."},
        {"q": "¿Cuál es la forma más segura de preparar frutas y verduras frescas?", "opts": ["Lavarlas cuidadosamente con agua potable", "Limpiarlas solo después de cortarlas", "Remojarlas sin retirar la suciedad visible"], "corr": "Lavarlas cuidadosamente con agua potable", "bien": "Correcto. El lavado cuidadoso ayuda a reducir microorganismos y residuos antes de consumirlas.", "mal": "La respuesta correcta es lavarlas cuidadosamente con agua potable antes de cortarlas o comerlas."},
        {"q": "Al elegir un producto lácteo, ¿qué característica debe verificarse en la etiqueta?", "opts": ["Que sea pasteurizado", "Que sea artesanal", "Que no necesite refrigeración después de abrirlo"], "corr": "Que sea pasteurizado", "bien": "Correcto. La pasteurización reduce el riesgo de infecciones transmitidas por lácteos.", "mal": "La respuesta correcta es que sea pasteurizado; los productos artesanales o sin etiqueta no garantizan este proceso."},
        {"q": "Si aparece sangrado vaginal en el primer trimestre, ¿cuál es la conducta adecuada?", "opts": ["Comunicarse de inmediato con el servicio de salud", "Esperar a que se repita antes de avisar", "Mencionarlo únicamente en la próxima cita programada"], "corr": "Comunicarse de inmediato con el servicio de salud", "bien": "Correcto. El sangrado durante el embarazo necesita orientación y valoración profesional oportuna.", "mal": "La respuesta correcta es comunicarse de inmediato con el servicio de salud, aunque el sangrado parezca escaso."},
        {"q": "¿Qué bebida debe ser la principal fuente de hidratación durante el embarazo?", "opts": ["Agua potable", "Jugos azucarados", "Bebidas deportivas"], "corr": "Agua potable", "bien": "Muy bien. El agua potable hidrata sin añadir alcohol, estimulantes ni exceso de azúcar.", "mal": "La respuesta correcta es agua potable; otras bebidas no deben reemplazarla como fuente principal de hidratación."},
        {"q": "¿Qué medida reduce mejor la exposición del bebé a la nicotina y al humo?", "opts": ["Evitar cigarrillos, vapeadores y humo ajeno", "Cambiar el cigarrillo por un vapeador", "Reducir el número de cigarrillos sin suspenderlos"], "corr": "Evitar cigarrillos, vapeadores y humo ajeno", "bien": "Correcto. La mejor protección es evitar completamente el tabaco, el vapeo y el humo de segunda mano.", "mal": "La respuesta correcta es evitar cigarrillos, vapeadores y humo ajeno; vapear o fumar menos no elimina el riesgo."},
        {"q": "¿Qué información es importante comunicar en la primera consulta prenatal?", "opts": ["Enfermedades previas y todos los medicamentos o suplementos", "Solo los medicamentos con receta", "Únicamente los síntomas del día de la consulta"], "corr": "Enfermedades previas y todos los medicamentos o suplementos", "bien": "Correcto. La historia clínica completa permite planificar una atención prenatal más segura.", "mal": "La respuesta correcta incluye enfermedades previas y todos los productos usados, incluso vitaminas, hierbas y medicamentos sin receta."},
        {"q": "En un embarazo sin complicaciones, ¿qué actividad suele ser una opción adecuada?", "opts": ["Caminar o nadar a intensidad moderada con autorización", "Iniciar un entrenamiento de alta intensidad sin evaluación", "Practicar deportes con riesgo de golpes o caídas"], "corr": "Caminar o nadar a intensidad moderada con autorización", "bien": "Muy bien. La actividad moderada puede aportar beneficios cuando el profesional confirma que es segura.", "mal": "La respuesta correcta es caminar o nadar a intensidad moderada con autorización y ajustar la actividad a cada embarazo."},
        {"q": "¿Qué práctica reduce el riesgo de infecciones al consumir carne?", "opts": ["Cocinarla completamente", "Servirla término medio", "Marinarla sin cocinarla"], "corr": "Cocinarla completamente", "bien": "Correcto. La cocción completa ayuda a eliminar microorganismos que pueden causar enfermedad.", "mal": "La respuesta correcta es cocinarla completamente; marinar o sellar la superficie no sustituye una cocción segura."},
        {"q": "¿Qué estudio utiliza ondas de sonido para valorar la ubicación y evolución inicial del embarazo?", "opts": ["Ecografía obstétrica", "Radiografía abdominal", "Tomografía computarizada"], "corr": "Ecografía obstétrica", "bien": "Correcto. La ecografía obstétrica utiliza ondas de sonido y se realiza cuando la indica el profesional.", "mal": "La respuesta correcta es ecografía obstétrica; los estudios con radiación requieren una indicación médica específica."},
        {"q": "Si los vómitos impiden retener alimentos o líquidos, ¿qué debe hacerse?", "opts": ["Contactar al personal de salud", "Suspender todos los líquidos hasta el día siguiente", "Sustituir el agua por bebidas energéticas"], "corr": "Contactar al personal de salud", "bien": "Correcto. No poder retener líquidos puede causar deshidratación y requiere valoración.", "mal": "La respuesta correcta es contactar al personal de salud; dejar de beber o usar bebidas energéticas puede empeorar la deshidratación."}
    ],
    "Segundo trimestre": [
        {"q": "¿Entre qué semanas se ubica aproximadamente el segundo trimestre?", "opts": ["De la semana 14 a la 27", "De la semana 9 a la 20", "De la semana 28 a la 40"], "corr": "De la semana 14 a la 27", "bien": "Correcto. El segundo trimestre comprende aproximadamente desde la semana 14 hasta el final de la 27.", "mal": "La respuesta correcta es de la semana 14 a la 27; a partir de la semana 28 comienza el tercer trimestre."},
        {"q": "¿Qué mineral se utiliza principalmente para prevenir y tratar la anemia por deficiencia durante el embarazo?", "opts": ["Hierro", "Calcio", "Yodo"], "corr": "Hierro", "bien": "Muy bien. El hierro es necesario para producir hemoglobina y cubrir el aumento del volumen sanguíneo.", "mal": "La respuesta correcta es hierro. El calcio y el yodo son importantes, pero no sustituyen el tratamiento de la anemia por falta de hierro."},
        {"q": "¿Qué cambio suele empezar a notar la madre durante el segundo trimestre?", "opts": ["Los primeros movimientos del bebé", "Contracciones regulares de trabajo de parto", "La ruptura de la fuente"], "corr": "Los primeros movimientos del bebé", "bien": "Correcto. Muchas madres comienzan a percibir movimientos fetales durante este trimestre, aunque el momento varía.", "mal": "La respuesta correcta es los primeros movimientos del bebé; las contracciones regulares o la pérdida de líquido requieren valoración."},
        {"q": "¿Qué estudio prenatal permite observar con detalle la anatomía del bebé?", "opts": ["Ecografía morfológica", "Prueba de glucosa", "Hemograma materno"], "corr": "Ecografía morfológica", "bien": "Correcto. La ecografía morfológica revisa estructuras y crecimiento fetal; los otros estudios evalúan la salud materna.", "mal": "La respuesta correcta es ecografía morfológica. La prueba de glucosa y el hemograma responden a objetivos diferentes."},
        {"q": "¿Qué medición se utiliza para detectar hipertensión durante el control prenatal?", "opts": ["Presión arterial", "Glucosa en sangre", "Hemoglobina"], "corr": "Presión arterial", "bien": "Correcto. La presión arterial se controla en las consultas para detectar trastornos hipertensivos.", "mal": "La respuesta correcta es presión arterial; la glucosa y la hemoglobina evalúan otras condiciones."},
        {"q": "¿Cuándo suele realizarse la detección de diabetes gestacional si no se indicó antes?", "opts": ["Entre las semanas 24 y 28", "Entre las semanas 11 y 14", "Entre las semanas 32 y 36"], "corr": "Entre las semanas 24 y 28", "bien": "Correcto. Generalmente se realiza entre las semanas 24 y 28, aunque puede adelantarse según los factores de riesgo.", "mal": "La respuesta correcta es entre las semanas 24 y 28, salvo que el profesional indique otro momento."},
        {"q": "¿Cuál es una actividad apropiada para muchas embarazadas sin complicaciones?", "opts": ["Caminar o nadar a intensidad moderada", "Practicar deportes de contacto", "Comenzar ejercicios con alto riesgo de caída"], "corr": "Caminar o nadar a intensidad moderada", "bien": "Excelente. Las actividades moderadas suelen ser adecuadas si el profesional no identifica contraindicaciones.", "mal": "La respuesta correcta es caminar o nadar a intensidad moderada; deben evitarse golpes y caídas."},
        {"q": "Si aparece mareo durante la actividad física, ¿cuál es la respuesta adecuada?", "opts": ["Detenerse y solicitar orientación profesional", "Bajar un poco el ritmo y terminar la rutina", "Beber algo y reiniciar el ejercicio de inmediato"], "corr": "Detenerse y solicitar orientación profesional", "bien": "Correcto. El mareo es una señal para suspender el ejercicio, descansar y consultar antes de reanudar la actividad.", "mal": "La respuesta correcta es detenerse y solicitar orientación profesional; no se debe continuar hasta aclarar la causa."},
        {"q": "¿Qué nutriente es especialmente importante para la formación de huesos y dientes?", "opts": ["Calcio", "Hierro", "Ácido fólico"], "corr": "Calcio", "bien": "Muy bien. El calcio participa en la formación y mantenimiento de huesos y dientes.", "mal": "La respuesta correcta es calcio. El hierro y el ácido fólico son esenciales, pero cumplen funciones diferentes."},
        {"q": "¿Cuál de estas combinaciones es una señal de alarma durante el embarazo?", "opts": ["Dolor de cabeza intenso y visión borrosa", "Acidez leve después de comer", "Hinchazón leve de tobillos al final del día"], "corr": "Dolor de cabeza intenso y visión borrosa", "bien": "Correcto. El dolor de cabeza intenso acompañado de alteraciones visuales requiere valoración inmediata.", "mal": "La respuesta correcta es dolor de cabeza intenso y visión borrosa, porque puede relacionarse con un trastorno hipertensivo."},
        {"q": "Ante una salida repentina o continua de líquido por la vagina, ¿qué se debe hacer?", "opts": ["Comunicarse de inmediato con el servicio de salud", "Esperar hasta que comiencen contracciones", "Usar una toalla y comentarlo en la próxima cita"], "corr": "Comunicarse de inmediato con el servicio de salud", "bien": "Correcto. La pérdida de líquido puede indicar ruptura de membranas y necesita valoración.", "mal": "La respuesta correcta es comunicarse de inmediato con el servicio de salud; no se debe esperar a que aparezcan contracciones."},
        {"q": "¿Qué práctica ayuda a prevenir infecciones transmitidas por alimentos?", "opts": ["Separar alimentos crudos y cocinar bien carnes y huevos", "Guardar juntos alimentos crudos y cocidos", "Consumir lácteos artesanales sin comprobar la pasteurización"], "corr": "Separar alimentos crudos y cocinar bien carnes y huevos", "bien": "Correcto. Separar, cocinar, limpiar y refrigerar adecuadamente reduce el riesgo de infección.", "mal": "La respuesta correcta es separar alimentos crudos y cocinar bien carnes y huevos."},
        {"q": "¿Qué patrón de alimentación es más adecuado durante el embarazo?", "opts": ["Una dieta variada ajustada a las necesidades individuales", "Duplicar todas las porciones porque se come por dos", "Eliminar por completo los carbohidratos"], "corr": "Una dieta variada ajustada a las necesidades individuales", "bien": "Correcto. La alimentación debe aportar variedad y nutrientes sin asumir que es necesario comer el doble.", "mal": "La respuesta correcta es una dieta variada ajustada a las necesidades individuales y a la orientación profesional."},
        {"q": "¿Qué cambio en los movimientos del bebé debe comunicarse al personal de salud?", "opts": ["Una disminución respecto a su patrón habitual", "Que aumenten temporalmente después de comer", "Sentir pequeños movimientos rítmicos parecidos al hipo"], "corr": "Una disminución respecto a su patrón habitual", "bien": "Correcto. Lo importante es reconocer cambios respecto al patrón habitual del bebé.", "mal": "La respuesta correcta es una disminución respecto a su patrón habitual; ante la duda se debe consultar."},
        {"q": "¿Qué combinación de hábitos favorece el bienestar en el segundo trimestre?", "opts": ["Mantener controles, hidratarse y descansar", "Guardar reposo absoluto sin indicación", "Usar bebidas energéticas para compensar el cansancio"], "corr": "Mantener controles, hidratarse y descansar", "bien": "Correcto. Los controles regulares, la hidratación y el descanso contribuyen al bienestar materno.", "mal": "La respuesta correcta es mantener controles, hidratarse y descansar; el reposo absoluto solo se realiza si está indicado."}
    ],
    "Tercer trimestre": [
        {"q": "¿Desde qué semana comienza aproximadamente el tercer trimestre?", "opts": ["Desde la semana 28", "Desde la semana 24", "Desde la semana 32"], "corr": "Desde la semana 28", "bien": "Correcto. El tercer trimestre comienza aproximadamente en la semana 28 y continúa hasta el nacimiento.", "mal": "La respuesta correcta es desde la semana 28; las semanas anteriores corresponden al segundo trimestre."},
        {"q": "¿Qué característica distingue generalmente a las contracciones de Braxton Hicks?", "opts": ["Son irregulares y no aumentan progresivamente", "Se vuelven regulares, más frecuentes e intensas", "Siempre provocan salida de líquido o sangrado"], "corr": "Son irregulares y no aumentan progresivamente", "bien": "Muy bien. Las contracciones de práctica suelen ser irregulares y no siguen el patrón progresivo del trabajo de parto.", "mal": "La respuesta correcta es que son irregulares y no aumentan progresivamente; ante dudas se debe consultar."},
        {"q": "¿Qué patrón de contracciones puede indicar el inicio del trabajo de parto?", "opts": ["Regulares, cada vez más frecuentes e intensas", "Aisladas y que desaparecen con reposo", "Irregulares y sin cambios con el paso del tiempo"], "corr": "Regulares, cada vez más frecuentes e intensas", "bien": "Correcto. El trabajo de parto suele producir contracciones con un patrón regular y progresivo.", "mal": "La respuesta correcta es regulares, cada vez más frecuentes e intensas; las contracciones aisladas o irregulares suelen corresponder a otra causa."},
        {"q": "Si se sospecha que se rompió la fuente, ¿cuál es la conducta adecuada?", "opts": ["Contactar y acudir al servicio de salud", "Esperar en casa hasta que aparezca dolor", "Realizar una revisión vaginal por cuenta propia"], "corr": "Contactar y acudir al servicio de salud", "bien": "Correcto. La posible ruptura de membranas necesita valoración para proteger a la madre y al bebé.", "mal": "La respuesta correcta es contactar y acudir al servicio de salud; no se debe esperar ni introducir objetos en la vagina."},
        {"q": "Si el bebé se mueve menos que en su patrón habitual, ¿qué debe hacerse?", "opts": ["Contactar de inmediato al personal de salud", "Tomar algo dulce y esperar hasta el día siguiente", "Esperar a la próxima consulta prenatal"], "corr": "Contactar de inmediato al personal de salud", "bien": "Correcto. Una reducción de movimientos respecto al patrón habitual necesita evaluación oportuna.", "mal": "La respuesta correcta es contactar de inmediato al personal de salud; no se debe retrasar la consulta."},
        {"q": "¿Qué síntomas pueden relacionarse con un trastorno hipertensivo del embarazo?", "opts": ["Dolor de cabeza intenso y alteraciones visuales", "Acidez después de una comida abundante", "Hinchazón leve de tobillos al terminar el día"], "corr": "Dolor de cabeza intenso y alteraciones visuales", "bien": "Correcto. El dolor intenso y los cambios visuales son señales de alarma que requieren valoración inmediata.", "mal": "La respuesta correcta es dolor de cabeza intenso y alteraciones visuales, porque pueden indicar una complicación que necesita atención inmediata."},
        {"q": "¿Cómo se debe actuar ante un sangrado vaginal abundante?", "opts": ["Buscar atención obstétrica urgente", "Guardar reposo y observar si se detiene", "Esperar a la siguiente consulta programada"], "corr": "Buscar atención obstétrica urgente", "bien": "Correcto. El sangrado abundante puede representar una emergencia y requiere atención inmediata.", "mal": "La respuesta correcta es buscar atención obstétrica urgente; no se debe esperar para ver si desaparece."},
        {"q": "Si aparecen contracciones regulares antes de completar 37 semanas, ¿qué se debe hacer?", "opts": ["Comunicarse de inmediato con el servicio de salud", "Esperar a que sean muy dolorosas", "Tomar un analgésico y continuar las actividades"], "corr": "Comunicarse de inmediato con el servicio de salud", "bien": "Correcto. Podrían ser signos de parto prematuro y necesitan evaluación sin demora.", "mal": "La respuesta correcta es comunicarse de inmediato con el servicio de salud; no se debe esperar a que aumente el dolor."},
        {"q": "¿Qué preparación práctica conviene completar antes del nacimiento?", "opts": ["Reunir documentos, controles y artículos esenciales para madre y bebé", "Preparar únicamente la ropa del bebé", "Esperar al inicio del parto para buscar documentos y transporte"], "corr": "Reunir documentos, controles y artículos esenciales para madre y bebé", "bien": "Muy bien. Tener documentos, registros prenatales y artículos esenciales listos facilita una salida segura al hospital.", "mal": "La respuesta correcta es reunir documentos, controles y artículos esenciales para madre y bebé; la preparación debe hacerse antes del parto."},
        {"q": "¿Qué elementos deben formar parte del plan de traslado para el parto?", "opts": ["Centro de atención, transporte, ruta y persona de apoyo", "Solo una lista de objetos para el bebé", "Decidir el lugar de atención cuando comiencen las contracciones"], "corr": "Centro de atención, transporte, ruta y persona de apoyo", "bien": "Correcto. Definir con anticipación el lugar, el traslado y el apoyo reduce demoras.", "mal": "La respuesta correcta es centro de atención, transporte, ruta y persona de apoyo."},
        {"q": "¿Qué información es prioritaria revisar durante los controles prenatales finales?", "opts": ["Señales de parto, señales de alarma y cuándo acudir", "Solo la fecha probable de parto", "Medicamentos para iniciar sin indicación al sentir contracciones"], "corr": "Señales de parto, señales de alarma y cuándo acudir", "bien": "Excelente. Reconocer las señales y saber dónde acudir permite tomar decisiones oportunas.", "mal": "La respuesta correcta es señales de parto, señales de alarma y cuándo acudir; la fecha probable por sí sola no permite planificar todas las situaciones."},
        {"q": "¿Cómo deben observarse los movimientos del bebé en el tercer trimestre?", "opts": ["Comparándolos con su patrón habitual y siguiendo la guía profesional", "Usando el mismo número fijo para todos los embarazos", "Revisándolos únicamente una vez por semana"], "corr": "Comparándolos con su patrón habitual y siguiendo la guía profesional", "bien": "Correcto. Cada bebé tiene un patrón; cualquier disminución o cambio importante debe comunicarse.", "mal": "La respuesta correcta es comparándolos con su patrón habitual y siguiendo la guía profesional."},
        {"q": "¿Qué elemento de seguridad conviene instalar antes de trasladar al recién nacido en automóvil?", "opts": ["Una silla infantil adecuada e instalada correctamente", "Un cojín sujeto con el cinturón de un adulto", "Un portabebé colocado en el asiento delantero"], "corr": "Una silla infantil adecuada e instalada correctamente", "bien": "Correcto. La silla infantil apropiada brinda la protección necesaria durante el traslado.", "mal": "La respuesta correcta es una silla infantil adecuada e instalada correctamente; los brazos o el cinturón de adulto no la sustituyen."},
        {"q": "¿Qué estrategia ayuda a manejar el cansancio y mantener una buena nutrición al final del embarazo?", "opts": ["Comidas variadas, hidratación y pausas de descanso", "Duplicar todas las porciones en cada comida", "Usar bebidas energéticas para dormir menos"], "corr": "Comidas variadas, hidratación y pausas de descanso", "bien": "Correcto. Una alimentación equilibrada, agua y descanso apoyan el bienestar sin recurrir a estimulantes.", "mal": "La respuesta correcta es comidas variadas, hidratación y pausas de descanso; no es necesario comer el doble."},
        {"q": "Ante hinchazón repentina de la cara o las manos, ¿qué se debe hacer?", "opts": ["Contactar de inmediato al personal de salud", "Elevar las piernas y esperar a la próxima cita", "Tomar un diurético sin indicación"], "corr": "Contactar de inmediato al personal de salud", "bien": "Correcto. La hinchazón repentina puede ser una señal de alarma y requiere valoración.", "mal": "La respuesta correcta es contactar de inmediato al personal de salud; no se deben usar diuréticos por cuenta propia."}
    ]
}


def preparar_examen(preguntas, cantidad=10):
    """Elige preguntas y mezcla sus opciones sin modificar el banco original."""

    seleccionadas = random.sample(preguntas, min(cantidad, len(preguntas)))
    examen = []

    for pregunta in seleccionadas:
        copia = {**pregunta, "opts": list(pregunta["opts"])}
        random.shuffle(copia["opts"])
        examen.append(copia)

    return examen

# =========================================================
# 💾 RANKING
# =========================================================

def inicializar_ranking_local():
    """Crea la base local si todavía no existe."""

    conexion = sqlite3.connect(RANKING_DB_PATH, timeout=10)

    try:
        conexion.execute("""
            CREATE TABLE IF NOT EXISTS ranking (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                puntos INTEGER NOT NULL,
                trimestre TEXT NOT NULL,
                creado_en TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conexion.execute("""
            CREATE INDEX IF NOT EXISTS idx_ranking_puntos
            ON ranking (puntos DESC, creado_en ASC)
        """)
        conexion.commit()
    finally:
        conexion.close()


def guardar_resultado(nombre, puntos, trimestre):
    """Guarda siempre en local y sincroniza en la nube si está configurada."""

    nombre_limpio = " ".join(str(nombre).split())[:60] or "Participante"
    puntos_limpios = max(0, min(100, int(puntos)))
    trimestre_limpio = str(trimestre)[:30]

    try:
        inicializar_ranking_local()
        conexion = sqlite3.connect(RANKING_DB_PATH, timeout=10)

        try:
            conexion.execute(
                """
                INSERT INTO ranking (nombre, puntos, trimestre)
                VALUES (?, ?, ?)
                """,
                (nombre_limpio, puntos_limpios, trimestre_limpio)
            )
            conexion.commit()
        finally:
            conexion.close()
    except (OSError, sqlite3.Error):
        st.warning(
            "El resultado no pudo guardarse en este equipo. "
            "El puntaje final sigue visible en pantalla."
        )
        return False

    if db is not None:
        try:
            db.table("ranking").insert({
                "nombre": nombre_limpio,
                "puntos": puntos_limpios,
                "correo": "sin_correo"
            }).execute()
        except Exception:
            # El ranking local es la fuente segura cuando la nube no responde.
            pass

    return True


def obtener_ranking(limite=10):
    """Combina resultados locales y remotos, conservando el mejor por persona."""

    filas = []

    try:
        inicializar_ranking_local()
        conexion = sqlite3.connect(RANKING_DB_PATH, timeout=10)
        conexion.row_factory = sqlite3.Row

        try:
            filas.extend(
                dict(fila)
                for fila in conexion.execute(
                    """
                    SELECT nombre, puntos
                    FROM ranking
                    ORDER BY puntos DESC, creado_en ASC
                    LIMIT 500
                    """
                ).fetchall()
            )
        finally:
            conexion.close()
    except (OSError, sqlite3.Error):
        pass

    if db is not None:
        try:
            respuesta = db.table("ranking").select(
                "nombre,puntos"
            ).order(
                "puntos",
                desc=True
            ).limit(100).execute()

            filas.extend(respuesta.data or [])
        except Exception:
            pass

    mejores = {}

    for fila in filas:
        nombre = " ".join(str(fila.get("nombre", "")).split())[:60]

        if not nombre:
            continue

        try:
            puntos = max(0, min(100, int(fila.get("puntos", 0))))
        except (TypeError, ValueError):
            continue

        clave = nombre.casefold()

        if clave not in mejores or puntos > mejores[clave]["puntos"]:
            mejores[clave] = {"nombre": nombre, "puntos": puntos}

    ranking = sorted(
        mejores.values(),
        key=lambda fila: (-fila["puntos"], fila["nombre"].casefold())
    )

    return ranking[:limite]

# =========================================================
# SESSION
# =========================================================

if "fase" not in st.session_state:

    st.session_state.update({

        "fase":"login",
        "user":"",
        "pts":0,
        "idx":0,
        "resp":False,
        "fb":"",
        "correcto":False,
        "respuesta_seleccionada":None,
        "trimestre":"Primer trimestre",
        "examen":[],
        "ranking_guardado":False,
        "ranking_storage_version":RANKING_STORAGE_VERSION
    })

if st.session_state.get("ranking_storage_version") != RANKING_STORAGE_VERSION:
    # Recupera también el resultado de una sesión que falló con la clave antigua.
    st.session_state.ranking_guardado = False
    st.session_state.ranking_storage_version = RANKING_STORAGE_VERSION

# =========================================================
# LOGIN
# =========================================================

if st.session_state.fase == "login":

    col1,col2,col3 = st.columns([0.85,1.45,0.85])

    with col2:

        if img_base64:

            st.markdown(f"""

            <div class='login-logo-wrap'>
                <img class='login-logo' src='data:image/png;base64,{img_base64}' alt='Logo Vida Nueva'>
            </div>

            """, unsafe_allow_html=True)

        st.markdown("<h1 class='brand-title'>Tecnológico Universitario Vida Nueva</h1>", unsafe_allow_html=True)

        st.markdown("<h3 class='brand-subtitle'>Cuidado Prenatal Inteligente</h3>", unsafe_allow_html=True)

        nombre = st.text_input(
            "Nombre de la mamá",
            placeholder="Escribe tu nombre..."
        )

        trimestre = st.selectbox(
            "Elige el trimestre de embarazo",
            list(BANCO.keys())
        )

        st.markdown(f"""

        <div class='login-note'>
            {trimestre}
            <span>La app preparará 10 preguntas aleatorias para esta etapa.</span>
        </div>

        """, unsafe_allow_html=True)

        if st.button("COMENZAR EXPERIENCIA", use_container_width=True):

            if nombre != "":

                st.session_state.user = nombre

                st.session_state.trimestre = trimestre

                st.session_state.examen = preparar_examen(
                    BANCO[trimestre],
                    10
                )

                st.session_state.fase = "test"

                st.rerun()

            else:

                st.warning("Escribe el nombre de la mamá para comenzar.")

        st.markdown(
            "<div style='height:4px'></div>",
            unsafe_allow_html=True
        )

        st.markdown("""
        <div class='admin-access-copy'>
            <strong>🔐 Acceso administrativo protegido</strong>
            <span>La contraseña se verificará en esta misma pestaña antes de mostrar los reportes.</span>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "🔐 ENTRAR AL PANEL ADMINISTRATIVO",
            key="abrir_panel_admin",
            help="Continuar a la pantalla protegida de verificación",
            type="secondary",
            width="stretch"
        ):
            st.switch_page("pages/panel_admin.py")

# =========================================================
# TEST
# =========================================================

elif st.session_state.fase == "test":

    actual = st.session_state.examen[
        st.session_state.idx
    ]

    progreso = (
        st.session_state.idx + 1
    ) / len(st.session_state.examen)

    c1,c2,c3 = st.columns(3)

    with c1:

        st.metric(
            "Puntaje",
            f"{st.session_state.pts}/100"
        )

    with c2:

        st.metric(
            "Pregunta",
            f"{st.session_state.idx + 1}/{len(st.session_state.examen)}"
        )

    with c3:

        st.metric(
            "Progreso",
            f"{int(progreso*100)}%"
        )

    st.progress(progreso)

    left,right = st.columns([3,1])

    with left:

        st.markdown(f"""

        <div class='question-title'>

        {actual['q']}

        </div>

        """, unsafe_allow_html=True)

        st.markdown("""

        <div class='quiz-instruction'>
            💡 Elige la respuesta correcta
        </div>

        """, unsafe_allow_html=True)

        if st.session_state.resp:

            indice_correcto = actual["opts"].index(actual["corr"]) + 1
            indice_seleccionado = actual["opts"].index(
                st.session_state.respuesta_seleccionada
            ) + 1

            regla_error = ""

            if not st.session_state.correcto:
                regla_error = f"""
                .stRadio div[role="radiogroup"] > label:nth-child({indice_seleccionado}){{
                    background:#FFF0F0 !important;
                    border-color:#DC2626 !important;
                    color:#8A1F1F !important;
                    box-shadow:0 0 0 3px rgba(220,38,38,0.12) !important;
                    opacity:1 !important;
                }}
                """

            st.markdown(f"""

            <style>
            .stRadio div[role="radiogroup"] > label:nth-child({indice_correcto}){{
                background:#FFF7D6 !important;
                border-color:#C9A227 !important;
                color:#6B4F00 !important;
                box-shadow:0 0 0 3px rgba(201,162,39,0.14) !important;
                opacity:1 !important;
            }}

            .stRadio div[role="radiogroup"] > label:nth-child({indice_correcto}) p{{
                color:#6B4F00 !important;
            }}

            {regla_error}

            .stRadio div[role="radiogroup"] > label:nth-child({indice_seleccionado}) p{{
                color:{'#6B4F00' if st.session_state.correcto else '#8A1F1F'} !important;
            }}
            </style>

            """, unsafe_allow_html=True)

        def mostrar_opcion(opcion):

            if not st.session_state.resp:
                return opcion

            if opcion == actual["corr"]:
                return f"✓ {opcion}"

            if opcion == st.session_state.respuesta_seleccionada:
                return f"✕ {opcion}"

            return opcion

        respuesta = st.radio(
            "Opciones de respuesta",
            actual["opts"],
            index=None,
            format_func=mostrar_opcion,
            key=f"r_{st.session_state.idx}",
            disabled=st.session_state.resp,
            label_visibility="collapsed"
        )

        if not st.session_state.resp:

            if st.button(
                "CONFIRMAR RESPUESTA",
                disabled=respuesta is None,
                use_container_width=True
            ):

                correcto = (
                    respuesta == actual["corr"]
                )

                st.session_state.correcto = correcto

                st.session_state.respuesta_seleccionada = respuesta

                if correcto:

                    st.session_state.pts += 10

                    st.session_state.fb = actual["bien"]

                else:

                    st.session_state.fb = (
                        f"Elegiste «{respuesta}». {actual['mal']}"
                    )

                st.session_state.resp = True

                st.rerun()

        else:

            if st.session_state.correcto:

                st.markdown(f"""

                <div class='success-box'>

                ✅ {st.session_state.fb}

                </div>

                """, unsafe_allow_html=True)

            else:

                st.markdown(f"""

                <div class='error-box'>

                ❌ {st.session_state.fb}

                </div>

                """, unsafe_allow_html=True)

            hablar(st.session_state.fb)

            if st.button("SIGUIENTE"):

                st.session_state.idx += 1

                st.session_state.resp = False

                st.session_state.respuesta_seleccionada = None

                if st.session_state.idx >= len(st.session_state.examen):

                    st.session_state.fase = "final"

                st.rerun()

    with right:

        st.markdown(f"""

        <div class='quiz-side'>
            <p>Paciente: {html.escape(st.session_state.user)}</p>
            <p>Etapa: {st.session_state.trimestre}</p>
            <p>Preguntas: {len(st.session_state.examen)}</p>
        </div>

        """, unsafe_allow_html=True)

# =========================================================
# FINAL
# =========================================================

elif st.session_state.fase == "final":

    if not st.session_state.ranking_guardado:

        guardar_resultado(
            st.session_state.user,
            st.session_state.pts,
            st.session_state.trimestre
        )

        st.session_state.ranking_guardado = True

    st.balloons()

    st.markdown("""

    <h1 class='screen-title'>¡Felicidades!</h1>
    <p class='screen-caption'>Completaste la experiencia de cuidado prenatal.</p>

    """, unsafe_allow_html=True)

    st.metric(
        "Puntaje final",
        f"{st.session_state.pts}/100"
    )

    st.markdown(f"""

    <div class='side-card'>
        <p>Etapa: {st.session_state.trimestre}</p>
        <p>Preguntas respondidas: {len(st.session_state.examen)}</p>
    </div>

    """, unsafe_allow_html=True)

    st.markdown("<h2 class='screen-title' style='font-size:1.55rem;margin-top:24px;'>Ranking de participantes</h2>", unsafe_allow_html=True)

    ranking = obtener_ranking()

    if ranking:

        for i,fila in enumerate(ranking):

            medal = "🏅"

            if i == 0:
                medal = "🥇"

            elif i == 1:
                medal = "🥈"

            elif i == 2:
                medal = "🥉"

            nombre_ranking = html.escape(str(fila["nombre"]))

            st.markdown(f"""

            <div class='ranking-row'>
                <span>{medal} {nombre_ranking}</span>
                <span class='ranking-points'>{fila['puntos']} pts</span>
            </div>

            """, unsafe_allow_html=True)

    else:

        st.info("Todavía no hay resultados guardados en el ranking.")

    if st.button("VOLVER A JUGAR"):

        st.session_state.clear()

        st.rerun()
