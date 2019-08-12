import random

class Heap:

    def __init__(self, values):
        array = [None]
        array.extend(values)
        self._heap = array
        self.n = len(self._heap) - 1

    def __len__(self):
        return self.n

    def empty(self):
        return self.n == 0

    def exch(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def less(self, i, j):
        return self._heap[i] < self._heap[j]

    def swim(self, k):
        while k > 1 and self.less(k//2, k):
            self.exch(k//2, k)
            k = k // 2

    def sink(self, k):
        while 2*k <= self.n:
            j = 2 * k
            if j < self.n and self.less(j, j+1):
                j += 1
            if not self.less(k, j):
                break
            self.exch(k, j)
            k = j

    def push(self, item):
        self._heap.append(item)
        self.n += 1
        self.swim(self.n)

    def pop(self):
        if self.empty():
            return None
        item = self._heap[1]
        self.exch(1, self.n)
        del self._heap[self.n]
        self.n -= 1
        self.sink(1)
        return item

    def merge(self, queue):
        pass
        

def main():
    heap = Heap([])
    for _ in range(100):
        item = random.randint(1, 100)
        heap.push(item)

    for i in heap._heap[1:]:
        print(i, end=' ')
    print()
    while not heap.empty():
        print(heap.pop(), end=' ')

if __name__ == '__main__':
    main()
    

