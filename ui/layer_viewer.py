from PyQt6.QtWidgets import QWidget

class LayerViewer(QWidget):
    def __init__(self):
        super().__init__()

    def set_layers(self, layers: list) -> None:
        """Establecer lista de capas"""
        pass

    def move_layer(self, from_index: int, to_index: int) -> None:
        """Mover capa"""
        pass