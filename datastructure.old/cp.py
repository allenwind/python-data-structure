import threading
import queue
import time
import random
import string

_sentinel = object()

class Consumer(threading.Thread):
    def __init__(self, q):
        self.q = q
        super().__init__(daemon=True)

    def run(self):
        while True:
            e = self.q.get()
            print('consume:{} by thread<{}>'.format(e, threading.current_thread().ident))
            self.q.task_done()
            time.sleep(random.random())

class Producer(threading.Thread):
    def __init__(self, q):
        self.q = q
        super().__init__(daemon=True)

    def run(self):
        while True:
            e = random.choice(string.ascii_letters)
            self.q.put(e)
            print('produce:{} by thread<{}>'.format(e, threading.current_thread().ident))
            time.sleep(random.random())

def main():
    q = queue.Queue(maxsize=10)
    producer = Producer(q)
    consumer = Consumer(q)
    producer.start()
    consumer.start()

    time.sleep(3)

    q.join()
    print('queue is empty, so quit', flush=True)

if __name__ == '__main__':
    main()