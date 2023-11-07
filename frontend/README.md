# Nuxt template

## Features

This template uses [Nuxt 3](https://nuxt.com/) and [Typescript](https://www.typescriptlang.org/) with the following plugins:

- [Vuetify 3](https://vuetifyjs.com/) - *"Vuetify is a no design skills required UI Library with beautifully handcrafted Vue Components."*

- [Plinia](https://pinia.vuejs.org/) - *"The intuitive store for Vue.js. Type Safe, Extensible, and Modular by design. Forget you are even using a store."*

As development plugins, this template also uses:

- [Prettier](https://prettier.io/) - *"An opinionated code formatter."*

- [ESLint](https://eslint.org/) - *"The pluggable linting utility for JavaScript and JSX."*

## Environment variables

### General variables

- `HOST` → The server binding host (default: `localhost`)

- `PORT` → The server binding port (default: `3000`)

- `BASE_URL` → A variable to help setting a base URL for requests (default: `undefined`)

## Running with `docker compose`

The configuration for integrating this project with Docker Compose is bellow. It assumes that you have the `docker-compose.yaml` file in the root folder of your project and that this Nuxt.js project is in a `./frontend` folder.

### Development environment

```yaml
services:
  frontend:
    build:
      context: "./frontend"
      dockerfile: "dev.Dockerfile"
    restart: "unless-stopped"
    environment:
      - "HOST=$FRONTEND_HOST"
      - "PORT=$FRONTEND_PORT"
      - "NUXT_PUBLIC_BASE_URL=$BASE_URL"
    ports:
      - "$FRONTEND_PORT:$FRONTEND_PORT"
    volumes:
      - "./frontend:/srv/app"
```

### Production environment

```yaml
services:
  frontend:
    build:
      context: "./frontend"
      dockerfile: "prod.Dockerfile"
    restart: "unless-stopped"
    environment:
      - "HOST=$FRONTEND_HOST"
      - "PORT=$FRONTEND_PORT"
      - "NUXT_PUBLIC_BASE_URL=$BASE_URL"
    ports:
      - "$FRONTEND_PORT:$FRONTEND_PORT"
```

### Environment variables in the `.env` file

```py
# FRONTEND
FRONTEND_HOST="0.0.0.0"
FRONTEND_PORT="3000"
BASE_URL=
```
