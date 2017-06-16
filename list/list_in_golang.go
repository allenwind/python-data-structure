// 参考Python的list接口在Golang下实现list

// length

// append
// clear
// copy
// count
// extend
// index
// insert
// pop
// remove
// reverse
// sort

package main

type Element struct {
	next, prev *Element
	list       *List
	location   int
	Value      interface{}
}

func (e *Element) Next() *Element {
	if p := e.next; e.list != nil && p != &e.list.root {
		return p
	}
	return nil
}

func (e *Element) Prev() *Element {
	if p := e.prev; e.list != nil && p != &e.list.root {
		return p
	}
	return nil
}

type List struct {
	root   Element
	length int
}

func (l *List) Init() *List {
	l.root.next = &l.root
	l.root.prev = &l.root
	l.length = 0
	return l
}

func New() *List { return new(List).Init() }

func (l *List) Length() int {
	return l.length
}

func (l *List) Insert(index int, v interface{}) {
	if l.Length()-index < 1 {
		return nil
	}
}
