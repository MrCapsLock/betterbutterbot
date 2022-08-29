FROM python:3.10-slim

# Select workdir
WORKDIR /usr/share/betterbutterbot

# Install dependency
RUN apt update && apt upgrade -y
RUN pip install poetry

# Copy Source code
COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install --no-dev

# Labels
LABEL maintainer = "me@mrcapslock.com"

# Install
COPY . .

# Run scheduled
CMD [ "poetry", "run", "python3", "personal-bot/main.py" ]
