from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame
from PyQt6.QtCore import Qt, QMimeData
from PyQt6.QtGui import QDragEnterEvent, QDropEvent

class CanvasWidget(QFrame):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.setFrameStyle(QFrame.Shape.StyledPanel | QFrame.Shadow.Raised)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(QLabel("Lienzo de diseño visual"))
        # ...puedes mejorar el layout para soporte absoluto o grid...

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasFormat("application/x-widget-class"):
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        widget_class = event.mimeData().data("application/x-widget-class")
        if widget_class:
            # Instancia el widget y lo añade al layout
            cls = eval(widget_class.data().decode())
            widget = cls()
            self.layout.addWidget(widget)
            event.acceptProposedAction()
