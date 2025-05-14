from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QPushButton

class HistoryPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.list = QListWidget(self)
        self.layout.addWidget(self.list)
        self.undo_btn = QPushButton("Deshacer")
        self.redo_btn = QPushButton("Rehacer")
        self.layout.addWidget(self.undo_btn)
        self.layout.addWidget(self.redo_btn)
        self.history = []
        self.redo_stack = []
        self.undo_btn.clicked.connect(self.undo)
        self.redo_btn.clicked.connect(self.redo)

    def add_action(self, description: str, state):
        self.history.append((description, state))
        self.list.addItem(description)
        self.redo_stack.clear()

    def undo(self):
        if self.history:
            desc, state = self.history.pop()
            self.redo_stack.append((desc, state))
            self.list.takeItem(self.list.count() - 1)
            # ...restaurar el estado anterior...

    def redo(self):
        if self.redo_stack:
            desc, state = self.redo_stack.pop()
            self.history.append((desc, state))
            self.list.addItem(desc)
            # ...aplicar el estado de redo...

    def list_history(self) -> list:
        return [self.list.item(i).text() for i in range(self.list.count())]