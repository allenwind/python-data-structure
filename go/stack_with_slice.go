package main

import (
	"errors"
	"fmt"
)

type Stack struct {
	s      []int
	top    int
	length int
}

func (s *Stack) Push(item int) {
	s.s = append(s.s, item)
	s.top = item
	s.length += 1
}

func (s *Stack) Empty() bool {
	return s.length == 0
}

func (s *Stack) Pop() int {
	if s.Empty() {
		return 0
	}
	item := s.s[s.length-1]
	s.s = s.s[:s.length-1]
	s.length -= 1
	return item
}

func (s *Stack) Len() int {
	return s.length
}

func (s *Stack) Top() int {
	if s.Empty() {
		return 0
	} else {
		return s.top
	}
}

func NewStack() *Stack {
	stack := &Stack{
		s: make([]int, 0, 10),
	}
	return stack
}

func TestStack() {
	stack := NewStack()
	for i := 0; i <= 10; i++ {
		stack.Push(i)
	}

	for !stack.Empty() {
		fmt.Println(stack.Pop())
	}

	stack = nil
	fmt.Println(stack)
}

func main() {
	stack := make([]int, 0, 10)

	push := func(x int) error {
		n := len(stack)
		if n == cap(stack) {
			return errors.New("stack is full")
		}

		stack = stack[:n+1]
		stack[n] = x
		return nil
	}

	pop := func() (int, error) {
		n := len(stack)
		if n == 0 {
			return 0, errors.New("stack is empty")
		}

		x := stack[n-1]
		stack = stack[:n-1]
		return x, nil
	}

	push(1)
	push(2)
	push(3)
	fmt.Println(pop())
	fmt.Println(pop())

	s := NewStack()
	s.Push(1)
	s.Push(2)
	fmt.Println(s.Pop())
	fmt.Println(s.Pop())

	TestStack()
}
