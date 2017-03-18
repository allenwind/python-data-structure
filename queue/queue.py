class Full(Exception):
    pass

class Empty(Exception):
    pass


class Queue:
    
    def __init__(self, maxsize=0):
        pass

    def qsize(self):
        pass

    def is_empty(self):
        pass

    def full(self):
        pass

    def put(self):
        pass

    def get(self):
        pass

    def clear(self):
        pass

class PriorityQueue(Queue):
    pass

class LifoQueue(Queue):
    pass
