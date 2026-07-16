# =========================================================
# 🌸 VIDA NUEVA PREMIUM UI 8.0 FINAL
# =========================================================

import streamlit as st
import random
import base64
import os
import html
from supabase import create_client

# =========================================================
# 🔐 SUPABASE
# =========================================================

SUPABASE_URL = "https://ohswfrjxertuwtsocyhf.supabase.co"
SUPABASE_KEY = "sb_secret_0DcETvMBG6onZxM_cIf8LQ_4XCsANiB"

db = create_client(SUPABASE_URL, SUPABASE_KEY)

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

.stRadio label{
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

.stRadio label p{
    color:var(--ink) !important;
    font-weight:800 !important;
}

.stRadio label:hover{
    border-color:var(--pink);
    background:#FFF4FA;
    transform:translateX(2px);
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
    background:#EAFBF1;
    border-left:6px solid #16A34A;
    color:#14532D;
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

    .stRadio label{
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
        {"q": "¿Qué vitamina ayuda a prevenir defectos del tubo neural del bebé?", "opts": ["Ácido fólico", "Vitamina C"], "corr": "Ácido fólico", "bien": "Correcto. El ácido fólico es muy importante al inicio del embarazo.", "mal": "La respuesta correcta es ácido fólico. Ayuda al desarrollo del sistema nervioso del bebé."},
        {"q": "¿Qué bebida debe evitarse durante todo el embarazo?", "opts": ["Alcohol", "Agua"], "corr": "Alcohol", "bien": "Muy bien. El alcohol puede afectar el desarrollo del bebé.", "mal": "La respuesta correcta es alcohol. Debe evitarse durante el embarazo."},
        {"q": "¿Qué síntoma suele ser común en las primeras semanas?", "opts": ["Náuseas", "Fracturas"], "corr": "Náuseas", "bien": "Correcto. Las náuseas son frecuentes por los cambios hormonales.", "mal": "La respuesta correcta es náuseas. Son comunes en el primer trimestre."},
        {"q": "¿Qué control es importante iniciar en el primer trimestre?", "opts": ["Control prenatal", "Entrenamiento intenso"], "corr": "Control prenatal", "bien": "Excelente. El control prenatal temprano ayuda a cuidar a la mamá y al bebé.", "mal": "La respuesta correcta es control prenatal. Debe iniciarse lo antes posible."},
        {"q": "¿Qué alimento conviene lavar muy bien antes de consumir?", "opts": ["Frutas y verduras", "Caramelos cerrados"], "corr": "Frutas y verduras", "bien": "Correcto. Lavar frutas y verduras ayuda a prevenir infecciones.", "mal": "La respuesta correcta es frutas y verduras. Deben lavarse muy bien."},
        {"q": "¿Qué debe hacer la embarazada antes de tomar medicamentos?", "opts": ["Consultar al médico", "Automedicarse"], "corr": "Consultar al médico", "bien": "Muy bien. Los medicamentos deben consultarse con un profesional.", "mal": "La respuesta correcta es consultar al médico. No es recomendable automedicarse."},
        {"q": "¿Qué hábito ayuda al bienestar durante el embarazo?", "opts": ["Dormir y descansar", "Fumar"], "corr": "Dormir y descansar", "bien": "Correcto. El descanso favorece la salud de la mamá.", "mal": "La respuesta correcta es dormir y descansar. Fumar debe evitarse."},
        {"q": "¿Qué señal debe comunicarse al personal de salud?", "opts": ["Sangrado vaginal", "Antojo ocasional"], "corr": "Sangrado vaginal", "bien": "Correcto. El sangrado debe ser evaluado por personal de salud.", "mal": "La respuesta correcta es sangrado vaginal. Es una señal de alarma."},
        {"q": "¿Qué líquido es recomendable tomar con frecuencia?", "opts": ["Agua", "Bebidas alcohólicas"], "corr": "Agua", "bien": "Muy bien. Mantenerse hidratada es importante.", "mal": "La respuesta correcta es agua. La hidratación ayuda al bienestar."},
        {"q": "¿Qué estudio suele confirmar y valorar el embarazo al inicio?", "opts": ["Ecografía", "Radiografía innecesaria"], "corr": "Ecografía", "bien": "Correcto. La ecografía ayuda a valorar el embarazo.", "mal": "La respuesta correcta es ecografía. Debe indicarla el profesional de salud."}
    ],
    "Segundo trimestre": [
        {"q": "¿Entre qué semanas se ubica generalmente el segundo trimestre?", "opts": ["Semanas 13 a 27", "Semanas 1 a 8"], "corr": "Semanas 13 a 27", "bien": "Correcto. El segundo trimestre va aproximadamente de la semana 13 a la 27.", "mal": "La respuesta correcta es semanas 13 a 27."},
        {"q": "¿Qué mineral ayuda a prevenir anemia en el embarazo?", "opts": ["Hierro", "Azúcar"], "corr": "Hierro", "bien": "Muy bien. El hierro ayuda a prevenir anemia.", "mal": "La respuesta correcta es hierro. Es importante para la sangre."},
        {"q": "¿Qué movimiento suele empezar a sentirse en este trimestre?", "opts": ["Movimientos del bebé", "Caída de dientes"], "corr": "Movimientos del bebé", "bien": "Correcto. Muchas mamás empiezan a sentir movimientos del bebé.", "mal": "La respuesta correcta es movimientos del bebé."},
        {"q": "¿Qué actividad suele ser beneficiosa si el médico la permite?", "opts": ["Caminar suavemente", "Levantar peso excesivo"], "corr": "Caminar suavemente", "bien": "Excelente. La actividad suave puede ser beneficiosa con autorización médica.", "mal": "La respuesta correcta es caminar suavemente, si el médico lo permite."},
        {"q": "¿Qué debe vigilarse en los controles prenatales?", "opts": ["Presión arterial", "Color de zapatos"], "corr": "Presión arterial", "bien": "Correcto. La presión arterial es un dato importante del control prenatal.", "mal": "La respuesta correcta es presión arterial."},
        {"q": "¿Qué nutriente ayuda a fortalecer huesos y dientes?", "opts": ["Calcio", "Cafeína"], "corr": "Calcio", "bien": "Muy bien. El calcio apoya la salud ósea.", "mal": "La respuesta correcta es calcio."},
        {"q": "¿Qué señal de alarma requiere atención?", "opts": ["Dolor de cabeza fuerte", "Sueño moderado"], "corr": "Dolor de cabeza fuerte", "bien": "Correcto. Un dolor de cabeza fuerte debe comunicarse al personal de salud.", "mal": "La respuesta correcta es dolor de cabeza fuerte."},
        {"q": "¿Qué examen puede evaluar el crecimiento y anatomía del bebé?", "opts": ["Ecografía morfológica", "Prueba de visión"], "corr": "Ecografía morfológica", "bien": "Correcto. La ecografía morfológica permite valorar al bebé.", "mal": "La respuesta correcta es ecografía morfológica."},
        {"q": "¿Qué postura puede ayudar a descansar mejor si hay incomodidad?", "opts": ["De lado", "Boca abajo"], "corr": "De lado", "bien": "Muy bien. Dormir de lado suele ser más cómodo y seguro.", "mal": "La respuesta correcta es de lado."},
        {"q": "¿Qué debe hacerse si disminuyen los movimientos del bebé?", "opts": ["Consultar de inmediato", "Ignorarlo varios días"], "corr": "Consultar de inmediato", "bien": "Correcto. Los cambios importantes deben consultarse.", "mal": "La respuesta correcta es consultar de inmediato."}
    ],
    "Tercer trimestre": [
        {"q": "¿Desde qué semana inicia generalmente el tercer trimestre?", "opts": ["Semana 28", "Semana 10"], "corr": "Semana 28", "bien": "Correcto. El tercer trimestre inicia alrededor de la semana 28.", "mal": "La respuesta correcta es semana 28."},
        {"q": "¿Qué contracciones pueden aparecer como preparación del cuerpo?", "opts": ["Braxton Hicks", "Contracciones de brazo"], "corr": "Braxton Hicks", "bien": "Muy bien. Las contracciones de Braxton Hicks pueden aparecer al final del embarazo.", "mal": "La respuesta correcta es Braxton Hicks."},
        {"q": "¿Qué señal puede indicar inicio de trabajo de parto?", "opts": ["Contracciones regulares", "Hambre ocasional"], "corr": "Contracciones regulares", "bien": "Correcto. Las contracciones regulares pueden indicar trabajo de parto.", "mal": "La respuesta correcta es contracciones regulares."},
        {"q": "¿Qué debe hacerse si se rompe la fuente?", "opts": ["Acudir a atención médica", "Esperar sin avisar"], "corr": "Acudir a atención médica", "bien": "Correcto. La ruptura de fuente debe ser evaluada.", "mal": "La respuesta correcta es acudir a atención médica."},
        {"q": "¿Qué debe prepararse antes del parto?", "opts": ["Bolso para el hospital", "Maleta de vacaciones larga"], "corr": "Bolso para el hospital", "bien": "Muy bien. Tener el bolso listo ayuda a estar preparada.", "mal": "La respuesta correcta es bolso para el hospital."},
        {"q": "¿Qué señal de alarma requiere consulta urgente?", "opts": ["Visión borrosa", "Antojo de fruta"], "corr": "Visión borrosa", "bien": "Correcto. La visión borrosa puede ser una señal de alarma.", "mal": "La respuesta correcta es visión borrosa."},
        {"q": "¿Qué ayuda a reconocer el bienestar del bebé al final del embarazo?", "opts": ["Movimientos fetales", "Color de ropa"], "corr": "Movimientos fetales", "bien": "Correcto. Los movimientos fetales son una señal importante.", "mal": "La respuesta correcta es movimientos fetales."},
        {"q": "¿Qué tema conviene conversar en los controles finales?", "opts": ["Plan de parto", "Cambio de celular"], "corr": "Plan de parto", "bien": "Excelente. El plan de parto ayuda a preparar el nacimiento.", "mal": "La respuesta correcta es plan de parto."},
        {"q": "¿Qué alimento es recomendable priorizar?", "opts": ["Comidas nutritivas", "Comida en mal estado"], "corr": "Comidas nutritivas", "bien": "Correcto. Una alimentación nutritiva apoya la salud materna.", "mal": "La respuesta correcta es comidas nutritivas."},
        {"q": "¿Qué debe hacerse ante sangrado abundante?", "opts": ["Buscar ayuda urgente", "Esperar en casa"], "corr": "Buscar ayuda urgente", "bien": "Correcto. El sangrado abundante requiere atención inmediata.", "mal": "La respuesta correcta es buscar ayuda urgente."}
    ]
}

# =========================================================
# 💾 RANKING
# =========================================================

def guardar_resultado(nombre,puntos):

    try:

        db.table("ranking").insert({

            "nombre":nombre,
            "puntos":puntos,
            "correo":"sin_correo"

        }).execute()

    except Exception as e:

        st.error(f"Error ranking: {e}")

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
        "trimestre":"Primer trimestre",
        "examen":[],
        "ranking_guardado":False
    })

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

                st.session_state.examen = random.sample(
                    BANCO[trimestre],
                    10
                )

                st.session_state.fase = "test"

                st.rerun()

            else:

                st.warning("Escribe el nombre de la mamá para comenzar.")

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

        respuesta = st.radio(
            "Elige la respuesta correcta:",
            actual["opts"],
            key=f"r_{st.session_state.idx}",
            disabled=st.session_state.resp
        )

        if not st.session_state.resp:

            if st.button("CONFIRMAR"):

                correcto = (
                    respuesta == actual["corr"]
                )

                st.session_state.correcto = correcto

                if correcto:

                    st.session_state.pts += 10

                    st.session_state.fb = actual["bien"]

                else:

                    st.session_state.fb = actual["mal"]

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
            st.session_state.pts
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

    st.markdown("<h2 class='screen-title' style='font-size:1.55rem;margin-top:24px;'>Ranking global</h2>", unsafe_allow_html=True)

    try:

        ranking = db.table(
            "ranking"
        ).select(
            "nombre,puntos"
        ).order(
            "puntos",
            desc=True
        ).limit(10).execute()

        if ranking.data:

            for i,fila in enumerate(ranking.data):

                medal = "🥇"

                if i == 1:
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

    except Exception as e:

        st.error(f"Error ranking: {e}")

    if st.button("VOLVER A JUGAR"):

        st.session_state.clear()

        st.rerun()
