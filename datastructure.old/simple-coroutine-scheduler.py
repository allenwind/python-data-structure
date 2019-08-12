from collections import deque
from queue import PriorityQueue

def printer(nums):
    print('printer start')
    for item in nums:
        yield item
    print('printer end')

class CoroutineScheduler:

    def __init__(self):
        self._task_queue = deque()

    def add_task(self, task):
        self._task_queue.append(task)

    def run(self):
        while self._task_queue:
            task = self._task_queue.popleft()
            try:
                result = next(task)
                print(result)
                self._task_queue.append(task)
            except StopIteration:
                pass

class CoroutinePriorityScheduler:

    def __init__(self):
        self._task_queue = PriorityQueue()

    def add_task(self, task, priority):
        self._task_queue.append((priority, task))

    def run(self):
        while self._task_queue:
            priority, task = self._task_queue.popleft()
            try:
                result = next(task)
                print(result)
                if priority > 0:
                    priority = priority - 1
                self._task_queue.append((priority, task))
            except StopIteration:
                pass

def print_worker():
    printer1 = printer([1, 3, 5, 7, 9])
    printer2 = printer([2, 4, 6, 8, 10])

    scheduler = CoroutineScheduler()
    scheduler.add_task(printer1)
    scheduler.add_task(printer2)
    scheduler.run()

if __name__ == '__main__':
    print_worker()

    
