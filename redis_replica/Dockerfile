FROM redis:7.2.3-alpine
COPY redis_replica.conf /usr/local/etc/redis/redis.conf
CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]