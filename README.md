# Vida Nueva - Cuidado Prenatal Inteligente

Aplicación educativa en Streamlit con preguntas por trimestre, retroalimentación inmediata, ranking local y panel administrativo protegido.

## Ejecutar localmente

1. Crea y activa un entorno virtual de Python.
2. Instala las dependencias con `pip install -r requirements.txt`.
3. En Windows, ejecuta `run_app.bat`. El acceso administrativo usa el secreto
   `ADMIN_PASSWORD` cuando existe o el verificador seguro de respaldo.

La aplicación se abre en `http://127.0.0.1:8501`.

## Panel administrativo

El botón **Entrar al panel administrativo** aparece en la pantalla inicial y abre
la verificación en una pestaña nueva. Después de validar la contraseña, el panel
permite consultar registros, revisar el ranking y descargar reportes en Excel,
CSV compatible con Excel y PDF. El panel usa la variable o secreto
`ADMIN_PASSWORD` cuando está configurada.

Para un despliegue en Streamlit, configura `ADMIN_PASSWORD` como secreto del servicio. No guardes contraseñas, bases de datos de participantes ni claves de Supabase en GitHub.

Puedes usar `.streamlit/secrets.toml.example` como guía de configuración, reemplazando todos los valores de ejemplo en el administrador de secretos del despliegue.

Mientras el secreto del despliegue no exista, el panel utiliza un verificador PBKDF2 de respaldo sin almacenar la contraseña original. Al configurar `ADMIN_PASSWORD`, el secreto de Streamlit reemplaza automáticamente ese acceso de respaldo.
