from tortoise import fields

from src.core.models import AppModel


class Dummy(AppModel):
    name = fields.CharField(max_length=255)
