import redis
import collections
import time

class FileSync:

    aggregates = collections.defaultdict(lambda: collections.defaultdict(int))

    def __init__(self):
        self._conn = redis.Redis()

    def daily_country_aggregate(self, line):
        if not line:
            return
        ip, day, time, achievement = line.split()
        country = ip
        self.aggregates[day][country] += 1

        for day, aggregate in self.aggregates.items():
            self._conn.zadd('daily:country:'+day, **aggregate)
            del self.aggregates

    def create_chat(self, source, obj, s, channel):
        pass

    def _clean(self, channel, waiting, count):
        pass

    def send_message(self, channel, source, logfile):
        pass

    def copy_logs_to_redis(self, path, channel, count=10, limit=2**30, quit_when_done=True):
        bytes_in_redis = 0
        waiting = collections.deque()
        self.create_chat('source', map(str, range(count)), '', channel)
        count = str(count)
        for logfile in sorted(os.listdir(path)):
            full_path = os.path.join(path, logfile)
            fsize = os.stat(full_path).st_size
            while bytes_in_redis + fsize > limit:
                cleaned = self._clean(channel, waiting, count)
                if cleaned:
                    bytes_in_redis -= cleaned
                else:
                    time.sleep(0.25)
            with open(full_path, 'rb') as inp:
                block = ' '
                while block:
                    block = inp.read(2**17)
                    self._conn.append(channel+logfile, block)
            self.send_message(channel, 'source', logfile)

            bytes_in_redis += fsize
            waiting.append((logfile, fsize))

        if quit_when_done:
            self.send_message(channel, 'source', ':done')

        while waiting:
            cleaned = self._clean(channel, waiting, count)
            if cleaned:
                bytes_in_redis -= cleaned
            else:
                time.sleep(0.25)


















            
                
                    
