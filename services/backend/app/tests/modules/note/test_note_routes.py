from fastapi import status
import pytest
from httpx import AsyncClient


@pytest.mark.anyio
async def test_create(client: AsyncClient):
    payload = {
        'title': 'My First Note',
        'body': 'This is the first note that I am writing.'
    }

    response = await client.post(
        '/note',
        json=payload
    )
    assert response.status_code == status.HTTP_201_CREATED, response.text
    data = response.json()
    assert data['title'] == 'My First Note'
    assert data['body'] == 'This is the first note that I am writing.'
