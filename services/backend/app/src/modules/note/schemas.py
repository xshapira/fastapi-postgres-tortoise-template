from tortoise.contrib.pydantic import pydantic_model_creator

from src.core.schemas import AppSchema
from src.modules.note.models import Note


NoteCreate = pydantic_model_creator(
    Note,
    name='NoteCreate',
    exclude_readonly=True,
    exclude=[
    ]
)


NoteGet = pydantic_model_creator(
    Note,
    name='NoteGet',
    exclude_readonly=True,
    exclude=[
    ]
)


class NoteUpdate(AppSchema):
    pass
