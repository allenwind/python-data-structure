import random
from functools import total_ordering

@total_ordering
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
    	return 'Node<{}>'.format(self.value)

    def __eq__(self, other):
    	return self.value == other.value

    def __gt__(self, other):
    	return self.value > other.value

def build_linked_list(values):
	if not values:
		return None
	root = Node(values[0])
	p_node = root
	for value in values[1:]:
		p_node.next = Node(value)
		p_node = p_node.next
	return root

def travel_list(linked):
	while linked:
		yield linked
		linked = linked.next

def sorted_linked_list(p_head1, p_head2):
	if p_head1 is None:
		return p_head2
	if p_head2 is None:
		return p_head1

	p_node = None # 没有必要在这里创建，仅用于表示
	if p_head1 < p_head2:
		p_node = p_head1
		p_node.next = sorted_linked_list(p_head1.next, p_head2)
	else:
		p_node = p_head2
		p_node.next = sorted_linked_list(p_head1, p_head2.next)
	return p_node

def main():
    p_head1 = build_linked_list(sorted(random.sample(range(20), 5)))
    p_head2 = build_linked_list(sorted(random.sample(range(20), 5)))

    for node in travel_list(p_head1):
        print(node)

    for node in travel_list(p_head2):
        print(node)

    p_head = sorted_linked_list(p_head1, p_head2)
    for node in travel_list(p_head):
        print(node)

if __name__ == '__main__':
	main()




