# mypy: no-disallow-untyped-decorators
# pylint: disable=E0611,E0401
import os


# Setup env before importing anything
os.environ['DATABASE_NAME'] = 'example_app_db_test'
os.environ['RECREATE_DATABASE'] = 'TRUE'


import pytest
from asgi_lifespan import LifespanManager
from httpx import AsyncClient
from src.main import app


@pytest.fixture(scope="module")
def anyio_backend():
    return "asyncio"


@pytest.fixture(scope="module")
async def client():
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://test") as c:
            yield c
