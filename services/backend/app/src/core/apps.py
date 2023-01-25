from fastapi import FastAPI

from src import config


# Create app
app: FastAPI = FastAPI(title=config.PROJECT_NAME)
