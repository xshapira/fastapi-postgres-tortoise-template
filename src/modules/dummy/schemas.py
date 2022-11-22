from tortoise.contrib.pydantic import pydantic_model_creator

from src.modules.dummy.models import Dummy


DummyGetBase = pydantic_model_creator(
    Dummy,
    name='DummyGet',
)

class DummyGet(DummyGetBase):
    pass

DummyCreate = pydantic_model_creator(
    Dummy,
    name='DummyCreate',
    exclude=['id'],
    exclude_readonly=True
)

DummyUpdate = pydantic_model_creator(
    Dummy,
    name='DummyUpdate',
)
