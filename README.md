# Overview

Basic template that includes:

* FastAPI
* PostgreSQL
* TortoiseORM (Aerich for migrations)

Ready to go.

* Project layout is inspired by [zhanymkanov/fastapi-best-practices](https://github.com/zhanymkanov/fastapi-best-practices#1-project-structure-consistent--predictable) but deviates slightly by putting all 'modules' into a sub-folder and core/shared concerns in the core folder.
* The database is created and migrations run automatically on startup. No messing around with Aerich or migration tools unless you want to create a new model.
* The test database is a real database but is reset with each run (public schema dropped & recreated), so it's ephemeral for all practical purposes.

# Getting Started


## Docker

Requires:

* Docker
* Docker-Compose

`docker-compose up --build`

## Local

Requires:

* Python 3.10+
* Postgres

Clone repo:

```bash
    git clone git@github.com:pavdwest/fastapi-postgres-tortoise-template.git
```

NB! Navigate to app folder:

```bash
    cd fastapi-postgres-tortoise-template/services/backend/app
```

Create & Activate virtual environment:

```bash
    python -m venv ./ignored/venv
```

```bash
    source ./ignored/venv/bin/activate
```

Install dependencies:

```bash
    pip install requirements/base.txt
```

Note that versions are intentionally omitted - lock them down when you start.

Run:

```bash
    uvicorn src.main:app --reload --port 8000
```

## View Swagger docs

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

# Tests

NB! Navigate to the app folder:

```bash
    cd fastapi-postgres-tortoise-template/services/backend/app
    pytest -vv
```

# Adding New Models/Modules

## Model

Definition:

```bash
    src/modules/thingy/models.py
```

ORM:

`src/database/config.py` -> Add to APP_MODELS

`aerich migrate` -> Generates migration. Double check & name correctly. Rename constraints


## Schemas

`src/modules/thingy/schemas.py`

## Routes

`src/modules/thingy/routes.py`
