$ErrorActionPreference = "Stop"
Set-Location -LiteralPath $PSScriptRoot

$previousAdminPassword = $env:ADMIN_PASSWORD

if ([string]::IsNullOrWhiteSpace($previousAdminPassword)) {
    $securePassword = Read-Host "Define la contraseña temporal del panel administrativo" -AsSecureString
    $credential = [System.Management.Automation.PSCredential]::new("admin", $securePassword)
    $plainPassword = $credential.GetNetworkCredential().Password

    if ([string]::IsNullOrWhiteSpace($plainPassword)) {
        Write-Host "La contraseña no puede estar vacía." -ForegroundColor Red
        exit 1
    }

    $env:ADMIN_PASSWORD = $plainPassword
}

$env:NODE_EXE = "C:\Users\insan\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe"
$env:PDF_PYTHON_EXE = "C:\Users\insan\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"

try {
    & "$PSScriptRoot\venv\Scripts\streamlit.exe" run "$PSScriptRoot\app.py" --server.address 127.0.0.1 --server.port 8501 --server.headless false --browser.gatherUsageStats false
}
finally {
    if ([string]::IsNullOrWhiteSpace($previousAdminPassword)) {
        Remove-Item Env:ADMIN_PASSWORD -ErrorAction SilentlyContinue
    }
    else {
        $env:ADMIN_PASSWORD = $previousAdminPassword
    }

    Remove-Item Env:NODE_EXE -ErrorAction SilentlyContinue
    Remove-Item Env:PDF_PYTHON_EXE -ErrorAction SilentlyContinue
    $plainPassword = $null
    $credential = $null
}
