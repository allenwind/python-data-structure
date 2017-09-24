import threading

class RWLock:

    def __init__(self):
        self._lock = threading.Lock()
        self._write = False
        self._read_count = 0

    def rlock(self):
        if not self._write:
            return
        else:
            self._lock.acquire()
    def runlock(self):
        if not self._write:
            return
        else:
