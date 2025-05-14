from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QListWidget, QListWidgetItem
from widgets import (
    BasicButton, FlatButton, IconButton,
    RoundedButton, GhostButton, OutlineButton, ToggleButton, FloatingButton,
    BasicSlider, StyledSlider,
    VerticalSlider, RangeSlider, ColoredSlider,
    BasicProgressBar, CircularProgressBar,
    VerticalProgressBar, GradientProgressBar,
    BasicTextField, PasswordTextField,
    MultilineTextField, DisabledTextField, ReadOnlyTextField,
    # ...agrega aquí más variantes reales...
)

class ToolboxWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Buscar widget:"))
        self.search = QLineEdit(self)
        layout.addWidget(self.search)
        self.widget_list = QListWidget(self)
        layout.addWidget(self.widget_list)
        self.all_widgets = self.get_all_widgets()
        self.populate_list(self.all_widgets)
        self.search.textChanged.connect(self.filter_widgets)

    def get_all_widgets(self):
        widget_types = [
            # Botones y variantes reales
            ("Botón básico", BasicButton),
            ("Botón plano", FlatButton),
            ("Botón con ícono", IconButton),
            ("Botón redondeado", RoundedButton),
            ("Botón ghost", GhostButton),
            ("Botón outline", OutlineButton),
            ("Botón toggle", ToggleButton),
            ("Botón flotante", FloatingButton),
            # Sliders y variantes reales
            ("Slider básico", BasicSlider),
            ("Slider estilizado", StyledSlider),
            ("Slider vertical", VerticalSlider),
            ("Slider de rango", RangeSlider),
            ("Slider de color", ColoredSlider),
            # ProgressBar y variantes reales
            ("Barra de progreso", BasicProgressBar),
            ("Barra de progreso circular", CircularProgressBar),
            ("Barra de progreso vertical", VerticalProgressBar),
            ("Barra de progreso gradiente", GradientProgressBar),
            # Campos de texto y variantes reales
            ("Campo de texto", BasicTextField),
            ("Campo de contraseña", PasswordTextField),
            ("Campo de texto multilinea", MultilineTextField),
            ("Campo de texto deshabilitado", DisabledTextField),
            ("Campo de texto solo lectura", ReadOnlyTextField),
            # ...agrega aquí más widgets y variantes reales...
        ]
        print(f"Widgets reales definidos: {len(widget_types)}")
        return widget_types

    def populate_list(self, widget_defs):
        self.widget_list.clear()
        for name, cls in widget_defs:
            item = QListWidgetItem(name)
            item.setData(1000, cls)
            self.widget_list.addItem(item)

    def filter_widgets(self, text):
        filtered = [w for w in self.all_widgets if text.lower() in w[0].lower()]
        self.populate_list(filtered)
