# EduEvent

Main EduEvent repo.

## Running Project

To run this project you first need to have [docker](https://www.docker.com/) and [docker compose](https://docs.docker.com/compose/) installed.

### Dev

Development mode allows you to start the project with HMR (Hot Module Reload) which allows you to see changes as soon as you save a project file.

You build the project in develepment mode by running this command in the root of the repo.

```bash
docker compose -f docker-compose.yaml -f docker-compose.dev.yaml up --build
```

This will also automatically start the containers. To stop them you just exit out of the process.

To later start the project in develepment mode you use this command in the root of the repo.

```bash
docker compose -f docker-compose.yaml -f docker-compose.dev.yaml up
```

To stop the containers you just exit from the process.

When the containers are running you can access the Next.js frontend at `localhost:3000` and FastAPI backend at `localhost:8000`.

Note that when you add any new dependency to `requirements.txt` you need to rebuild the containers.

### Building

You build the project by running this command in the root of the repo.

```bash
docker compose up --build
```

This will also automatically start the containers. To stop them you just exit out of the process.

To later start the project you use this command in the root of the repo.

```bash
docker compose up
```

To stop the containers you just exit from the process.

When the containers are running you can access the Next.js frontend at `localhost:3000` and FastAPI backend at `localhost:8000`.

### Rebuilding

To rebuild containers you first need to run:

```bash
docker compose down -v
```

This deletes the existing containers.

Then you normally build the project.
