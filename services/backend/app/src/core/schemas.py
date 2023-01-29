from enum import Enum
from typing import Tuple, Type

from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import BaseModel

from src.core.models import AppModel


class AppSchema(BaseModel):

    """
    Base class for app's pydantic schemas

    Args:
        BaseModel (_type_): pydantic.BaseModel
    """

    @classmethod
    def suffix(cls):
        raise NotImplementedError("AppSchema")


class AppSchemaDb(AppSchema):
    @classmethod
    def suffix(cls):
        return 'Db'


class AppSchemaCreate(AppSchema):
    @classmethod
    def suffix(cls):
        return 'Create'


class AppSchemaGet(AppSchema):
    @classmethod
    def suffix(cls):
        return 'Get'


class AppSchemaUpdate(AppSchema):
    @classmethod
    def suffix(cls):
        return 'Update'


class AppSchemaUpdateWithId(AppSchema):
    @classmethod
    def suffix(cls):
        return 'UpdateWithId'


class Status(AppSchema):
    message: str


# TODO: Refine the 'excludes' params
def generate_app_schema(
    model: AppModel,
    app_schema_base_class: Type[AppSchema],
    name: str = None,
    exclude: Tuple[str, ...] = (),
    include: Tuple[str, ...] = (),
    exclude_readonly: bool = False,

) -> AppSchema:

    """
    Generates a new Pydantic class type using the provided Tortoise model and mixes in AppSchema

    Args:
        model (AppModel): Tortoise ORM Model
        name (str): What should this generated class be called?
        exclude_readonly (bool, optional): See tortoise.contrib.pydantic.pydantic_model_creator. Defaults to False.
        exclude (Tuple[str, ...], optional): See tortoise.contrib.pydantic.pydantic_model_creator. Defaults to nothing explicitly excluded.

    Returns:
        BaseModel: Generated pydantic class ready to use in FastAPI routes
    """

    if name is None:
        name = f"{model.__name__}{app_schema_base_class.suffix()}"

    pydantic_model: BaseModel = pydantic_model_creator(
        model,
        name=name,
        exclude=exclude,
        include=include,
        exclude_readonly=exclude_readonly
    )

    pydantic_app_model = type(
        f"{name}AppSchema",
        (pydantic_model, AppSchema, ),
        {}
    )

    return pydantic_app_model
