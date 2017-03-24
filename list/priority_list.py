class PriorityQueue:

    def __init__(self, elist):
        self._elements = elist
        self._elements.sort(reverse=True)

    def enqueue(self, e): #可以使用二分查找
        i = self.length() - 1
        while i >= 0:
            if self._elements[i] <= e:
                i -= 1
            else:
                break
        self._elements.insert(i+1, e)

    def length(self):
        return len(self._elements)

    def is_empty(self):
        return not self._elements

    def peek(self):
        return self._elements[-1]

    def dequeue(self):
        return self._elements.pop()


