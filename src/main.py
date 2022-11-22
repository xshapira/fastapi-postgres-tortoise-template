from fastapi import FastAPI

from src.logging.services import logger
from src import config
from src.database.utils import AppDatabaseUtil
from src.orm.service import AppORM


# Create app
app: FastAPI = FastAPI(title=config.PROJECT_NAME)

# DB
db_created: bool = AppDatabaseUtil.init_app_db(config.DATABASE_NAME)

# ORM
AppORM.init_app_orm(app=app, generate_schemas=db_created)

# Routes
# NB: The pydantic schemas must be created AFTER the ORM relationships are init'ed
from src.modules.home.routes import router as home_router
from src.modules.dummy.routes import router as dummy_router

app.include_router(home_router)
app.include_router(dummy_router)
