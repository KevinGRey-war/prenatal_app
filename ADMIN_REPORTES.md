# Panel administrativo de registros y ranking

El panel puede abrirse desde el botón administrativo de la pantalla inicial o ejecutarse como una aplicación separada. En ambos casos exige contraseña; la ejecución independiente utiliza el puerto local `8502` y solo escucha conexiones desde la misma computadora (`127.0.0.1`).

## Iniciar el panel

Desde el aplicativo principal, pulsa **Entrar al panel administrativo** e ingresa la contraseña definida al iniciar `run_app.bat`.

Para ejecutarlo por separado:

1. Ejecuta `run_admin.bat`.
2. Define una contraseña temporal cuando PowerShell la solicite.
3. Abre `http://localhost:8502` si el navegador no se abre automáticamente.
4. Ingresa la misma contraseña en la pantalla de acceso.

La contraseña solo vive mientras el proceso está en ejecución; no se guarda en archivos del proyecto.

## Consultas y descargas

El panel permite:

- buscar participantes por nombre;
- filtrar por trimestre y rango de puntaje;
- consultar todos los intentos registrados;
- revisar el ranking con el mejor puntaje de cada participante;
- descargar el resultado filtrado en Excel (`.xlsx`) y PDF (`.pdf`).

Los datos se leen de `ranking.db`. El panel no modifica ni elimina los registros.

## Privacidad

Los reportes contienen información de participantes. Mantén el panel protegido, no compartas la contraseña y entrega los archivos únicamente a personal autorizado.
