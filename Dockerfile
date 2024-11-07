FROM python:3.10 AS base

RUN apt-get update && apt-get upgrade -y && \
  apt-get install -y --no-install-recommends \
  build-essential \
  && apt-get clean

ENV POETRY_VERSION=1.3.2
ENV POETRY_HOME=/opt/poetry
ENV PATH="$POETRY_HOME/bin:$PATH"

RUN curl -sSL https://install.python-poetry.org | python3 - && \
  poetry --version

WORKDIR /usr/src/app/

COPY ./pyproject.toml ./poetry.lock /usr/src/app/

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY . /usr/src/app/
