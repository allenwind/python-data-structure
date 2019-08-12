package main

import (
	"fmt"
)

type Node struct {
	value interface{}
	next  *Node
}

type Stack struct {
	top    *Node
	length int
}

func NewStack() *Stack {
	stack := &Stack{
		top:    nil,
		length: 0,
	}
	return stack
}

func (s *Stack) Empty() bool {
	return s.top == nil
}

func (s *Stack) Len() int {
	return s.length
}

func (s *Stack) Push(value interface{}) {
	node := &Node{
		value: value,
		next:  s.top,
	}

	s.top = node
}

func (s *Stack) Pop() interface{} {
	if s.Empty() {
		return nil
	}
	item := s.top
	s.top = s.top.next
	return item
}

func (s *Stack) Top() interface{} {
	return s.top
}

func main() {
	stack := NewStack()
	stack.Push(1)
	stack.Push(2)
	stack.Push(3)
	fmt.Println(stack.Pop().(*Node).value)
	fmt.Println(stack.Pop().(*Node).value)
	fmt.Println(stack.Pop().(*Node).value)
}
