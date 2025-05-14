from PyQt6.QtWidgets import QPushButton

class RoundedButton(QPushButton):
    def __init__(self, text="Botón redondeado"):
        super().__init__(text)
        self.setStyleSheet("border-radius: 16px;")

class GhostButton(QPushButton):
    def __init__(self, text="Botón ghost"):
        super().__init__(text)
        self.setStyleSheet("background: transparent; border: 1px solid #888; color: #888;")

class OutlineButton(QPushButton):
    def __init__(self, text="Botón outline"):
        super().__init__(text)
        self.setStyleSheet("background: none; border: 2px solid #0078d7; color: #0078d7;")

class ToggleButton(QPushButton):
    def __init__(self, text="Botón toggle"):
        super().__init__(text)
        self.setCheckable(True)
        self.setText(text)

class FloatingButton(QPushButton):
    def __init__(self, text="Botón flotante"):
        super().__init__(text)
        self.setStyleSheet("border-radius: 24px; background: #0078d7; color: white; min-width: 48px; min-height: 48px;")
