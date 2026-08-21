"""Autenticación compartida por el aplicativo y el panel administrativo."""

import hashlib
import hmac
import os

import streamlit as st


# Verificador seguro de respaldo para Streamlit Cloud.
# La contraseña original no forma parte del repositorio.
FALLBACK_ADMIN_SALT = "9bd16485b62e60f1dc3b962d2ba900297069"
FALLBACK_ADMIN_HASH = "2403935a6daedd6848a6ebf62212c4dd6540ff83069b9b231ae80c00fe545f8b"
FALLBACK_ADMIN_ITERATIONS = 390000


def obtener_clave_administrativa():
    """Obtiene primero el secreto privado del entorno o de Streamlit."""

    clave = os.getenv("ADMIN_PASSWORD", "").strip()

    if clave:
        return clave

    try:
        return str(st.secrets.get("ADMIN_PASSWORD", "")).strip()
    except (FileNotFoundError, KeyError, TypeError):
        return ""


def clave_administrativa_valida(clave_ingresada, clave_configurada=None):
    """Valida el secreto privado o el verificador PBKDF2 de respaldo."""

    clave_configurada = (
        obtener_clave_administrativa()
        if clave_configurada is None
        else clave_configurada
    )

    if clave_configurada:
        return hmac.compare_digest(clave_ingresada, clave_configurada)

    derivada = hashlib.pbkdf2_hmac(
        "sha256",
        clave_ingresada.encode("utf-8"),
        bytes.fromhex(FALLBACK_ADMIN_SALT),
        FALLBACK_ADMIN_ITERATIONS,
    ).hex()

    return hmac.compare_digest(derivada, FALLBACK_ADMIN_HASH)
