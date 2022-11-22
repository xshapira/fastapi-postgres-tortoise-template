from typing import List

from fastapi import APIRouter, status

from src.modules.dummy.models import Dummy
from src.modules.dummy.schemas import DummyGet, DummyCreate, DummyUpdate


router = APIRouter(
    tags=['Dummy']
)


@router.post(
    '/dummy',
    response_model=DummyGet,
    status_code=status.HTTP_201_CREATED,
    description='Create a single Dummy item.'
)
async def create(item: DummyCreate) -> DummyGet:
    db_item = await Dummy(**item.dict())
    await db_item.save()
    return await DummyGet.from_tortoise_orm(db_item)


@router.get(
    '/dummy',
    response_model=List[DummyGet],
    status_code=status.HTTP_200_OK,
    description='Get all Dummies.'
)
async def index() -> List[DummyGet]:
    db_items = await Dummy.all()
    return [await DummyGet.from_tortoise_orm(i) for i in await Dummy.all()]
