from PyQt6.QtWidgets import QWidget

class AnimationPanel(QWidget):
    def __init__(self):
        super().__init__()

    def set_target(self, widget) -> None:
        """Seleccionar widget a animar"""
        pass

    def add_animation(self, animation_type: str) -> None:
        """Agregar animación"""
        pass

    def remove_animation(self, animation_id: str) -> None:
        """Eliminar animación"""
        pass