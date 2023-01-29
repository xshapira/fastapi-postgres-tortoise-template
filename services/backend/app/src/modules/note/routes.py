from fastapi import APIRouter, status, HTTPException
from tortoise.exceptions import IntegrityError, DoesNotExist

from src.modules.note.models import Note
from src.modules.note.schemas import NoteCreate, NoteGet


router = APIRouter(
    tags=['Notes']
)


@router.post(
    f"/note",
    response_model=NoteGet,
    status_code=status.HTTP_201_CREATED,
    description=f"Create Note"
)
async def create(item: NoteCreate) -> NoteGet:

    """
    Create a new item from the data provided

    Args:
        item (NoteCreate): Instance of AppSchema (a Pydantic Base Model)

    Raises:
        HTTPException: 409 if a required with the desired key already exists

    Returns:
        NoteGet: Instance of AppSchema (a Pydantic Base Model)
    """

    try:
        db_item = await Note.create(
            **item.dict(exclude_unset=True)
        )
        return await NoteGet.from_tortoise_orm(db_item)
    except IntegrityError as ex:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(ex)
        )


@router.get(
    f"/note",
    response_model=NoteGet,
    status_code=status.HTTP_200_OK,
    description=f"Get Note by ID"
)
async def get(id: int) -> NoteGet:

    """
    Get an item by its surrogate key (id)

    Args:
        id (int): Id of the item you want to retrieve

    Raises:
        HTTPException: 404 if an item with the requested id could not be found

    Returns:
        NoteGet: Instance of AppSchema (a Pydantic Base Model)
    """

    try:
        db_item = await Note.get(id=id)
        return await NoteGet.from_tortoise_orm(db_item)
    except DoesNotExist as ex:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(ex)
        )
