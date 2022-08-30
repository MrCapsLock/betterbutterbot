FROM python:3.10-slim

# Labels
LABEL maintainer = "me@mrcapslock.com"

# Select workdir
WORKDIR /betterbutterbot

# Install dependency
RUN apt update && apt upgrade -y
RUN pip install poetry

# Copy Source code
COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install --no-dev

# Install
COPY . .

# Run scheduled
CMD [ "poetry", "run", "python3", "main.py" ]
