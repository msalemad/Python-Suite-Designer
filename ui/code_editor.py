from PyQt6.QtWidgets import QWidget

class CodeEditor(QWidget):
    def __init__(self):
        super().__init__()
        # ...existing code...

    def load_code(self, code: str) -> None:
        """Cargar código en el editor"""
        pass

    def get_code(self) -> str:
        """Obtener código actual"""
        pass

    def set_read_only(self, value: bool) -> None:
        """Establecer modo solo lectura"""
        pass