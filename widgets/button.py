from PyQt6.QtWidgets import QPushButton

class BasicButton(QPushButton):
    def __init__(self, text="Botón"):
        super().__init__(text)

class FlatButton(QPushButton):
    def __init__(self, text="Botón plano"):
        super().__init__(text)

class IconButton(QPushButton):
    def __init__(self, icon=None, text=""):
        super().__init__(text)