"""Entrada multipágina al panel administrativo protegido."""

import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
ADMIN_SCRIPT = BASE_DIR / "admin_reportes.py"

# Permite que el panel muestre el regreso al aplicativo principal.
os.environ["ADMIN_EMBEDDED"] = "1"

namespace = {
    "__name__": "__main__",
    "__file__": str(ADMIN_SCRIPT),
}
exec(
    compile(ADMIN_SCRIPT.read_text(encoding="utf-8"), str(ADMIN_SCRIPT), "exec"),
    namespace,
)
