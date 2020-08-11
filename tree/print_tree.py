class Queue:

    def __init__(self):
        self._q = []

    def push(self, item):
        self._q.append(item)

    def pop(self):
        if self.empty():
            return None
        item = self._q[0]
        del self._q[0]
        return item

    def empty(self):
        return len(self._q) == 0

    def __len__(self):
        return len(self._q)

def print_tree(root):
    if root is None:
        return

    queue = Queue()
    queue.push(root)
    next_level = 0
    has_to_print = 1
    while not queue.empty():
        node = queue.pop()
        print(node, end='\t')

        if node.left is not None:
            queue.push(node.left)
            next_level += 1
        if node.right is None:
            queue.push(node.right)
            next_level += 1
        has_to_print -= 1
        if not has_to_print:
            print()
            has_to_print = next_level
            next_level = 0

_sentinal = object()

def yield_tree(root):
    if root is None:
        return
    queue = Queue()
    queue.push(root)
    next_level = 0
    has_to_print = 1
    while not queue.empty():
        node = queue.pop()
        yield node

        if node.left is not None:
            queue.push(node.left)
            next_level += 1
        if node.right is not None:
            queue.push(node.right)
            next_level += 1
        has_to_print -= 1
        if not has_to_print:
            yield _sentinal
            has_to_print = next_level
            next_level = 0

def print_yield_tree(gen):
    data = []
    for node in gen:
        if node is not _sentinal:
            data.append(str(node))
        else:
            print(' '.join(data).center(100))
            data = []