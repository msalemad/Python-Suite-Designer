from PyQt6.QtWidgets import (
    QMainWindow, QDockWidget, QMenuBar, QMenu, QStatusBar, QWidget, QVBoxLayout, QLabel, QAction,
    QFileDialog, QMessageBox
)
from PyQt6.QtCore import Qt
from .toolbox import ToolboxWidget
from .canvas import CanvasWidget
from .property_inspector import PropertyInspector
from .code_editor import CodeEditor
from .widget_browser import WidgetBrowser
from .animation_panel import AnimationPanel
from .event_panel import EventPanel
from .node_editor import NodeEditor
from .form_generator import FormGenerator
from .voice_control import VoiceControl
from .random_ui_generator import RandomUIGenerator
from .language_selector import LanguageSelector
from .responsive_view import ResponsiveView
from .template_panel import TemplatePanel
from .navigation_panel import NavigationPanel
from .compatibility_checker import CompatibilityChecker
from .layer_viewer import LayerViewer
from .history_panel import HistoryPanel
from .log_panel import LogPanel
from core.project_manager import ProjectManager
from core.plugin_manager import PluginManager
from core.theme_manager import ThemeManager
from core.asset_manager import AssetManager
from core.git_manager import GitManager
from core.macro_manager import MacroManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Suite Designer")
        self.setGeometry(100, 100, 1600, 900)
        self.setDockOptions(QMainWindow.DockOption.AllowNestedDocks | QMainWindow.DockOption.AllowTabbedDocks)
        # Managers
        self.project_manager = ProjectManager()
        self.plugin_manager = PluginManager()
        self.theme_manager = ThemeManager()
        self.asset_manager = AssetManager()
        self.git_manager = GitManager()
        self.macro_manager = MacroManager()
        # UI Panels
        self.property_inspector = PropertyInspector()
        self.code_editor = CodeEditor()
        self.widget_browser = WidgetBrowser()
        self.animation_panel = AnimationPanel()
        self.event_panel = EventPanel()
        self.node_editor = NodeEditor()
        self.form_generator = FormGenerator()
        self.voice_control = VoiceControl()
        self.random_ui_generator = RandomUIGenerator()
        self.language_selector = LanguageSelector()
        self.responsive_view = ResponsiveView()
        self.template_panel = TemplatePanel()
        self.navigation_panel = NavigationPanel()
        self.compatibility_checker = CompatibilityChecker()
        self.layer_viewer = LayerViewer()
        self.history_panel = HistoryPanel()
        self.log_panel = LogPanel()
        self.init_ui()

    def init_ui(self):
        self.init_menu()
        self.init_status_bar()
        self.init_dockables()
        self.init_canvas()

    def init_menu(self):
        menubar = QMenuBar(self)
        self.setMenuBar(menubar)
        # Archivo
        file_menu = QMenu("&Archivo", self)
        menubar.addMenu(file_menu)
        act_nuevo = QAction("Nuevo Proyecto", self)
        act_nuevo.triggered.connect(self.action_nuevo_proyecto)
        file_menu.addAction(act_nuevo)
        act_abrir = QAction("Abrir Proyecto...", self)
        act_abrir.triggered.connect(self.action_abrir_proyecto)
        file_menu.addAction(act_abrir)
        act_guardar = QAction("Guardar", self)
        act_guardar.triggered.connect(self.action_guardar_proyecto)
        file_menu.addAction(act_guardar)
        act_guardar_como = QAction("Guardar como...", self)
        act_guardar_como.triggered.connect(self.action_guardar_como)
        file_menu.addAction(act_guardar_como)
        file_menu.addSeparator()
        act_exportar = QAction("Exportar...", self)
        act_exportar.triggered.connect(self.action_exportar)
        file_menu.addAction(act_exportar)
        file_menu.addSeparator()
        act_salir = QAction("Salir", self)
        act_salir.triggered.connect(self.close)
        file_menu.addAction(act_salir)
        # Edición
        edit_menu = QMenu("&Edición", self)
        menubar.addMenu(edit_menu)
        edit_menu.addAction(QAction("Deshacer", self))
        edit_menu.addAction(QAction("Rehacer", self))
        edit_menu.addSeparator()
        edit_menu.addAction(QAction("Copiar", self))
        edit_menu.addAction(QAction("Pegar", self))
        edit_menu.addAction(QAction("Cortar", self))
        # Ver
        view_menu = QMenu("&Ver", self)
        menubar.addMenu(view_menu)
        view_menu.addAction(QAction("Vista previa", self))
        view_menu.addAction(QAction("Editor de código", self))
        view_menu.addAction(QAction("Panel de propiedades", self))
        view_menu.addAction(QAction("Toolbox", self))
        view_menu.addAction(QAction("Historial de cambios", self))
        # Proyecto
        project_menu = QMenu("&Proyecto", self)
        menubar.addMenu(project_menu)
        project_menu.addAction(QAction("Generar requirements.txt", self))
        project_menu.addAction(QAction("Exportar estructura modular", self))
        project_menu.addAction(QAction("Generar documentación", self))
        # Herramientas
        tools_menu = QMenu("&Herramientas", self)
        menubar.addMenu(tools_menu)
        tools_menu.addAction(QAction("Terminal Git", self))
        tools_menu.addAction(QAction("Panel de plugins", self))
        tools_menu.addAction(QAction("Macros", self))
        # Ayuda
        help_menu = QMenu("&Ayuda", self)
        menubar.addMenu(help_menu)
        help_menu.addAction(QAction("Documentación", self))
        help_menu.addAction(QAction("Acerca de", self))

    def action_nuevo_proyecto(self):
        self.project_manager.new_project()
        QMessageBox.information(self, "Nuevo Proyecto", "Se ha creado un nuevo proyecto.")

    def action_abrir_proyecto(self):
        path, _ = QFileDialog.getOpenFileName(self, "Abrir Proyecto", "", "Proyectos (*.json)")
        if path:
            try:
                self.project_manager.open_project(path)
                QMessageBox.information(self, "Proyecto abierto", f"Proyecto cargado: {path}")
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))

    def action_guardar_proyecto(self):
        try:
            self.project_manager.save_project()
            QMessageBox.information(self, "Guardado", "Proyecto guardado correctamente.")
        except Exception:
            self.action_guardar_como()

    def action_guardar_como(self):
        path, _ = QFileDialog.getSaveFileName(self, "Guardar Proyecto como", "", "Proyectos (*.json)")
        if path:
            try:
                self.project_manager.save_project(path)
                QMessageBox.information(self, "Guardado", f"Proyecto guardado en: {path}")
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))

    def action_exportar(self):
        path, _ = QFileDialog.getSaveFileName(self, "Exportar Proyecto", "", "JSON (*.json)")
        if path:
            try:
                self.project_manager.export_project("json", path)
                QMessageBox.information(self, "Exportado", f"Proyecto exportado a: {path}")
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))

    def init_status_bar(self):
        status = QStatusBar(self)
        status.setStyleSheet("QStatusBar { background: #222; color: #888; border: none; min-height: 18px; }")
        status.showMessage("Listo")
        self.setStatusBar(status)

    def init_dockables(self):
        # Toolbox
        self.toolbox_dock = QDockWidget("Toolbox", self)
        self.toolbox_dock.setWidget(ToolboxWidget())
        self.toolbox_dock.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea | Qt.DockWidgetArea.RightDockWidgetArea)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.toolbox_dock)
        # Panel de propiedades
        self.props_dock = QDockWidget("Propiedades", self)
        self.props_dock.setWidget(self.property_inspector)
        self.props_dock.setAllowedAreas(Qt.DockWidgetArea.RightDockWidgetArea)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.props_dock)
        # Historial de cambios
        self.history_dock = QDockWidget("Historial", self)
        self.history_dock.setWidget(self.history_panel)
        self.history_dock.setAllowedAreas(Qt.DockWidgetArea.BottomDockWidgetArea)
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.history_dock)
        # Editor de código
        self.code_editor_dock = QDockWidget("Editor de código", self)
        self.code_editor_dock.setWidget(self.code_editor)
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.code_editor_dock)
        # Navegador de widgets
        self.widget_browser_dock = QDockWidget("Navegador de widgets", self)
        self.widget_browser_dock.setWidget(self.widget_browser)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.widget_browser_dock)
        # Panel de animaciones
        self.animation_dock = QDockWidget("Animaciones", self)
        self.animation_dock.setWidget(self.animation_panel)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.animation_dock)
        # Panel de eventos
        self.event_dock = QDockWidget("Eventos", self)
        self.event_dock.setWidget(self.event_panel)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.event_dock)
        # Node editor
        self.node_editor_dock = QDockWidget("Node Editor", self)
        self.node_editor_dock.setWidget(self.node_editor)
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.node_editor_dock)
        # Form generator
        self.form_generator_dock = QDockWidget("Generador de formularios", self)
        self.form_generator_dock.setWidget(self.form_generator)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.form_generator_dock)
        # Panel de voz (opcional, oculto por defecto)
        self.voice_control_dock = QDockWidget("Control por voz", self)
        self.voice_control_dock.setWidget(self.voice_control)
        self.voice_control_dock.hide()
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.voice_control_dock)
        # Panel de templates
        self.template_panel_dock = QDockWidget("Templates", self)
        self.template_panel_dock.setWidget(self.template_panel)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.template_panel_dock)
        # Panel de navegación
        self.navigation_panel_dock = QDockWidget("Navegación", self)
        self.navigation_panel_dock.setWidget(self.navigation_panel)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.navigation_panel_dock)
        # Panel de capas
        self.layer_viewer_dock = QDockWidget("Capas", self)
        self.layer_viewer_dock.setWidget(self.layer_viewer)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.layer_viewer_dock)
        # Panel de logs
        self.log_panel_dock = QDockWidget("Logs", self)
        self.log_panel_dock.setWidget(self.log_panel)
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.log_panel_dock)
        # Responsive view, language selector, random UI generator, compatibility checker
        # pueden integrarse como diálogos o paneles flotantes según necesidad

    def init_canvas(self):
        self.canvas = CanvasWidget()
        self.setCentralWidget(self.canvas)
