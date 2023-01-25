# Overview

Basic template that includes:

* FastAPI
* TortoiseORM (Aerich for migrations)

Ready to go.

# Getting Started


## Docker

Requires:

* Docker
* Docker-Compose

`docker-compose up --build`

## Local

Requires:

* Python 3.10+

Clone repo:

`git clone git@github.com:pavdwest/fastapi-postgres-tortoise-template.git`

NB! Navigate to app folder:

`cd fastapi-postgres-tortoise-template/services/backend/app`

Create & Activate virtual environment:

`python -m venv ./ignored/venv`

`source ./ignored/venv/bin/activate`

Install dependencies:

`pip install requirements/base.txt`

Run:

`uvicorn src.main:app --reload --port 8000`

## View Swagger docs

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Tests

NB! Navigate to the app folder:

`cd fastapi-postgres-tortoise-template/services/backend/app`
`pytest -vv`
