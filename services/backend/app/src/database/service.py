from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.exceptions import DBConnectionError
from tortoise.transactions import in_transaction
from aerich import Command

from src.core.logging import logger
from src.core.services import AppService
from src.database.config import APP_MODELS, APPS, TORTOISE_CONFIG, MODULES, RESET_DATABASE


class DatabaseService(AppService):
    # Early init models
    Tortoise.init_models(
        models_paths=APP_MODELS,
        app_label='models',
        _init_relations=True
    )

    @classmethod
    async def on_shutdown(cls):
        await Tortoise.close_connections()

    @classmethod
    def register_app(cls, app: FastAPI):
        DatabaseService.app = app
        app.add_event_handler('startup', cls.on_startup)
        app.add_event_handler('shutdown', cls.on_shutdown)

    @classmethod
    async def tortoise_init(
        cls,
        create_db: bool,
    ) -> None:

        """
        Simple QOL

        Args:
            create_db (bool): Whether the db must be created
        """
        # print(TORTOISE_CONFIG)

        await Tortoise.init(
            config=TORTOISE_CONFIG,
            _create_db=create_db,
            modules=MODULES
        )

    @classmethod
    async def db_migrate(cls) -> None:

        """
        Run migrations. Is idempotent.

        """

        logger.info('Checking if any migrations need to be run...')
        command = Command(
            tortoise_config=TORTOISE_CONFIG,
            app='models',
            location='src/database/migrations'
        )
        await command.init()
        migrations = await command.upgrade()
        if len(migrations) > 0:
            logger.warning(f"Migrations run ({len(migrations)}):")
            [logger.warning(m) for m in migrations]

    @classmethod
    async def db_seed(cls) -> None:
        from src.core.models import AppModel
        AppModel.seed_all_derived_classes()

    @classmethod
    async def drop_public_schema(cls) -> None:
        async with in_transaction('default') as conn:
            # Check schema
            schemas_res = await conn.execute_query('SELECT schema_name FROM information_schema.schemata;')
            assert 'public' in [s.get('schema_name') for s in schemas_res[1]]

            # Drop public schema
            await conn.execute_query('DROP SCHEMA public CASCADE;')
            schemas_res = await conn.execute_query('SELECT schema_name FROM information_schema.schemata;')
            assert 'public' not in [s.get('schema_name') for s in schemas_res[1]]

            # Recreate public schema
            await conn.execute_query('CREATE SCHEMA public;')
            await conn.execute_query('GRANT ALL ON SCHEMA public TO postgres;')
            await conn.execute_query('GRANT ALL ON SCHEMA public TO public;')
            schemas_res = await conn.execute_query('SELECT schema_name FROM information_schema.schemata;')
            assert 'public' in [s.get('schema_name') for s in schemas_res[1]]

            logger.warning('Database reset.')

    @classmethod
    async def on_startup(cls, generate_schemas: bool = False):

        """
        Initialise the App's ORM

        Args:
            app (FastAPI): The App
            generate_schemas (bool, optional): If the db was just created,
            we need to run migrations. Defaults to False.
        """

        try:
            await cls.tortoise_init(create_db=False)

            if RESET_DATABASE:
                logger.warning('Resetting database...')
                await cls.drop_public_schema()

            await cls.db_migrate()
            await cls.db_seed()

        except DBConnectionError as ex:
            logger.warning('Could not connect to database. Trying to create it...')
            await cls.tortoise_init(create_db=True)
            await cls.db_migrate()
            logger.warning('Database created.')
