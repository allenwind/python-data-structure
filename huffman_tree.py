import heapq
import collections
import decimal
import string
import random
import binascii

from functools import total_ordering, partial

@total_ordering
class Node:

    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.tag = None
        self.left = None
        self.right = None

    def __eq__(self, node):
        return self.weight == node.weight

    def __gt__(self, node):
        return self.weight > node.weight

    def __repr__(self):
        return 'Node<{}>'.format(self.weight)

class PriorityQueue:

    def __init__(self, queue=None):
        if queue is not None:
            heapq.heapify(queue)
            self._q = queue
        else:
            self._q = []

    def push(self, item):
        heapq.heappush(self._q, item)

    def pop(self):
        return heapq.heappop(self._q)

    def empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._q)
    
class Stack:

    def __init__(self):
        self._q = []

    def push(self, item):
        self._q.append(item)

    def pop(self):
        if self.empty():
            return None
        return self._q.pop()

    def empty(self):
        return len(self._q) == 0

    def top(self):
        return self._q[-1]

def travel_tree_deeply(tree):
    if not tree:
        return
    stack = Stack()
    stack.push(tree)
    while not stack.empty():
        node = stack.pop()
        yield node
        if node.left:
            stack.push(node.left)
        if node.right:
            stack.push(node.right)

def _is_leaf_node(node):
    return bool(node.value)

def generate_nodes(weights):
    nodes = []
    for w in weights:
        nodes.append(Node(None, w))
    return nodes

def build_huffman_tree(nodes):
    heapq.heapify(nodes)
    while len(nodes) > 1:
        n1 = heapq.heappop(nodes)
        n2 = heapq.heappop(nodes)
        n1.tag = 1
        n2.tag = 0
        total_weight = n1.weight + n2.weight
        root = Node(None, total_weight)
        root.left = n1
        root.right = n2
        heapq.heappush(nodes, root)
    return nodes.pop()

def build_huffman_tree_with_priority_queue(nodes):
    queue = PriorityQueue(nodes)
    while len(queue) > 1:
        left_child = queue.pop()
        right_child = queue.pop()
        total_weight = left_child.weight + right_child.weight
        root = Node(None, total_weight)
        root.left = left_child
        root.right = right_child
        queue.push(root)
    return queue.pop()

def _generate_codes(node, prefix, codes):
    if _is_leaf_node(node):
        codes[node.value] = prefix
    else:
        left_prefix = prefix + '0'
        _generate_codes(node.left, left_prefix, codes)
        right_prefix = prefix + '1'
        _generate_codes(node.right, right_prefix, codes)

def counter(string):
    c = collections.Counter(string)
    length = len(string)
    m = {}
    for value, weight in c.items():
        weight = decimal.Decimal(weight) / length
        m[value] = weight
    return m

def generate_huffman_code(string):
    c = collections.Counter(string)
    length = len(string)
    nodes = []
    for value, weight in c.items():
        weight = decimal.Decimal(weight) / length
        nodes.append(Node(value, weight))
    tree = build_huffman_tree_with_priority_queue(nodes)
    codes = {}
    _generate_codes(tree, '', codes)
    return tree, codes

def generate_random_string(size):
    s = []
    template = string.ascii_letters
    for _ in range(size):
        s.append(random.choice(template))
    return ''.join(s)

def decode_huffman_codes(root, codes):
    p_node = root
    for code in codes:
        if code == '0':
            p_node = p_node.left
        else:
            p_node = p_node.right
            
        if _is_leaf_node(p_node):
            yield p_node.value
            p_node = root

def encode_string(string, codes):
    s = ''
    for code in string:
        s += codes[code]
    return s

def test_decode_huffman_codes(string):
    tree, codes = generate_huffman_code(string)
    encode_string = ''
    for code in string:
        encode_string += codes[code]
    print(string, '==>', encode_string)
    decode_string = decode_huffman_codes(tree, encode_string)
    print(encode_string, '==>', ''.join(decode_string))
     
def main():
    string = 'littlefeng'
    tree, codes = generate_huffman_code(string)
    print(codes)
    test_decode_huffman_codes('littlefeng')

def read_bytes(string):
    length = len(string)
    n = 0
    while n < length:
        yield string[n:n+8]
        n += 8

def compress_image(image=r'E:\picture\295.jpg'):
    fd = open(image, 'rb')
    data = binascii.b2a_qp(fd.read()).decode('utf-8')
    print("origin data", len(data))
    tree, codes = generate_huffman_code(data)
    print(codes)

    path = image + '_compress'
    fd = open(path, 'wb')
    encode_data = encode_string(data, codes)
    print("encode data", len(encode_data))
    print(len(encode_data)/len(data))
    buffer = []
    for byte in read_bytes(encode_data):
        buffer.append(int(byte, base=2))
    fd.write(bytes(buffer))
    fd.close()

def compress_image(image=r'E:\picture\295.jpg'):
    fd = open(image, 'rb')
    data = str(int(binascii.hexlify(fd.read()), base=16))
    print("origin data", len(data))
    tree, codes = generate_huffman_code(data)
    print(codes)

    path = image + '_compress'
    fd = open(path, 'wb')
    encode_data = encode_string(data, codes)
    print("encode data", len(encode_data))
    print(len(encode_data)/len(data))
    buffer = []
    for byte in read_bytes(encode_data):
        buffer.append(int(byte, base=2))
    fd.write(bytes(buffer))
    fd.close()

import collections

def print_tree_step(tree):
    stack = collections.deque()
    stack.append(tree)
    next_level_count = 0
    current_print_count = 1

    while len(stack):
        p_node = stack.popleft()
        print(p_node, end='\t')
        current_print_count -= 1
        if p_node.left is not None:
            next_level_count += 1
            stack.append(p_node.left)
        if p_node.right is not None:
            next_level_count += 1
            stack.append(p_node.right)
        if current_print_count == 0:
            current_print_count = next_level_count
            next_level_count = 0
            print('\n')

if __name__ == '__main__':
    main()


