from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton

class LogPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.text = QTextEdit(self)
        self.text.setReadOnly(True)
        self.layout.addWidget(self.text)
        self.clear_btn = QPushButton("Limpiar logs")
        self.clear_btn.clicked.connect(self.clear_logs)
        self.layout.addWidget(self.clear_btn)

    def add_log(self, message: str) -> None:
        self.text.append(message)

    def clear_logs(self) -> None:
        self.text.clear()

    def list_logs(self) -> list:
        return self.text.toPlainText().splitlines()