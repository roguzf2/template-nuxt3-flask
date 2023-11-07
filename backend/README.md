# Flask template

## Features

This template uses [Python 3.10](https://docs.python.org/3.10/) and [Flask](https://flask.palletsprojects.com/en/2.2.x/) with the following libraries:

- [Flask-CORS](https://flask-cors.readthedocs.io/en/3.0.10/) - *"A Flask extension for handling Cross Origin Resource Sharing (CORS), making cross-origin AJAX possible."*

- [Gunicorn](https://docs.gunicorn.org/en/20.1.0/) - *"Gunicorn is a Python WSGI HTTP Server for UNIX."*

- [pandas](https://pandas.pydata.org/pandas-docs/version/1.5/index.html) - *"pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language."*

- [Requests](https://requests.readthedocs.io/en/stable/) - *"Requests is an elegant and simple HTTP library for Python, built for human beings."*

## Environment variables

### General variables

- `HOST` → The server binding host (default: `localhost`)

- `PORT` → The server binding port (default: `5000`)

### Development environment variables

- `DEBUG` → Boolean that indicates whether to run Flask server in debug mode (default: `1`)

## Running with `docker compose`

The configuration for integrating this project with Docker Compose is bellow. It assumes that you have the `docker-compose.yaml` file in the root folder of your project and that this Flask project is in a `./backend` folder.

### Development environment

```yaml
services:
  backend:
    build:
      context: "./backend"
      dockerfile: "dev.Dockerfile"
    restart: "unless-stopped"
    environment:
      - "DEBUG=$DEBUG"
      - "HOST=$BACKEND_HOST"
      - "PORT=$BACKEND_PORT"
    ports:
      - "$BACKEND_PORT:$BACKEND_PORT"
    volumes:
      - "./backend:/srv/app"
```

### Production environment

```yaml
services:
  backend:
    build:
      context: "./backend"
      dockerfile: "prod.Dockerfile"
    restart: "unless-stopped"
    environment:
      - "HOST=$BACKEND_HOST"
      - "PORT=$BACKEND_PORT"
    ports:
      - "$BACKEND_PORT:$BACKEND_PORT"
```

### Environment variables in the `.env` file

```py
# BACKEND
BACKEND_HOST="localhost"
BACKEND_PORT="5000"
DEBUG="1"
```
