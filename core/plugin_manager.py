from typing import List

class PluginManager:
    def load_plugins(self) -> None:
        """Cargar plugins instalados"""
        pass

    def install_plugin(self, source: str) -> None:
        """Instalar un nuevo plugin"""
        pass

    def remove_plugin(self, name: str) -> None:
        """Eliminar un plugin"""
        pass

    def enable_plugin(self, name: str) -> None:
        """Activar un plugin"""
        pass

    def disable_plugin(self, name: str) -> None:
        """Desactivar un plugin"""
        pass

    def list_plugins(self) -> List[str]:
        """Listar plugins instalados"""
        pass
