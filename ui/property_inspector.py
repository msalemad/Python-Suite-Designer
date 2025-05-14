from PyQt6.QtWidgets import QWidget, QFormLayout, QLineEdit, QLabel

class PropertyInspector(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QFormLayout(self)
        self.target = None

    def set_target(self, widget) -> None:
        self.target = widget
        self.update_properties()

    def update_properties(self) -> None:
        self.clear()
        if self.target:
            self.layout.addRow("Clase", QLabel(self.target.__class__.__name__))
            if hasattr(self.target, "text"):
                text_edit = QLineEdit(self.target.text())
                text_edit.editingFinished.connect(lambda: self.target.setText(text_edit.text()))
                self.layout.addRow("Texto", text_edit)
            # ...agrega más propiedades editables según el tipo de widget...

    def clear(self):
        while self.layout.rowCount():
            self.layout.removeRow(0)