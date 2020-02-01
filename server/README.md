# BTS Prediction Market API Server

This repository contains the logic for user/trade authentication,
market predictions and pricing, database interactions, trade logic,
and MLB statistics mining.

## Layout

The repository is laid out as follows:

```
├── README.md
├── app/
│   ├── __init__.py
│   ├── auth/
│   ├── errors/
│   ├── main.py
│   └── routers/
│       ├── __init__.py
│       └── players.py
├── tests/
└── pyproject.toml
```

`pyproject.toml` is the new defacto standard for the new Python package
managers, [Poetry](https://github.com/python-poetry/poetry)
and [Pipenv](https://github.com/pypa/pipenv). It replaces all previous configuration files and scripts, including requirements.txt, setup.cfg, pytest.ini, setup.py, etc.

The API server uses [FastAPI](https://github.com/tiangolo/fastapi) due to its speed, simplicity, and freshness.

## Install

Ensure that [Python 3.6+](https://www.python.org/downloads/) is installed.
Then, make sure you have [Poetry](https://github.com/python-poetry/poetry) installed too.

Once Poetry is installed, to install all packages (including development dependencies), run

```bash
poetry install
```

To add any new packages, simply run

```bash
poetry add [--dev] <package>
```

Note: `--dev` will add the dependency under the development dependencies
section. This is reserved for tools like Pytest, Black, Coverage, Mock, etc.

## Running the server

After all dependencies are installed, you can run the server with

```bash
poetry run uvicorn app.main:app [--reload]
```

Note: Passing in `--reload` will hot-reload whenever you save a file.

## Contributing

To contribute, ensure commit messages contain a succinct title describing
the changes as well as a more detailed description with any nuances or
relevant information.

Once you build a new feature, fix a bug, etc., ensure to run

```bash
poetry run black **
poetry run pytest
```

`black` is used for enforcing consistent Python formatting and
`pytest` is used for running tests.

Lastly, while in development, if you navigate to http://127.0.0.1:8000/docs,
you'll see Swagger docs for the API server.