from fastapi import FastAPI


def mount_routes(app: FastAPI):
    # Routes
    # NB: The pydantic schemas must be created AFTER the ORM is init'ed!
    from src.modules.home.routes import router as home_router
    from src.modules.note.routes import router as note_router


    app.include_router(home_router)
    app.include_router(note_router)
