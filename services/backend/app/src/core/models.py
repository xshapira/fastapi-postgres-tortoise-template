from enum import IntEnum
from typing import Type

from tortoise.models import Model
from tortoise import fields
from functools import lru_cache
from inflection import underscore

from src.core.logging import logger


class HasId:
    id = fields.BigIntField(pk=True)


class HasIdentifier:
    identifier = fields.CharField(unique=True, max_length=1023, null=False)


class HasTimestamps:
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)


class HasDescription:
    description = fields.TextField(null=True)


class AppModel(Model, HasId, HasTimestamps):

    """
    Base Object Relational Model
    """

    @classmethod
    def seed_all_derived_classes(cls):
        # logger.warn(f"Not implemented: {cls.__name__}.seed_all_derived_classes")
        pass

    class Meta:
        abstract = True

    @classmethod
    @lru_cache(maxsize=1)
    def table_name(cls) -> str:
        return underscore(cls.__name__)

    def __init_subclass__(cls) -> None:
        super().__init_subclass__()
        cls._meta.db_table = cls.table_name()


class AppEnum(IntEnum):
    pass


class AppEnumModel(AppModel):
    enum_class: Type[AppEnum]
