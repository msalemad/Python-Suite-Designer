from PyQt6.QtWidgets import QSlider
from PyQt6.QtCore import Qt

class VerticalSlider(QSlider):
    def __init__(self):
        super().__init__(Qt.Orientation.Vertical)

class RangeSlider(QSlider):
    def __init__(self):
        super().__init__(Qt.Orientation.Horizontal)
        # Placeholder: para un range real, se requiere implementación personalizada

class ColoredSlider(QSlider):
    def __init__(self):
        super().__init__(Qt.Orientation.Horizontal)
        self.setStyleSheet("QSlider::groove:horizontal { background: #0078d7; height: 8px; }")
