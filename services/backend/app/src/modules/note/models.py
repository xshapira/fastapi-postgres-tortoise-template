from tortoise import fields

from src.core.models import AppModel


class Note(AppModel):
    title = fields.CharField(max_length=4095, unique=True, null=False)
    body = fields.TextField(null=True)
