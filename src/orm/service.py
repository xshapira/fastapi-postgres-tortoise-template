from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from src.config import APP_MODELS, TORTOISE_CONFIG


class AppORM:

    @classmethod
    def init_app_orm(cls, app: FastAPI, generate_schemas: bool = False):

        Tortoise.init_models(
            APP_MODELS,
            'models',
            True
        )

        if generate_schemas:
            print('Generating schemas...')

        register_tortoise(
            app=app,
            config=TORTOISE_CONFIG,
            generate_schemas=generate_schemas,
            add_exception_handlers=True
        )

        @app.on_event('shutdown')
        async def shutdown():
            await Tortoise.close_connections()
