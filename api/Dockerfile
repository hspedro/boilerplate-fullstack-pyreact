FROM python:3.10-buster as base_image

ARG BASE_PATH=./api

ENV POETRY_VERSION=1.1.12
RUN pip install "poetry==${POETRY_VERSION}"

WORKDIR /code

COPY ${BASE_PATH}/poetry.lock ${BASE_PATH}/pyproject.toml /code/
RUN poetry config virtualenvs.create false && \
    poetry config cache-dir /code/.cache/pypoetry
RUN --mount=type=cache,target=/code/.cache/pypoetry \
    poetry install --no-interaction --no-ansi --no-dev

COPY ${BASE_PATH}/api/ /code/api
WORKDIR /code/api

FROM base_image as prod_stage

CMD uvicorn main:app \
    --host $HOST \
    --port $PORT \
    --workers $WORKERS

FROM base_image as dev_stage

CMD uvicorn main:app \
    --host $HOST \
    --port $PORT \
    --workers $WORKERS \
    --reload
