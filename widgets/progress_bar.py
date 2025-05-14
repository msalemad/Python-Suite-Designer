from PyQt6.QtWidgets import QProgressBar

class BasicProgressBar(QProgressBar):
    def __init__(self):
        super().__init__()
        # Initialize the basic progress bar
        self.setMinimum(0)
        self.setMaximum(100)
        self.setValue(0)

class CircularProgressBar(QProgressBar):
    def __init__(self):
        super().__init__()
        # Initialize the circular progress bar
        self.setMinimum(0)
        self.setMaximum(100)
        self.setValue(0)
        self.setTextVisible(False)
        self.setStyleSheet("""
            QProgressBar {
                border: 2px solid grey;
                border-radius: 5px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #05B8CC;
                width: 20px;
            }
        """)