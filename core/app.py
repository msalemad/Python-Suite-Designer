from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow

class PythonSuiteDesignerApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.setApplicationName("Python Suite Designer")
        self.main_window = MainWindow()
        self.main_window.show()
