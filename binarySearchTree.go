package main

type Node struct {
	key    string
	value  string
	left   *Node
	right  *Node
	length int
}

func (n *Node) compareTo(node *Node) {
	if n.key == node.key {
		return 0
	} else if n.key > node.key {
		return 1
	} else {
		return -1
	}
}

type Queue []*Node

func (q *Queue) Push(node *Node) {
	*q = append(*q, node)
}

func (q *Queue) Pop() *Node {
	n := len(*q)
	node := *q[0]
	*q = *q[1:n]
	return node
}

func (q *Queue) Len() int {
	return len(*q)
}

func (q *Queue) Empty() bool {
	return q.Len() == 0
}

type Stack []*Node

func (s *Stack) Push(node *Node) {
	*s = append(*s, node)
}

func (s *Stack) Empty() bool {
	return s.Len() == 0
}

func (s *Stack) Len() int {
	return len(*s)
}

func (s *Stack) Pop() *Node {
	n := len(*s)
	node := *s[n-1]
	*s = *s[0 : n-1]
	return node
}

func (s *Stack) Top() *Node {
	n := len(*s)
	return *s[n-1]
}

type BinarySearchTree struct {
	root *Node
}

func (tree *BinarySearchTree) Search(key string) {
	tree.search(tree.root, key)
}

func (tree *BinarySearchTree) search(node *Node, key string) {
}
