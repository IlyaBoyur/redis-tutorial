# Шпоргалка Redis

## Подключение

```bash
# Поднять контейнер с базой Redis в текущей папке
$ docker compose up -d --remove-orphans
$ docker compose exec -it redis sh
/data \# redis-cli
127.0.0.1:6379> PING
PONG
```


