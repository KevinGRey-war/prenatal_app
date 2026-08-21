$ErrorActionPreference = "Stop"
Set-Location -LiteralPath $PSScriptRoot

$env:NODE_EXE = "C:\Users\insan\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe"
$env:PDF_PYTHON_EXE = "C:\Users\insan\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"

try {
    & "$PSScriptRoot\venv\Scripts\streamlit.exe" run "$PSScriptRoot\app.py" --server.address 127.0.0.1 --server.port 8501 --server.headless false --browser.gatherUsageStats false
}
finally {
    Remove-Item Env:NODE_EXE -ErrorAction SilentlyContinue
    Remove-Item Env:PDF_PYTHON_EXE -ErrorAction SilentlyContinue
}
