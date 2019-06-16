package main

type Node struct {
	Key         interface{}
	Value       interface{}
	left, right *Node
	Size        int
}

type Key interface {
	CompareTo() bool
}

func (node *Node) Size() int {
	return node.Size
}

type BST struct {
	root Node
}

func NewBST() *BST {
	bst := new(BST)
	bst.root.left = &bst.root
	bst.root.right = &bst.root
	bst.root.Size = 0
}

func (bst *BST) IsEmpty() bool {
	return bst.SizeRoot() == 0
}

func (bst *BST) SizeRoot() int {
	return bst.root.Size
}

func (bst *BST) SizeNode(node *Node) int {
	if node == nil {
		return 0
	} else {
		return node.Size
	}
}

func (bst *BST) Get(key interface{}) interface{} {
}
