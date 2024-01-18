import redis

red = redis.Redis(
    host='redis-14785.c302.asia-northeast1-1.gce.cloud.redislabs.com:',
    port=14785,
    password='vypTosFLko7LJnwYYwPAr9857Am7OGR4'
)

red.set('var1', 'value1')  # записываем в кеш строку "value1"
print(red.get('var1'))  # считываем из кэша данные