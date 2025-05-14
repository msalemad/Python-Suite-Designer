class GitManager:
    def login(self, username: str, password: str) -> None:
        """Login a Git"""
        pass

    def clone_repo(self, url: str, path: str) -> None:
        """Clonar repositorio"""
        pass

    def pull(self) -> None:
        """Pull cambios"""
        pass

    def push(self) -> None:
        """Push cambios"""
        pass

    def commit(self, message: str) -> None:
        """Commit cambios"""
        pass

    def create_repo(self, name: str) -> None:
        """Crear nuevo repositorio"""
        pass

    def sync(self) -> None:
        """Sincronizar repositorio"""
        pass
