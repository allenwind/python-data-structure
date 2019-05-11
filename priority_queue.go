package main

import (
	"fmt"
)

type Node struct {
	value  string
	weight int
	left   *Node
	right  *Node
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

type PriorityQueue struct {
	array  []*Node
	length int
}

func (pq *PriorityQueue) Len() int {
	return pq.length
}

func (pq *PriorityQueue) Empty() bool {
	return pq.length == 0
}

func (pq *PriorityQueue) Exch(i, j int) {
	pq.array[i], pq.array[j] = pq.array[j], pq.array[i]
}

func (pq *PriorityQueue) Less(i, j int) bool {
	if pq.array[i].weight < pq.array[j].weight {
		return true
	} else {
		return false
	}
}

func (pq *PriorityQueue) Swim(k int) {
	for k > 1 && pq.Less(k/2, k) {
		pq.Exch(k/2, k)
		k = k / 2
	}
}

func (pq *PriorityQueue) Sink(k int) {
	for 2*k <= pq.length {
		j := 2 * k
		if j < pq.length && pq.Less(j, j+1) {
			j += 1
		}
		if !pq.Less(k, j) {
			break
		}
		pq.Exch(k, j)
		k = j
	}
}

func (pq *PriorityQueue) Push(node *Node) {
	pq.array = append(pq.array, node)
	pq.length += 1
	pq.Swim(pq.length)
}

func (pq *PriorityQueue) Pop() *Node {
	if pq.Empty() {
		return nil
	}
	item := pq.array[1]
	pq.Exch(1, pq.length)
	pq.length -= 1
	pq.array = pq.array[0:pq.length]
	pq.Sink(1)
	return item
}

func NewPriorityQueue(size int) *PriorityQueue {
	array := make([]*Node, size)
	array = append(array, &Node{})
	pq := &PriorityQueue{
		array:  array,
		length: 0,
	}
	return pq
}

func main() {
	queue := NewPriorityQueue(10)
	node := &Node{
		weight: 1,
	}
	node2 := &Node{
		weight: 2,
	}

	queue.Push(node)
	queue.Push(node2)
	fmt.Println(queue.Pop())
	fmt.Println(queue.Pop())
}
