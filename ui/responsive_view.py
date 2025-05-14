from PyQt6.QtWidgets import QWidget

class ResponsiveView(QWidget):
    def __init__(self):
        super().__init__()

    def set_mode(self, mode: str) -> None:
        """Cambiar modo de vista (móvil, tablet, escritorio)"""
        pass