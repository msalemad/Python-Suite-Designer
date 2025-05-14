from PyQt6.QtWidgets import QProgressBar

class VerticalProgressBar(QProgressBar):
    def __init__(self):
        super().__init__()
        self.setOrientation(1)  # Qt.Vertical, pero como int para compatibilidad

class GradientProgressBar(QProgressBar):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("QProgressBar::chunk { background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #0078d7, stop:1 #00cfff); }")
