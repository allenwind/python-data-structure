class Node:

    def __init__(self, next, prev, value):
        self.next = next 
        self.prev = prev
        self.value = value
        self.list = List

class List:

    def __init__(self, root, len):
        self.len = len
        self.root = root


# see golang/src/container/list.go