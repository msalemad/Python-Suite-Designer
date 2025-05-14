from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QPushButton

class PluginPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.list = QListWidget(self)
        self.layout.addWidget(self.list)
        self.enable_btn = QPushButton("Activar")
        self.disable_btn = QPushButton("Desactivar")
        self.layout.addWidget(self.enable_btn)
        self.layout.addWidget(self.disable_btn)
        self.plugins = []
        self.enable_btn.clicked.connect(self.enable_selected)
        self.disable_btn.clicked.connect(self.disable_selected)

    def list_plugins(self):
        self.list.clear()
        for plugin in self.plugins:
            self.list.addItem(plugin)

    def enable_plugin(self, name: str):
        # ...lógica para activar plugin...
        pass

    def disable_plugin(self, name: str):
        # ...lógica para desactivar plugin...
        pass

    def enable_selected(self):
        item = self.list.currentItem()
        if item:
            self.enable_plugin(item.text())

    def disable_selected(self):
        item = self.list.currentItem()
        if item:
            self.disable_plugin(item.text())