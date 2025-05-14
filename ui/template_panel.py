from PyQt6.QtWidgets import QWidget

class TemplatePanel(QWidget):
    def __init__(self):
        super().__init__()

    def list_templates(self) -> list:
        """Listar templates disponibles"""
        pass

    def apply_template(self, template_name: str) -> None:
        """Aplicar template seleccionado"""
        pass