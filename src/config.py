import os

from dotenv import load_dotenv


# Load values from the .env file
load_dotenv()

# Project
PROJECT_NAME='Thialfi'

# Project folders
# TODO

# Database
DATABASE_HOST=os.environ.get('DATABASE_HOST', 'localhost')
DATABASE_PORT=os.environ.get('DATABASE_PORT', 5432)
DATABASE_USERNAME=os.environ.get('DATABASE_USERNAME', 'postgres')
DATABASE_PASSWORD=os.environ.get('DATABASE_PASSWORD', '')
DATABASE_NAME=os.environ.get('DATABASE_NAME', 'example_app_db')

RECREATE_DATABASE=os.environ.get('RECREATE_DATABASE', 'FALSE') == 'TRUE'

# ORM
APP_MODELS = [
    "src.modules.dummy.models",
]

APPS = {
    'models': {
        'models': APP_MODELS + ['aerich.models'],
        'default_connection': 'default',
    }
}

TORTOISE_CONFIG = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": DATABASE_HOST,
                "port": DATABASE_PORT,
                "user": DATABASE_USERNAME,
                "password": DATABASE_PASSWORD,
                "database": DATABASE_NAME
            }
        },
    },
    'apps': APPS
}
