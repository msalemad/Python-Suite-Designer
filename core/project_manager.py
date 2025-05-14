import json
import os
from typing import Any, Optional

class ProjectManager:
    def __init__(self):
        self.current_project: dict = {}
        self.current_path: Optional[str] = None

    def new_project(self) -> None:
        self.current_project = {
            "name": "Nuevo Proyecto",
            "widgets": [],
            "theme": "default"
        }
        self.current_path = None

    def open_project(self, path: str) -> None:
        if not os.path.exists(path):
            raise FileNotFoundError(f"No existe el archivo: {path}")
        with open(path, "r", encoding="utf-8") as f:
            self.current_project = json.load(f)
        self.current_path = path

    def save_project(self, path: str = "") -> None:
        if not path:
            if not self.current_path:
                raise ValueError("No se ha especificado ruta para guardar el proyecto.")
            path = self.current_path
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.current_project, f, indent=2, ensure_ascii=False)
        self.current_path = path

    def export_project(self, format: str, path: str) -> None:
        # Por ahora solo soporta exportación a JSON
        if format == "json":
            self.save_project(path)
        else:
            raise NotImplementedError(f"Exportación a formato {format} no implementada.")

    def import_project(self, path: str) -> None:
        self.open_project(path)

    def generate_requirements(self) -> str:
        # Retorna un requirements.txt básico
        return "PyQt6\nPyInstaller\nGitPython\nwatchdog\njinja2\njsonschema\n"

    def generate_modular_structure(self) -> None:
        # Crea carpetas base si no existen
        for folder in ["core", "ui", "widgets", "plugins", "themes", "examples", "assets", "docs", "tests"]:
            os.makedirs(folder, exist_ok=True)

    def generate_documentation(self) -> None:
        # Genera un archivo docs/auto_doc.md con la estructura del proyecto
        doc = f"# Documentación automática de {self.current_project.get('name','Proyecto')}\n"
        doc += f"## Widgets:\n"
        for w in self.current_project.get("widgets", []):
            doc += f"- {w.get('type','widget')}\n"
        with open("docs/auto_doc.md", "w", encoding="utf-8") as f:
            f.write(doc)

    def load_assets(self, path: str) -> None:
        # Placeholder: cargar assets desde carpeta
        pass
