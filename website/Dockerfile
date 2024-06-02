# Use an official Python runtime based on Debian 10 "buster" as a parent image.
FROM python:3.8.1-slim-buster

# # Add user that will be used in the container.
# RUN useradd wagtail

# Port used by this container to serve HTTP.
EXPOSE 8000

# Set environment variables.
# 1. Force Python stdout and stderr streams to be unbuffered.
# 2. Set PORT variable that is used by Gunicorn. This should match "EXPOSE"
#    command.
ENV PYTHONUNBUFFERED=1 \
    PORT=8000

# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libmariadbclient-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
    curl \
 && rm -rf /var/lib/apt/lists/*

# Use /website folder as a directory where the source code is stored.
WORKDIR /website

# Set this directory to be owned by the "wagtail" user. This Wagtail project
# # uses SQLite, the folder needs to be owned by the user that
# # will be writing to the database file.
# RUN chown wagtail:wagtail /app

# Copy the source code of the project into the container.
COPY . .

# # Use user "wagtail" to run the build commands below and the server itself.
# USER wagtail

# Install poetry for management of project requirements.
RUN curl -sSL https://install.python-poetry.org | python3 -

# Install the project requirements.
COPY poetry.lock pyproject.toml /
RUN export PATH="/root/.local/bin:$PATH"
RUN /root/.local/bin/poetry config virtualenvs.create false
RUN /root/.local/bin/poetry install --no-interaction --no-ansi

# Collect static files.
RUN /root/.local/bin/poetry run python manage.py collectstatic --noinput --clear

# Runtime command that executes when "docker run" is called, it does the
# following:
#   1. Migrate the database.
#   2. Start the application server.
# WARNING:
#   Migrating database at the same time as starting the server IS NOT THE BEST
#   PRACTICE. The database should be migrated manually or using the release
#   phase facilities of your hosting platform. This is used only so the
#   Wagtail instance can be started with a simple "docker run" command.
CMD set -xe; /root/.local/bin/poetry run python manage.py migrate --noinput && /root/.local/bin/poetry run gunicorn website.wsgi:application
