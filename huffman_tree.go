package main

import (
	"container/heap"
	"fmt"
	_ "math/big"
)

type Node struct {
	value  string
	weight float64
	left   *Node
	right  *Node
	index  int
}

func (n *Node) compareTo(node *Node) int {
	if n.weight == node.weight {
		return 0
	} else if n.weight > node.weight {
		return 1
	} else {
		return -1
	}
}

type PriorityQueue []*Node

func (pq PriorityQueue) Len() int {
	return len(pq)
}

func (pq PriorityQueue) Less(i, j int) bool {
	return pq[i].weight <= pq[j].weight
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}

func (pq *PriorityQueue) Push(x interface{}) {
	n := len(*pq)
	node := x.(*Node)
	node.index = n
	*pq = append(*pq, node)
}

func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	node := old[n-1]
	node.index = -1
	*pq = old[0 : n-1]
	return node
}

func build_huffman_tree(nodes map[string]float64) *Node {
	pq := make(PriorityQueue, len(nodes))
	i := 0
	for value, weight := range nodes {
		pq[i] = &Node{
			value:  value,
			weight: weight,
			index:  i,
		}
		i++
	}
	heap.Init(&pq)

	for pq.Len() > 1 {
		leftChild := heap.Pop(&pq).(*Node)
		rightChild := heap.Pop(&pq).(*Node)
		totalWeight := leftChild.weight + rightChild.weight
		root := &Node{
			weight: totalWeight,
			left:   leftChild,
			right:  rightChild,
		}
		fmt.Println(root.weight)
		heap.Push(&pq, root)
	}

	return heap.Pop(&pq).(*Node)
}

func generateCodes(node *Node, prefix string, codes map[string]string) {
	if node.value != "" {
		codes[node.value] = prefix
	} else {
		leftPrefix := prefix + "0"
		generateCodes(node.left, leftPrefix, codes)
		rightPrefix := prefix + "1"
		generateCodes(node.right, rightPrefix, codes)
	}
}

func generateHuffmanCodes(s string) map[string]string {

	counter := make(map[string]float64)
	// length := float64(len(s))

	for i := 0; i < len(s); i++ {
		counter[string(s[i])] = counter[string(s[i])] + 1.0
	}

	/*
		for k, v := range counter {
			counter[k] = v / length
		}
	*/
	fmt.Println(counter)

	tree := build_huffman_tree(counter)
	codes := make(map[string]string)
	generateCodes(tree, "", codes)
	return codes
}

func main() {
	codes := generateHuffmanCodes("mrfenglovechenchen")
	fmt.Println(codes)
}
