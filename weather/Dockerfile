FROM python:3.11
RUN mkdir /app
WORKDIR /app
COPY pyproject.toml poetry.lock README.md ./
COPY app ./app
COPY utility ./utility
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
CMD ["poetry", "run", "flask", "run", "-p", "5050"]
