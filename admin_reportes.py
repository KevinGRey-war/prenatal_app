"""Panel administrativo independiente para registros y ranking prenatal."""

import json
import os
import sqlite3
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path

import pandas as pd
import streamlit as st

from admin_auth import (
    clave_administrativa_valida,
    obtener_clave_administrativa,
)


BASE_DIR = Path(__file__).resolve().parent
RANKING_DB_PATH = Path(
    os.getenv("RANKING_DB_PATH", str(BASE_DIR / "ranking.db"))
)
EXPORT_DIR = BASE_DIR / "admin_exports"

NODE_EXE = os.getenv(
    "NODE_EXE",
    r"C:\Users\insan\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe",
)
PDF_PYTHON_EXE = os.getenv(
    "PDF_PYTHON_EXE",
    sys.executable,
)

st.set_page_config(
    page_title="Administración - Vida Nueva",
    page_icon="🔐",
    layout="wide",
)

st.markdown(
    """
    <style>
    :root {
        --ink: #24324B;
        --muted: #697386;
        --pink: #EC4899;
        --gold: #C9A227;
        --line: #E8DFF0;
        --admin-red: #C62828;
        --admin-red-dark: #991B1B;
        --admin-red-soft: #FFF1F2;
    }
    .stApp {
        background: linear-gradient(135deg, #FFF8FC 0%, #F7FBFF 52%, #F9F5FF 100%);
        color: var(--ink);
    }
    header, #MainMenu, footer { visibility: hidden; }
    .block-container { max-width: 1220px; padding-top: 1.5rem; }
    .admin-header {
        padding: 24px 28px;
        border: 1px solid var(--line);
        border-top: 5px solid var(--admin-red);
        border-radius: 24px;
        background: rgba(255, 255, 255, 0.92);
        box-shadow: 0 16px 38px rgba(75, 45, 90, 0.10);
        margin-bottom: 16px;
    }
    .admin-header h1 { margin: 0; color: var(--ink); font-size: 2rem; }
    .admin-header p { margin: 8px 0 0; color: var(--muted); font-weight: 600; }
    [data-testid="stMetric"] {
        border: 1px solid var(--line);
        border-radius: 18px;
        padding: 14px 16px;
        background: white;
        box-shadow: 0 8px 24px rgba(36, 50, 75, 0.06);
    }
    [data-testid="stMetricValue"] { color: var(--pink); }
    div.stDownloadButton > button, div.stButton > button,
    div.stFormSubmitButton > button {
        min-height: 48px;
        border-radius: 14px;
        font-weight: 800;
    }
    div.stButton > button {
        background: #FFFFFF !important;
        color: var(--admin-red-dark) !important;
        border: 1.5px solid #FCA5A5 !important;
        box-shadow: 0 5px 15px rgba(153, 27, 27, 0.08);
    }
    div.stButton > button:hover {
        background: var(--admin-red-soft) !important;
        color: var(--admin-red-dark) !important;
        border-color: var(--admin-red) !important;
    }
    div.stFormSubmitButton > button,
    div.stDownloadButton > button {
        background: linear-gradient(135deg, #DC2626, #B91C1C) !important;
        color: #FFFFFF !important;
        border: 0 !important;
        box-shadow: 0 9px 22px rgba(185, 28, 28, 0.20);
    }
    div.stFormSubmitButton > button:hover,
    div.stDownloadButton > button:hover {
        background: linear-gradient(135deg, #B91C1C, #991B1B) !important;
        color: #FFFFFF !important;
    }
    [data-testid="stTextInput"] [data-baseweb="input"] {
        background: #FFFFFF !important;
        border: 1.5px solid #FCA5A5 !important;
        border-radius: 13px !important;
    }
    [data-testid="stTextInput"] input {
        background: #FFFFFF !important;
        color: var(--ink) !important;
        -webkit-text-fill-color: var(--ink) !important;
    }
    [data-testid="stTextInput"] input::placeholder {
        color: #9CA3AF !important;
        -webkit-text-fill-color: #9CA3AF !important;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        border-bottom: 1px solid #FECACA;
    }
    .stTabs [data-baseweb="tab"] {
        min-height: 50px;
        padding: 0 18px;
        border-radius: 13px 13px 0 0;
        background: var(--admin-red-soft);
        border: 1px solid #FECACA;
        border-bottom: 0;
    }
    .stTabs [data-baseweb="tab"] p {
        color: var(--admin-red) !important;
        font-weight: 800 !important;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background: #FFFFFF !important;
        box-shadow: 0 -5px 16px rgba(185, 28, 28, 0.08);
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] p {
        color: var(--admin-red-dark) !important;
        text-decoration: underline;
        text-decoration-color: var(--admin-red);
        text-decoration-thickness: 3px;
        text-underline-offset: 8px;
    }
    .stTabs [data-baseweb="tab-highlight"] {
        height: 3px;
        background-color: var(--admin-red) !important;
    }
    .privacy-note {
        padding: 12px 15px;
        border-left: 5px solid var(--gold);
        border-radius: 12px;
        background: #FFF9E8;
        color: #6B4F00;
        font-weight: 650;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def exigir_autenticacion():
    """Detiene el panel hasta validar la contraseña del proceso."""

    clave_configurada = obtener_clave_administrativa()

    if os.getenv("ADMIN_EMBEDDED") == "1":
        if st.button(
            "← VOLVER AL APLICATIVO",
            key="volver_desde_acceso_admin",
            width="content",
        ):
            st.switch_page("app.py")

    if st.session_state.get("admin_autenticado"):
        return

    acceso = st.empty()
    autenticacion_exitosa = False

    with acceso.container():
        _, columna_acceso, _ = st.columns([1, 1.7, 1])

        with columna_acceso:
            st.markdown(
                """
                <div class="admin-header" style="text-align:center">
                    <h1>🔐 Acceso administrativo</h1>
                    <p>Verifica la contraseña para consultar registros, ranking y reportes.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

            with st.form("acceso_admin", clear_on_submit=True):
                clave_ingresada = st.text_input(
                    "Contraseña de administración",
                    type="password",
                    placeholder="Ingresa la contraseña administrativa",
                )
                ingresar = st.form_submit_button(
                    "VERIFICAR Y ENTRAR",
                    width="stretch",
                )

            if ingresar:
                if clave_administrativa_valida(
                    clave_ingresada,
                    clave_configurada,
                ):
                    st.session_state.admin_autenticado = True
                    autenticacion_exitosa = True
                else:
                    st.error(
                        "Contraseña incorrecta. El acceso permanece bloqueado."
                    )

    if autenticacion_exitosa:
        acceso.empty()
        return

    st.stop()


@st.cache_data(ttl=10, show_spinner=False)
def cargar_registros_locales(ruta_db):
    """Lee todos los intentos sin alterar la base de datos original."""

    ruta = Path(ruta_db)

    if not ruta.exists():
        return pd.DataFrame(
            columns=[
                "ID",
                "Usuario",
                "Puntaje",
                "Trimestre",
                "Fecha",
                "Origen",
            ]
        )

    conexion = sqlite3.connect(str(ruta), timeout=10)

    try:
        datos = pd.read_sql_query(
            """
            SELECT
                id AS ID,
                nombre AS Usuario,
                puntos AS Puntaje,
                trimestre AS Trimestre,
                creado_en AS Fecha
            FROM ranking
            ORDER BY creado_en DESC, id DESC
            """,
            conexion,
        )
    finally:
        conexion.close()

    datos["Puntaje"] = pd.to_numeric(datos["Puntaje"], errors="coerce").fillna(0).astype(int)
    datos["Fecha"] = pd.to_datetime(datos["Fecha"], errors="coerce")
    datos["Origen"] = "Base local"

    return datos


def construir_ranking(registros):
    """Conserva el mejor puntaje de cada usuario y asigna posiciones."""

    if registros.empty:
        return pd.DataFrame(
            columns=["Posición", "Usuario", "Mejor puntaje", "Trimestre", "Fecha"]
        )

    ranking = registros.copy()
    ranking["_usuario_clave"] = ranking["Usuario"].astype(str).str.strip().str.casefold()
    ranking = ranking.sort_values(
        ["Puntaje", "Fecha", "Usuario"],
        ascending=[False, True, True],
        na_position="last",
    )
    ranking = ranking.drop_duplicates("_usuario_clave", keep="first")
    ranking = ranking.reset_index(drop=True)
    ranking.insert(0, "Posición", range(1, len(ranking) + 1))
    ranking = ranking.rename(columns={"Puntaje": "Mejor puntaje"})

    return ranking[["Posición", "Usuario", "Mejor puntaje", "Trimestre", "Fecha"]]


def serializar_fecha(valor):
    if pd.isna(valor):
        return ""
    return pd.Timestamp(valor).strftime("%Y-%m-%d %H:%M")


def construir_payload(registros, ranking, filtros):
    puntajes = registros["Puntaje"] if not registros.empty else pd.Series(dtype=float)

    resumen = {
        "total_registros": int(len(registros)),
        "usuarios_unicos": int(registros["Usuario"].nunique()) if not registros.empty else 0,
        "puntaje_promedio": round(float(puntajes.mean()), 1) if not registros.empty else 0,
        "puntaje_maximo": int(puntajes.max()) if not registros.empty else 0,
    }

    registros_exportar = []

    for posicion, (_, fila) in enumerate(
        registros.sort_values(
            ["Puntaje", "Fecha"],
            ascending=[False, True],
            na_position="last",
        ).iterrows(),
        start=1,
    ):
        registros_exportar.append(
            {
                "posicion": posicion,
                "usuario": str(fila["Usuario"]),
                "puntaje": int(fila["Puntaje"]),
                "trimestre": str(fila["Trimestre"]),
                "fecha": serializar_fecha(fila["Fecha"]),
                "origen": str(fila["Origen"]),
            }
        )

    ranking_exportar = [
        {
            "posicion": int(fila["Posición"]),
            "usuario": str(fila["Usuario"]),
            "puntaje": int(fila["Mejor puntaje"]),
            "trimestre": str(fila["Trimestre"]),
            "fecha": serializar_fecha(fila["Fecha"]),
        }
        for _, fila in ranking.iterrows()
    ]

    return {
        "generado_en": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "filtros": filtros,
        "resumen": resumen,
        "registros": registros_exportar,
        "ranking": ranking_exportar,
    }


@st.cache_data(show_spinner=False)
def generar_reporte(formato, payload_json):
    """Ejecuta los generadores aislados y devuelve los bytes descargables."""

    payload = json.loads(payload_json)

    with tempfile.TemporaryDirectory(prefix="prenatal-reportes-") as carpeta:
        carpeta_temporal = Path(carpeta)
        entrada = carpeta_temporal / "datos.json"
        entrada.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

        if formato == "xlsx":
            salida = carpeta_temporal / "registro_usuarios_ranking.xlsx"
            comando = [
                NODE_EXE,
                str(EXPORT_DIR / "generar_excel.mjs"),
                str(entrada),
                str(salida),
            ]
        elif formato == "pdf":
            salida = carpeta_temporal / "registro_usuarios_ranking.pdf"
            comando = [
                PDF_PYTHON_EXE,
                str(EXPORT_DIR / "generar_pdf.py"),
                str(entrada),
                str(salida),
            ]
        else:
            raise ValueError("Formato de reporte no compatible")

        resultado = subprocess.run(
            comando,
            cwd=str(BASE_DIR),
            capture_output=True,
            text=True,
            timeout=60,
            check=False,
        )

        if resultado.returncode != 0 or not salida.exists():
            detalle = (resultado.stderr or resultado.stdout or "").strip()
            raise RuntimeError(
                "No se pudo generar el reporte. "
                + (detalle[-500:] if detalle else "Revisa las dependencias del panel.")
            )

        return salida.read_bytes()


exigir_autenticacion()

st.markdown(
    """
    <div class="admin-header">
        <h1>Registros y ranking de usuarios</h1>
        <p>Consulta administrativa independiente de la experiencia prenatal.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="privacy-note">
        Uso administrativo: protege los archivos descargados y evita compartir
        información de participantes sin autorización.
    </div>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.subheader("Control del panel")
    st.caption(f"Fuente: {RANKING_DB_PATH.name}")

    if os.getenv("ADMIN_EMBEDDED") == "1":
        if st.button("VOLVER AL APLICATIVO", width="stretch"):
            st.switch_page("app.py")

    if st.button("ACTUALIZAR REGISTROS", width="stretch"):
        cargar_registros_locales.clear()
        generar_reporte.clear()
        st.rerun()

    if st.button("CERRAR SESIÓN", width="stretch"):
        st.session_state.admin_autenticado = False
        st.rerun()


registros = cargar_registros_locales(str(RANKING_DB_PATH))

if registros.empty:
    st.info("Todavía no existen resultados guardados.")
    st.stop()

f1, f2, f3 = st.columns([1.4, 1.2, 1.2])

with f1:
    buscar = st.text_input("Buscar usuario", placeholder="Nombre o parte del nombre")

with f2:
    opciones_trimestre = sorted(registros["Trimestre"].dropna().astype(str).unique())
    trimestres = st.multiselect(
        "Trimestre",
        opciones_trimestre,
        default=opciones_trimestre,
    )

with f3:
    puntaje_minimo, puntaje_maximo = st.slider(
        "Rango de puntaje",
        min_value=0,
        max_value=100,
        value=(0, 100),
        step=10,
    )

filtrados = registros.copy()

if buscar.strip():
    filtrados = filtrados[
        filtrados["Usuario"].astype(str).str.contains(
            buscar.strip(),
            case=False,
            na=False,
            regex=False,
        )
    ]

filtrados = filtrados[
    filtrados["Trimestre"].astype(str).isin(trimestres)
    & filtrados["Puntaje"].between(puntaje_minimo, puntaje_maximo)
]

ranking = construir_ranking(filtrados)

m1, m2, m3, m4 = st.columns(4)
m1.metric("Registros", len(filtrados))
m2.metric("Usuarios", filtrados["Usuario"].nunique())
m3.metric(
    "Promedio",
    f"{filtrados['Puntaje'].mean():.1f} pts" if not filtrados.empty else "0 pts",
)
m4.metric(
    "Mejor puntaje",
    f"{int(filtrados['Puntaje'].max())} pts" if not filtrados.empty else "0 pts",
)

tab_registros, tab_ranking, tab_descargas = st.tabs(
    ["Todos los registros", "Ranking", "Descargar reportes"]
)

with tab_registros:
    tabla_registros = filtrados.copy()
    tabla_registros["Fecha"] = tabla_registros["Fecha"].dt.strftime("%Y-%m-%d %H:%M")
    st.dataframe(
        tabla_registros,
        width="stretch",
        hide_index=True,
        column_config={
            "Puntaje": st.column_config.ProgressColumn(
                "Puntaje",
                min_value=0,
                max_value=100,
                format="%d pts",
            )
        },
    )

with tab_ranking:
    tabla_ranking = ranking.copy()
    tabla_ranking["Fecha"] = tabla_ranking["Fecha"].apply(serializar_fecha)
    st.dataframe(
        tabla_ranking,
        width="stretch",
        hide_index=True,
        column_config={
            "Mejor puntaje": st.column_config.ProgressColumn(
                "Mejor puntaje",
                min_value=0,
                max_value=100,
                format="%d pts",
            )
        },
    )

with tab_descargas:
    filtros = {
        "usuario": buscar.strip() or "Todos",
        "trimestres": ", ".join(trimestres) if trimestres else "Ninguno",
        "puntaje": f"{puntaje_minimo} a {puntaje_maximo}",
    }
    payload = construir_payload(filtrados, ranking, filtros)
    payload_json = json.dumps(payload, ensure_ascii=False, sort_keys=True)

    if filtrados.empty:
        st.warning("No hay datos que coincidan con los filtros seleccionados.")
    else:
        st.caption(
            "Prepara únicamente el formato que necesites. El panel no genera "
            "archivos automáticamente al abrirse."
        )
        d1, d2 = st.columns(2)

        with d1:
            if st.button(
                "PREPARAR EXCEL",
                key="preparar_reporte_excel",
                width="stretch",
            ):
                try:
                    with st.spinner("Preparando el archivo Excel..."):
                        datos_excel = generar_reporte("xlsx", payload_json)

                    st.session_state.reporte_excel = {
                        "payload": payload_json,
                        "datos": datos_excel,
                    }
                except Exception:
                    st.session_state.pop("reporte_excel", None)
                    st.error(
                        "No se pudo preparar Excel en este servidor. "
                        "Puedes descargar los mismos registros en CSV, "
                        "compatible con Excel."
                    )

            reporte_excel = st.session_state.get("reporte_excel", {})

            if reporte_excel.get("payload") == payload_json:
                st.download_button(
                    "DESCARGAR EXCEL",
                    data=reporte_excel["datos"],
                    file_name="registro_usuarios_ranking.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    width="stretch",
                )

            csv_excel = filtrados.copy()
            csv_excel["Fecha"] = csv_excel["Fecha"].apply(serializar_fecha)
            st.download_button(
                "DESCARGAR DATOS PARA EXCEL (.CSV)",
                data=csv_excel.to_csv(index=False).encode("utf-8-sig"),
                file_name="registro_usuarios_ranking.csv",
                mime="text/csv",
                width="stretch",
            )

        with d2:
            if st.button(
                "PREPARAR PDF",
                key="preparar_reporte_pdf",
                width="stretch",
            ):
                try:
                    with st.spinner("Preparando el archivo PDF..."):
                        datos_pdf = generar_reporte("pdf", payload_json)

                    st.session_state.reporte_pdf = {
                        "payload": payload_json,
                        "datos": datos_pdf,
                    }
                except Exception:
                    st.session_state.pop("reporte_pdf", None)
                    st.error(
                        "No se pudo preparar el PDF en este servidor. "
                        "Inténtalo nuevamente o actualiza los registros."
                    )

            reporte_pdf = st.session_state.get("reporte_pdf", {})

            if reporte_pdf.get("payload") == payload_json:
                st.download_button(
                    "DESCARGAR PDF",
                    data=reporte_pdf["datos"],
                    file_name="registro_usuarios_ranking.pdf",
                    mime="application/pdf",
                    width="stretch",
                )
