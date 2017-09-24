import heapq
import random

def last_k_number(seq, k):
    n = len(seq)
    heap = seq[:k]
    heapq.heapify(heap)
    for index in range(k, n-1):
        item = seq[index]
        heapq.heappush(heap, item)
        heapq.heappop(heap)
    return heap

def main():
    seq = [random.choice(range(20)) for _ in range(20)]
    heap = last_k_number(seq, 5)
    print(heap)
    print(sorted(seq)[::-1])

if __name__ == '__main__':
    main()
