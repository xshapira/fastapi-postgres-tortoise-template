from src.core.schemas import AppSchema


class NoteGet(AppSchema):
    id: int
    name: str
    pass


class NoteCreate(AppSchema):
    pass


class NoteUpdate(AppSchema):
    pass
