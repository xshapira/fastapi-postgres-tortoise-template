from __future__ import annotations
from src.logging.services import logger

import psycopg2

from src.database.exceptions import CouldNotConnectToServer


class AppDatabaseUtil:

    """Simple Utility to manage misc db admin tasks"""

    def __init__(
        self,
        server:   str = 'localhost',
        username: str = 'postgres',
        password: str = '',
        port:     int = 5432,
    ) -> None:

        """Init: Simple Utility to manage misc db admin tasks

        Args:
            server (str, optional): Defaults to 'localhost'.
            username (str, optional): Defaults to 'postgres'.
            password (str, optional): Defaults to ''.
            port (int, optional): Defaults to 5432.
        """

        self._server            = server
        self._username          = username
        self._password          = password
        self._port              = port
        self._server_connection = None
        self._create_server_connection()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._server_connection.close()

    def _create_server_connection(self):

        """Instantiates self._server_connection, a connection to the server

        Raises:
            CouldNotConnectToServer: A catch-all exception if anything goes wrong
        """

        try:
            self._server_connection = psycopg2.connect(
                host=self._server,
                user=self._username,
                password=self._password,
                port=self._port,
            )
            self._server_connection.set_isolation_level(
                psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT
            )
            logger.info(f"Connected to {self._server}:{self._port}")
        except Exception as e:
            raise CouldNotConnectToServer(server=self._server, port=self._port)

    def database_exists(
        self,
        database: str
    ) -> bool:

        """Checks if the given database exists

        Args:
            server_connection (psycopg2.extensions.connection): A connection to the server (see get_server_connection())
            database (str): Name of the database

        Returns:
            bool: True if the database exists, otherwise False
        """

        if self._server_connection is not None:
            sql = f"select count(datname) from pg_catalog.pg_database where datname = '{database}';"
            cursor = self._server_connection.cursor()
            cursor.execute(sql)
            res = cursor.fetchall()
            if len(res) > 0:
                if res[0][0] > 0:
                    logger.info(f"Database found: {self._server}/{database}")
                    return True
                else:
                    logger.warning(f"Database not found: {self._server}/{database}")
                    return False

        return False

    def create_database(
        self,
        database: str
    ) -> bool:

        """Create database if it doesn't exist

        Args:
            database (str): Database to create

        Returns:
            bool: True if the database was created during this function call. Other values are inconclusive.
        """

        if self._server_connection is not None:
            if self.database_exists(database):
                logger.info(f"Database exists: {self._server}/{database}")
                return False
            else:
                sql = f'create database "{database}";'
                cursor = self._server_connection.cursor()
                cursor.execute(sql)
                logger.warning(f"Created database: '{database}'")
                return True

        return False

    def drop_database(
        self,
        database: str
    ) -> bool:

        """Drop all connections to the database and then drop it. If anything's connected tough luck.

        Args:
            database (str): Database name

        Returns:
            bool: True if the database is known not to exist at the end of this function's execution. Other values are inconclusive.
        """

        if self._server_connection is not None:
            if self.database_exists(database):
                self.kill_all_connections(database)
                logger.warning(f"Dropping database: {self._server}/{database}")
                sql = f'drop database "{database}";'
                cursor = self._server_connection.cursor()
                cursor.execute(sql)
                return True
            else:
                return True

    def kill_all_connections(
        self,
        database: str
    ) -> bool:

        """_summary_

        Args:
            database (str): Kill all connections to the database.

        Returns:
            bool: True if it is known that there are no connections to the db left after this function's execution. Other values are inconclusive.
        """

        if self._server_connection is not None:
            if self.database_exists(database):
                sql = f"select *, pg_terminate_backend(pid) from pg_stat_activity where pid <> pg_backend_pid() and datname = '{database}';"
                logger.warning(f"Killing all connections to {self._server}/{database}...")
                cursor = self._server_connection.cursor()
                cursor.execute(sql)
                return True
            else:
                return True

    @classmethod
    def from_db_config(cls) -> AppDatabaseUtil:

        """Expedient factory method to create an instance of this utility

        Returns:
            AppDatabaseUtil: An instance of AppDatabaseUtil
        """

        from src import config

        return AppDatabaseUtil(
            server = config.DATABASE_HOST,
            username = config.DATABASE_USERNAME,
            password = config.DATABASE_PASSWORD,
            port = config.DATABASE_PORT
        )

    @classmethod
    def init_app_db(cls, database_name: str, recreate_database: bool = False) -> bool:

        """Read app config and init database

        Returns:
            bool: True if the database was created during this function call. Other values are not indicative.
        """

        with cls.from_db_config() as util:
            if recreate_database:
                util.drop_database(database_name)

            return util.create_database(database_name)
