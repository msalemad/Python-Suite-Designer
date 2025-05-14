from PyQt6.QtWidgets import QLineEdit

class BasicTextField(QLineEdit):
    def __init__(self):
        super().__init__()
        # ...existing code...

class PasswordTextField(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setEchoMode(QLineEdit.EchoMode.Password)
        # ...existing code...