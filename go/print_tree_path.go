package main

type Node struct {
	value string
	kids []*Node
}

func (e *Node) isLeaf() bool {
	return len(e.kids) == 0
}

func genRandomTree(root *Node, deep int, width int) {

}

func genTreePaths(root *Node, paths []string) {
	
}