FROM python:3-alpine

COPY . /app

WORKDIR /app

RUN addgroup btsuser && \
    adduser \
      --no-create-home \
      --ingroup btsuser \
      btsuser

RUN python -m pip install poetry && \
    poetry install

USER btsuser

ENTRYPOINT [ "poetry", "run", "uvicorn", "app.main:app" ]

