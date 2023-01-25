# mypy: no-disallow-untyped-decorators
# pylint: disable=E0611,E0401
import os
import pytest
from asgi_lifespan import LifespanManager
from httpx import AsyncClient

# Setup env before importing anything
os.environ['DATABASE_NAME'] = 'sleipnir_test'
os.environ['RESET_DATABASE'] = 'TRUE'

from src.main import app


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture(scope="session")
async def client():
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://test") as c:
            yield c
