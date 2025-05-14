from PyQt6.QtWidgets import QWidget

class VoiceControl(QWidget):
    def __init__(self):
        super().__init__()

    def start_listening(self) -> None:
        """Iniciar escucha por voz"""
        pass

    def stop_listening(self) -> None:
        """Detener escucha por voz"""
        pass

    def process_command(self, command: str) -> None:
        """Procesar comando de voz"""
        pass