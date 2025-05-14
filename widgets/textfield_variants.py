from PyQt6.QtWidgets import QLineEdit

class MultilineTextField(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setPlaceholderText("Multilínea (simulado, usar QTextEdit para real)")

class DisabledTextField(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setDisabled(True)
        self.setPlaceholderText("Deshabilitado")

class ReadOnlyTextField(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setReadOnly(True)
        self.setPlaceholderText("Solo lectura")
