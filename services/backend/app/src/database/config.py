import os


# Database
DATABASE_HOST     = os.environ.get('DATABASE_HOST'    , 'localhost')
DATABASE_PORT     = os.environ.get('DATABASE_PORT'    , 5432)
DATABASE_USERNAME = os.environ.get('DATABASE_USERNAME', 'postgres')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', '')
DATABASE_NAME     = os.environ.get('DATABASE_NAME'    , 'example_app_db')

RESET_DATABASE = os.environ.get('RESET_DATABASE', 'FALSE') == 'TRUE'
DATABASE_CONNECT_TIMEOUT = os.environ.get('DATABASE_CONNECT_TIMEOUT', 10)

# ORM: Add new models here
APP_MODELS = [
    'src.modules.note.models',
]

# Automated formatting
MODULES = {
    'models': APP_MODELS
}

APPS = {
    'models': {
        'models': APP_MODELS + ['aerich.models'],
        'default_connection': 'default',
    }
}

TORTOISE_CONFIG = {
    'connections': {
        'default': {
            'engine': 'tortoise.backends.asyncpg',
            'credentials': {
                "host":     DATABASE_HOST,
                "port":     DATABASE_PORT,
                "user":     DATABASE_USERNAME,
                "password": DATABASE_PASSWORD,
                "database": DATABASE_NAME
            }
        },
    },
    'apps': APPS
}
