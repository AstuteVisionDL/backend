FROM ultralytics/ultralytics:8.0.214-python
RUN mkdir app
WORKDIR /app
RUN pip install poetry
ADD poetry.lock .
ADD pyproject.toml .
RUN poetry install --without dev
COPY /src ./src

