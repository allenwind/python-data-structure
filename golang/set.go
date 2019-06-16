package main

import (
	"fmt"
)

type Set map[int]struct{}

func NewSet() Set {
	return Set{}
}

func (s Set) Add(n int) {
	s[n] = struct{}{}
}

func (s Set) Del(n int) {
	delete(s, n)
}

func (s Set) Len() int {
	return len(s)
}

func main() {
	s := NewSet()
	s.Add(1)
	fmt.Println(s)
	
	s.Del(1)
	fmt.Println(s.Len())
}