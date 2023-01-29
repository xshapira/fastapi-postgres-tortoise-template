from src.core.schemas import generate_app_schema, AppSchemaGet, AppSchemaCreate
from src.core.schemas import AppSchema
from src.modules.note.models import Note


NoteCreate = generate_app_schema(
    Note,
    app_schema_base_class=AppSchemaCreate,
    exclude_readonly=True,
    exclude=[
    ]
)


NoteGet = generate_app_schema(
    Note,
    app_schema_base_class=AppSchemaGet,
    exclude_readonly=True,
    exclude=[
    ]
)


class NoteUpdate(AppSchema):
    pass
