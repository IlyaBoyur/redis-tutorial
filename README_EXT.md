# Расширенные возможности Redis


## Простой интерфейс
### Telnet
Мы можем взаимодействовать с Redis без всякого командного интерфейса, просто посылая команды по TCP-соединению или через telnet.  
Каждая команда должна завершаться знаками возврата каретки и перехода на новую строку (CRLF, или `\r\n`).  
```bash
$ telnet localhost 6379
Trying 127.0.0.1...
Connected to localhost.
Escape character is ‘^]’.
SET test hello
+OK
GET test
$5
hello
SADD stest 1 99
:2
SMEMBERS stest
*2
$1
1
$2
99
CTRL-]
```


### Конвейеры
Можно также передавать строки по одной, воспользовавшись программой netcat (nc).

```bash
$ (echo -en "ECHO hello \r\n") | nc localhost 6379 -q 1
$5
hello
```
**Конвейер** команд - организация посылки несколько команд в одном запросе.
```bash
$ (echo -en "PING\r\nPING\r\nPING\r\n") | nc  localhost 6379 -q 1
+PONG
+PONG
+PONG
```


### Публикация-подписка
`SUBSCRIBE <channel> [<channel> ...]` - установить соедиение с ключом - подписаться на **канал**  
`PUBLISH <channel> <message>` - опубликовать через канал произвольное строковое сообщение  


## Информация о сервере
`INFO` выводит сведения о сервере, в том числе номер версии, идентификатор процесса, объем занятой памяти и время с момента последнего перезапуска.  
```bash
27.0.0.1:6379> INFO
# Server
redis_version:7.2.3
redis_git_sha1:00000000
redis_git_dirty:0
redis_build_id:2b65d8a1f1ec58dc
redis_mode:standalone
os:Linux 6.2.0-39-generic x86_64
arch_bits:64
monotonic_clock:POSIX clock_gettime
multiplexing_api:epoll
atomicvar_api:c11-builtin
gcc_version:13.2.1
process_id:1
process_supervised:no
run_id:29327c5c7bfe5b0672f9a0c5d9a9be9943cb04ef
tcp_port:6379
server_time_usec:1703336458406465
uptime_in_seconds:15144
uptime_in_days:0
hz:10
configured_hz:10
lru_clock:8837642
executable:/data/redis-server
config_file:
io_threads_active:0
listener0:name=tcp,bind=*,bind=-::*,port=6379

# Clients
connected_clients:2
cluster_connections:0
maxclients:10000
client_recent_max_input_buffer:20480
client_recent_max_output_buffer:0
blocked_clients:0
tracking_clients:0
clients_in_timeout_table:0
total_blocking_keys:0
total_blocking_keys_on_nokey:0

# Memory
used_memory:1463320
used_memory_human:1.40M
used_memory_rss:5767168
used_memory_rss_human:5.50M
used_memory_peak:1479288
used_memory_peak_human:1.41M
used_memory_peak_perc:98.92%
used_memory_overhead:870824
used_memory_startup:865776
used_memory_dataset:592496
used_memory_dataset_perc:99.16%
allocator_allocated:1744088
allocator_active:2043904
allocator_resident:6336512
total_system_memory:16093212672
total_system_memory_human:14.99G
used_memory_lua:31744
used_memory_vm_eval:31744
used_memory_lua_human:31.00K
used_memory_scripts_eval:0
number_of_cached_scripts:0
number_of_functions:0
number_of_libraries:0
used_memory_vm_functions:32768
used_memory_vm_total:64512
used_memory_vm_total_human:63.00K
used_memory_functions:184
used_memory_scripts:184
used_memory_scripts_human:184B
maxmemory:0
maxmemory_human:0B
maxmemory_policy:noeviction
allocator_frag_ratio:1.17
allocator_frag_bytes:299816
allocator_rss_ratio:3.10
allocator_rss_bytes:4292608
rss_overhead_ratio:0.91
rss_overhead_bytes:-569344
mem_fragmentation_ratio:4.00
mem_fragmentation_bytes:4326144
mem_not_counted_for_evict:0
mem_replication_backlog:0
mem_total_replication_buffers:0
mem_clients_slaves:0
mem_clients_normal:3856
mem_cluster_links:0
mem_aof_buffer:0
mem_allocator:jemalloc-5.3.0
active_defrag_running:0
lazyfree_pending_objects:0
lazyfreed_objects:0

# Persistence
loading:0
async_loading:0
current_cow_peak:0
current_cow_size:0
current_cow_size_age:0
current_fork_perc:0.00
current_save_keys_processed:0
current_save_keys_total:0
rdb_changes_since_last_save:0
rdb_bgsave_in_progress:0
rdb_last_save_time:1703328516
rdb_last_bgsave_status:ok
rdb_last_bgsave_time_sec:0
rdb_current_bgsave_time_sec:-1
rdb_saves:2
rdb_last_cow_size:548864
rdb_last_load_keys_expired:0
rdb_last_load_keys_loaded:15
aof_enabled:0
aof_rewrite_in_progress:0
aof_rewrite_scheduled:0
aof_last_rewrite_time_sec:-1
aof_current_rewrite_time_sec:-1
aof_last_bgrewrite_status:ok
aof_rewrites:0
aof_rewrites_consecutive_failures:0
aof_last_write_status:ok
aof_last_cow_size:0
module_fork_in_progress:0
module_fork_last_cow_size:0

# Stats
total_connections_received:13
total_commands_processed:125
instantaneous_ops_per_sec:0
total_net_input_bytes:4018
total_net_output_bytes:213036
total_net_repl_input_bytes:0
total_net_repl_output_bytes:0
instantaneous_input_kbps:0.00
instantaneous_output_kbps:0.00
instantaneous_input_repl_kbps:0.00
instantaneous_output_repl_kbps:0.00
rejected_connections:0
sync_full:0
sync_partial_ok:0
sync_partial_err:0
expired_keys:2
expired_stale_perc:0.00
expired_time_cap_reached_count:0
expire_cycle_cpu_milliseconds:548
evicted_keys:0
evicted_clients:0
total_eviction_exceeded_time:0
current_eviction_exceeded_time:0
keyspace_hits:61
keyspace_misses:7
pubsub_channels:0
pubsub_patterns:0
pubsubshard_channels:0
latest_fork_usec:935
total_forks:2
migrate_cached_sockets:0
slave_expires_tracked_keys:0
active_defrag_hits:0
active_defrag_misses:0
active_defrag_key_hits:0
active_defrag_key_misses:0
total_active_defrag_time:0
current_active_defrag_time:0
tracking_total_keys:0
tracking_total_items:0
tracking_total_prefixes:0
unexpected_error_replies:0
total_error_replies:15
dump_payload_sanitizations:0
total_reads_processed:141
total_writes_processed:119
io_threaded_reads_processed:0
io_threaded_writes_processed:0
reply_buffer_shrinks:5
reply_buffer_expands:0
eventloop_cycles:150884
eventloop_duration_sum:34231547
eventloop_duration_cmd_sum:27123
instantaneous_eventloop_cycles_per_sec:9
instantaneous_eventloop_duration_usec:234
acl_access_denied_auth:0
acl_access_denied_cmd:0
acl_access_denied_key:0
acl_access_denied_channel:0

# Replication
role:master
connected_slaves:0
master_failover_state:no-failover
master_replid:3afd4703d342ef491e0553132518ff5925a9fc16
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:0
second_repl_offset:-1
repl_backlog_active:0
repl_backlog_size:1048576
repl_backlog_first_byte_offset:0
repl_backlog_histlen:0

# CPU
used_cpu_sys:23.984363
used_cpu_user:17.288891
used_cpu_sys_children:0.003979
used_cpu_user_children:0.007253
used_cpu_sys_main_thread:23.979530
used_cpu_user_main_thread:17.287670

# Modules

# Errorstats
errorstat_ERR:count=14
errorstat_WRONGTYPE:count=1

# Cluster
cluster_enabled:0

# Keyspace
db0:keys=18,expires=0,avg_ttl=0

```


## Настройка Redis
```bash
### /usr/local/etc/redis/redis.conf
# Если задать значение yes,
# то сервер будет работать в фоновом режиме и запишет идентифика-
# тор своего процесса в pid-файл
daemonize no
# номер порта сервера
port 6379
# В производственной системе лучше задать режим notice или warning
loglevel verbose
# В режиме демона лучше указать имя файла журнала
logfile stdout
# количество доступных баз данных Redis (пространств имен)
database 16
```


### Долговечность
Redis поддерживает несколько режимов сохранения. Прежде всего, это отсутствие сохранения вообще, когда все значения хранятся в оперативной памяти.
Одна из особенностей Redis – встроенная поддержка хранения значений на диске.
По умолчанию пары ключ-значение сохраняются лишь периодически.  

`LASTSAVE` - показать временную метку последнего сохранения на диск  
`SAVE` - сохранить базу данных на диск принудительно  

### Мгновенные снимки
Мы можем изменить частоту сохранения на диск, добавив, удалив или изменив одно из полей сохранения. По умолчанию таких полей 3, и все они начинаются ключевым словом save, за которым следует время в секундах и минимальное количество ключей, которые долж-
ны быть изменены, чтобы началась запись на диск.

```bash
# Значения в конфигурационном файле по умолчанию
# save <время в секундах> <число изменившихся за время ключей>
save 900 1
save 300 10
save 60 10000
```


### Файл с дозаписью
Redis поддерживает файл с дозаписью (appendonly.aof), в котором сохраняются все команды записи. Если сервер «грохнется», не записав значение, то при перезапуске он выполнит сохраненные команды, восстановив последнее состояние. Активация:  
```bash
### файл redis.conf
appendonly yes
```

как часто сбрасывать команды в файл:  
no - сбросом управляет операционная система  
always - кажда операция  
everysec - каждую секунду (компромисс)   
```bash
### файл redis.conf
# appendfsync always
appendfsync everysec
# appendfsync no
```


### Безопасность
```bash
### файл redis.conf
# переименование команды
rename-command FLUSHALL c283d93ac9528f986023793b411e4ba2
# подавление (отключение) команды
rename-command FLUSHALL ""
```


### Дополнительные параметры
Инструмент эталонного тестирования **redis-benchmark** по умолчанию подключается к порту 6379 на локальной машине и отправляет 10 000 запросов от имени 50 параллельно работающих клиентов. Увеличить количество запросов до 100 000 можно с помощью аргумента -n.

```bash
redis-benchmark -n 100000
```


## Репликация главный-подчиненный
По умолчанию сервер является главным, если не подчинить его какому-то другому.  
Данные реплицируются на произвольное число подчиненных серверов.
Настройка подчиненного сервера:  
1) Скопировать файл конфигураций  
```bash
$ cp redis.conf redis-s1.conf  
```
2) Внести изменения  
```bash
### файл redis.conf
slaveof <имя master контейнера> 6379
```

## Загрузка данных
Способы ускорения загрузки большого объема данных
1. **hiredis** - драйвер базы данных на С
```bash
$ pip install redis[hiredis]
```
Внести изменения  
```bash
### файл redis.conf
hiredis require
```
2. Конвейеризация  
Используя драйвер БД, создавать пакет из 1000 строк и вставлять его целиком, передавая конвейеру.

## Кластер Redis
Кластер позволяет хранить данные на разных серверах так, что для клиента эта логика не видна, фактический сервер вычисляется налету.  
Кластер поддерживает _согласованное хеширование_.  
Кластер управляется клиентом, а не самими серверами.    
Оба сервера играют роль главного (как в конфигурации по умолчанию). Все экземпляры redis должны быть сконфигурированы в режиме _cluster mode_:  
```bash
# файл redis.conf 
port 7000 # фактический порт ноды
cluster-enabled yes # включение режима кластера для ноды
cluster-config-file nodes.conf # путь до конфигурационного файла кластера (обновляется автоматически)
cluster-node-timeout 5000 # максимальное время недоступности ноды в кластере, мс
appendonly yes
```
Минимальный кластер должен содержать **3 master ноды**.  


### Запуск кластера
```bash
$ redis-cli --cluster create 127.0.0.1:7000 127.0.0.1:7001 127.0.0.1:7002 127.0.0.1:7003 127.0.0.1:7004 127.0.0.1:7005 --cluster-replicas 1
```

Пример клиента
```python
from redis.cluster import RedisCluster

rc = RedisCluster(host='localhost', port=6379)

print(rc.get_nodes())
# [[host=127.0.0.1,port=6379,name=127.0.0.1:6379,server_type=primary,redis_connection=Redis<ConnectionPool<Connection<host=127.0.0.1,port=6379,db=0>>>], ...

rc.set('foo', 'bar')
# True

rc.get('foo')
# b'bar'
```
Если запрашивать ключи через объект **redis.cluster.RedisCluster**, то клиент будет получать значение от правильного сервера.


## Фильтры Блума
Для проверки того, встречалось ли слово ранее, можно воспользоваться фильтром Блума.
**Фильтр Блума** – это вероятностная структура данных, которая проверяет существование элемента в множестве. Фильтр Блума может возвращать ложноположительный ответ, но никогда – ложноотрицательный. Это полезно, если требуется быстро установить, что значение не существует.

```python
res1 = r.bf().reserve("bikes:models", 0.01, 1000)
print(res1)  # >>> True

res2 = r.bf().add("bikes:models", "Smoky Mountain Striker")
print(res2)  # >>> True

res3 = r.bf().exists("bikes:models", "Smoky Mountain Striker")
print(res3)  # >>> True

res4 = r.bf().madd(
    "bikes:models",
    "Rocky Mountain Racer",
    "Cloudy City Cruiser",
    "Windy City Wippet",
)
print(res4)  # >>> [True, True, True]

res5 = r.bf().mexists(
    "bikes:models",
    "Rocky Mountain Racer",
    "Cloudy City Cruiser",
    "Windy City Wippet",
)
print(res5)  # >>> [True, True, True]
```
Плюс – возможность обнаруживать слова-**дубликаты**.  
Минус – время от времени просачиваются ложноположительные ответы – фильтр Блума может пропустить слово, которое никогда не встречалось.  
Поэтому в реальных приложениях выполняется дополнительная проверка, например, по более медленной базе данных в системе, куда записываются все данные. Но это будет происходить достаточно редко в предположении, что размер фильтра достаточно велик, а этот размер можно оценить заранее

## SETBIT и GETBIT
Команды `SETBIT`, `GETBIT` позволяют манипулировать битами в некоторой позиции битового вектора, позиции нумеруются с нуля.  
Этот способ часто применяется для быстрой пометки в многопараметрических системах – проще завести несколько битов, чем описывать всё строками.  
Методы лежат в основе поведения фильтра Блума:  
`SETBIT <key> <offset> <value>` - установить бит в значение `value` в ключе по заданному смещению  
`GETBIT <key> <offset>` - получить бит в ключе по заданному смещению  
