# 139 cp

import heapq

with open('file1', 'rt') as f1, open('file2', 'rt') as f2, open('file3', 'rt') as f3:
for line in heapq.merge(f1, f2):
    f3.write(line)