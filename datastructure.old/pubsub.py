import threading
import queue
import time

from collections import defaultdict
from contextlib import contextmanager

class Exchange:

    def __init__(self):
        self._subscribers = set()

    def attach(self, task):
        self._subscribers.add(task)

    def detach(self, task):
        self._subscribers.remove(task)

    def send(self, msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)

    @contextmanager
    def subscribe(self, *tasks):
        for task in tasks:
            self.attach(task)
        try:
            yield
        finally:
            for task in tasks:
                self.detach(task)

_exchanges = defaultdict(Exchange)

def get_exchange(name):
    return _exchanges[name]

class Task:

    def __init__(self, name):
        self.name = name

    def send(self, msg):
        print(self.__class__.__name__, self.name, msg)

class Actor(threading.Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self._queue = queue.Queue()
        self._run = True

    def run(self):
        while self._run:
            job = self._queue.get()
            # do job
            print(job)

    def send(self, job):
        self._queue.put(job)

    def shutdown(self):
        self._run = False

def test_task():

    task1 = Task('task1')
    task2 = Task('task2')
    exchange = get_exchange('exchange')
    exchange.attach(task1)
    exchange.attach(task2)

    exchange.send('message')
    exchange.detach(task1)
    exchange.send('message')

    with exchange.subscribe(task1, task2):
        exchange.send('message1')
        exchange.send('message2')

def test_actor():

    actor1 = Actor("actor1")
    actor2 = Actor("actor2")

    actor1.start()
    actor2.start()

    exchange = get_exchange("exh")
    exchange.attach(actor1)
    exchange.attach(actor2)

    exchange.send('message')
    exchange.detach(actor1)
    exchange.send('message2')

if __name__ == '__main__':
    
    # test_task()
    test_actor()
    time.sleep(2)
    
