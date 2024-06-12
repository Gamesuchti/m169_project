# M169 Projekt - Docker Compose Anleitung

## Voraussetzungen

Bevor man beginnt, sollte man sicher stellen, dass man Folgendes auf dem System installiert hat:

- Docker: [Docker installieren](https://docs.docker.com/get-docker/)
- Docker Compose: [Docker Compose installieren](https://docs.docker.com/compose/install/)

## Anleitung

Folgende Schritte befolgen, um die To-Do App mit Docker Compose auszuführen:

1. **Repository clonen**

   ```
   git clone https://github.com/Gamesuchti/m169_project.git
   cd m169_project
   ```

2. **Container starten**

   Docker Compose verwenden, um die Container im Hintergrund zu starten:

   ```
   docker-compose up -d
   ```
3. **Container stoppen**

   Docker Compose down verwenden, um die Container zu stoppen:

   ```
   docker-compose down
   ```
