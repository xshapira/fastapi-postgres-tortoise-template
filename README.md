# Overview

A simple starter kit for:

* FastAPI
* PostgreSQL
* TortoiseORM

Some points to note:

* Project layout is inspired by [zhanymkanov/fastapi-best-practices](https://github.com/zhanymkanov/fastapi-best-practices#1-project-structure-consistent--predictable) but deviates slightly by putting all 'modules' into a sub-folder and core/shared concerns in the core folder.
* Database and ORM are intentionally kept separate as far as possible.
* The database is created and migrations run automatically on startup. No messing around with Aerich or migration tools unless you want to create a new model.
* The test database is a real Postgres database but is recreated with each run, so it's ephemeral for all practical purposes.
* Will dockerise it if more than zero people would find this useful.

# Pre-requisites

* PostgreSQL
* Python 3.10

# Setup

1. Clone repo & cd into project
2. Create & activate virtual environment:

```bash
    python -m venv .ignored/venv
    source .ignored/venv/bin/activate
```

3. Install dependencies

```bash
    pip install -r requirements/base.txt -r requirements/dev.txt
```

4. Run app

```bash
    uvicorn src.main:app
```

See swagger docs at [http://localhost:8000/docs](http://localhost:8000/docs)

4. Run tests

```bash
    pytest -vv
```
