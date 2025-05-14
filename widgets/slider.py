from PyQt6.QtWidgets import QSlider

class BasicSlider(QSlider):
    def __init__(self, orientation):
        super().__init__(orientation)
        self.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.setTickInterval(10)
        self.setSingleStep(1)

class StyledSlider(QSlider):
    def __init__(self, orientation):
        super().__init__(orientation)
        self.setStyleSheet("""
            QSlider::groove:horizontal {
                border: 1px solid #999999;
                height: 8px;
                background: #b0b0b0;
                margin: 2px 0;
            }
            QSlider::handle:horizontal {
                background: #5c5c5c;
                border: 1px solid #5c5c5c;
                width: 18px;
                margin: -2px 0;
                border-radius: 3px;
            }
        """)