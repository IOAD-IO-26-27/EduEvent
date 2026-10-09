# EduEvent

Main EduEvent repo.

## Running Project

To run this project you first need to have [docker](https://www.docker.com/) and [docker compose](https://docs.docker.com/compose/) installed.

### Dev

todo

### Building

You build the project by running this command in the root of the repo.

```bash
docker compose up --build
```

This will also automatically start the containers. To stop them you just quit out of the process.

To later start the project you use this command in the root of the repo.

```bash
docker compose start
```

This will start the containers in the background, so to stop them you need to run this command.

```bash
docker compose stop
```

When the containers are running you can access the Next.js frontend at `localhost:3000` and FastAPI backend at `localhost:8000`.
