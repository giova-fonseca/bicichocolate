# Setup

```shell
docker-compose build && docker-compose up
```

# Development

```shell
docker-compse up
```

**NOTE:** This will wipe your database data.

```shell
rm -rf ./.docker
docker-compose down
docker system prune -a
docker-compose build
docker-compose up
```
