package main

import (
	"fmt"
)

type Node struct {
	key   rune
	child []*Node
}

func (n *Node) compareTo(key string) int {
	if n.key == key {
		return 0
	} else if n.key > key {
		return 1
	} else {
		return -1
	}
}

func (n *Node) findChild(key string) *Node {
	for _, node := range n.child {
		if node.compareTo(key) == 0 {
			return node
		}
		return nil
	}
}

type Trie struct {
	root Node
}

func (t *Trie) insert(key string) {
	node := t.root
	for _, c := range key {
		newNode := node.findChild(c)
		if newNode != nil {
			node = newNode.child
		} else {
			newNode = &Node{
				key: c,
			}
			node = append(node, newNode)
			node = newNode.child
		}
	}
}

func NewTrieTree() *Trie {
	tree := &Trie{
		root: Node{},
	}
	return tree
}

func main() {
	tree := NewTrieTree()
	tree.insert("allenwind")
}
