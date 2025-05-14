from PyQt6.QtWidgets import QWidget

class NavigationPanel(QWidget):
    def __init__(self):
        super().__init__()
        # ...existing code...

    def add_page(self, name: str) -> None:
        """Agregar página"""
        pass

    def remove_page(self, name: str) -> None:
        """Eliminar página"""
        pass

    def navigate_to(self, name: str) -> None:
        """Navegar a página"""
        pass