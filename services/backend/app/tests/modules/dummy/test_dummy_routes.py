from fastapi import status
import pytest
from httpx import AsyncClient


@pytest.mark.anyio
async def test_create(client: AsyncClient):

    payload = {
        'name': 'Not idempotent'
    }

    response = await client.post(
        '/dummy',
        json=payload
    )
    assert response.status_code == status.HTTP_201_CREATED, response.text
    data = response.json()
    assert data['name'] == 'Not idempotent'


@pytest.mark.anyio
async def test_create_burst(client: AsyncClient):

    payload = {
        'name': 'Not idempotent'
    }

    responses = []

    for i in range(50):
        responses.append(
            await client.post(
                '/dummy',
                json=payload
            )
        )
    assert responses[0].status_code == status.HTTP_201_CREATED, responses[0].text
    data = responses[0].json()
    assert data['name'] == 'Not idempotent'
