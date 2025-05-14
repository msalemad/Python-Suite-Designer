from PyQt6.QtWidgets import QWidget

class LanguageSelector(QWidget):
    def __init__(self):
        super().__init__()

    def set_language(self, lang_code: str) -> None:
        """Cambiar idioma"""
        pass

    def get_available_languages(self) -> list:
        """Listar idiomas disponibles"""
        pass