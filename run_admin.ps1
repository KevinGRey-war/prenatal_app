$ErrorActionPreference = "Stop"
Set-Location -LiteralPath $PSScriptRoot

$securePassword = Read-Host "Define la contraseña temporal del panel administrativo" -AsSecureString
$credential = [System.Management.Automation.PSCredential]::new("admin", $securePassword)
$plainPassword = $credential.GetNetworkCredential().Password

if ([string]::IsNullOrWhiteSpace($plainPassword)) {
    Write-Host "La contraseña no puede estar vacía." -ForegroundColor Red
    exit 1
}

$env:ADMIN_PASSWORD = $plainPassword
$env:NODE_EXE = "C:\Users\insan\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe"
$env:PDF_PYTHON_EXE = "C:\Users\insan\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"

try {
    & "$PSScriptRoot\venv\Scripts\streamlit.exe" run "$PSScriptRoot\admin_reportes.py" --server.address 127.0.0.1 --server.port 8502 --server.headless false --browser.gatherUsageStats false
}
finally {
    Remove-Item Env:ADMIN_PASSWORD -ErrorAction SilentlyContinue
    Remove-Item Env:NODE_EXE -ErrorAction SilentlyContinue
    Remove-Item Env:PDF_PYTHON_EXE -ErrorAction SilentlyContinue
    $plainPassword = $null
    $credential = $null
}
