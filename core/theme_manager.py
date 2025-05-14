from typing import Dict

class ThemeManager:
    def __init__(self):
        self.themes = {
            "default": {"background": "#222", "foreground": "#eee"},
            "dark": {"background": "#111", "foreground": "#fff"},
            "light": {"background": "#fff", "foreground": "#111"},
        }
        self.current_theme = "default"

    def load_theme(self, name: str) -> None:
        if name in self.themes:
            self.current_theme = name

    def save_theme(self, name: str, data: Dict) -> None:
        self.themes[name] = data

    def list_themes(self) -> list:
        return list(self.themes.keys())

    def apply_theme(self, name: str, app=None) -> None:
        self.load_theme(name)
        theme = self.themes[name]
        if app:
            app.setStyleSheet(f"QWidget {{ background: {theme['background']}; color: {theme['foreground']}; }}")
