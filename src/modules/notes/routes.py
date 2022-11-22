from typing import Type, Dict

from fastapi import APIRouter, status, Response

from src.core.routes import CrudRouter
from src.modules.notes.models import Note
from src.modules.notes.schemas import NoteCreate, NoteUpdate, NoteGet


# Model crud class instance
CRUD: CrudRouter = CrudRouter(
    model=Note,
    get_schema=NoteGet,
    create_schema=NoteCreate,
    update_schema=NoteUpdate
)

@CRUD.router.get(
    f"{CRUD.endpoint}",
    response_model=CRUD.get_schema,
    status_code=status.HTTP_200_OK
)
async def get_one(
    id: int,
    response: Response
) -> CRUD.get_schema:
    return await CRUD.read_by_id(id)


@CRUD.router.delete(
    f"{CRUD.endpoint}",
    response_model=CRUD.get_schema,
    status_code=status.HTTP_200_OK
)
async def delete_one(
    id: int,
    response: Response
) -> CRUD.get_schema:
    return await CRUD.read_by_id(id)






# from fastapi import APIRouter


# from src.core.routes import RouterMetadata
# from src.modules.notes.models import Note


# ROUTER_METADATA = RouterMetadata(model=Note)
# router = APIRouter(
#     # prefix=f"{ROUTER_METADATA.ROUTE_NAME_SINGULAR}",
#     tags=[f"{ROUTER_METADATA.FRIENDLY_NAME_PLURAL}"]
# )


# @router.post(
#     f"/{ROUTER_METADATA.ROUTE_NAME_SINGULAR}",
#     description=f"Create a new {ROUTER_METADATA.FRIENDLY_NAME_SINGULAR}. Error if it already exists.",
# )
# async def post():
#     return {
#         'message': 'TODO'
#     }


# @router.put(
#     f"/{ROUTER_METADATA.ROUTE_NAME_SINGULAR}",
#     description=f"Update a {ROUTER_METADATA.FRIENDLY_NAME_SINGULAR}. Error if it already exists.",
# )
# async def put():
#     return {
#         'message': 'TODO'
#     }


# @router.patch(
#     f"/{ROUTER_METADATA.ROUTE_NAME_SINGULAR}",
#     description=f"Update a {ROUTER_METADATA.FRIENDLY_NAME_SINGULAR}. Error if it already exists.",
# )
# async def patch():
#     return {
#         'message': 'TODO'
#     }
