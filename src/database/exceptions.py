class CouldNotConnectToServer(Exception):

    """Custom general exception class to use when we can't connect to a server"""

    def __init__(
        self,
        *args: object,
        server: str,
        port: int
    ) -> None:
        """Custom general exception class to use when we can't connect to a server

        Args:
            server (str): Server name e.g. 'localhost'
            port (int): Port e.g. 5432
        """
        self.server = server
        self.port = port
        super().__init__(*args)

    def __str__(self) -> str:
        server_info: str = f"Could not connect to server '{self.server}:{self.port}'"
        s = super().__str__()
        return f"{s}. {server_info}" if s != "" else server_info
