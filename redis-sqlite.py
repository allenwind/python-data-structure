import sqlite3
import random
import string
import time
import redis

from functools import wraps

script = \
'''
create table kv (
    key text unique not null,
    value text not null
    );
'''

class SQLiteKValue:
    
    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
        self.conn.executescript(script)

    def set(self, key, value):
        self.conn.execute("insert into kv values (?, ?)", (key, value))
        self.conn.commit()

    def get(self, key):
        value = self.conn.execute("select value from kv where key = ?", key).fetchone()
        if value:
            return value[0]

class RedisKValue:

    def __init__(self):
        self.r = redis.Redis()
        self.r.ping()

    def set(self, key, value):
        self.r.set(key, value)

    def get(self, key):
        return self.r.get(key)

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('elapsed time is {}'.format(end-start))
        return result
    return wrapper

@timethis
def test_SQLiteKValue(kv, size):
    for _ in range(size):
        key = ''.join(random.sample(string.ascii_letters, 30))
        kv.set(key, key)

@timethis
def test_RedisKValue(kv, size):
    for _ in range(size):
        key = ''.join(random.sample(string.ascii_letters, 30))
        kv.set(key, key)

if __name__ == '__main__':
    size = 10000
    redis_kv = RedisKValue()
    redis_kv.set('test', 'test')
    sqlite_kv = SQLiteKValue()
    print("SQLite")
    test_SQLiteKValue(sqlite_kv, size)
    print("Redis")
    test_RedisKValue(redis_kv, size)
