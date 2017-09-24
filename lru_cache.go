package main

import (
	"fmt"
)

type Node struct {
	key   string
	value string
	next  *Node
	prev  *Node
}

type List struct {
	root Node
	len  int
}

func NewList() *List {
	l := new(List)
	l.root.next = &l.root
	l.root.prev = &l.root
	l.len = 0
	return l
}

func (l *List) Len() int {
	return l.len
}

func (l *List) Front() *Node {
	if l.len == 0 {
		return nil
	}
	return l.root.next
}

func (l *List) insert(e, at *Node) *Node {
	n := at.next
	at.next = e
	e.prev = at
	e.next = n
	n.prev = e
	l.len++
	return e
}

func (l *List) remove(e *Node) *Node {
	e.prev.next = e.next
	e.next.prev = e.prev
	e.next = nil
	e.prev = nil
	l.len--
	return e
}

func (l *List) moveToBack(e *Node) {
	if l.root.prev == e {
		return
	}
	l.insert(l.remove(e), l.root.prev)
}

func (l *List) appendToBack(e *Node) {
	l.insert(e, l.root.prev)
}

type LRUCache struct {
	data map[string]*Node
	root *List
	size int
}

func NewLRUCache(size int) *LRUCache {
	cache := new(LRUCache)
	cache.size = size
	cache.root = NewList()
	cache.data = make(map[string]*Node, size)
	return cache
}

func (cache *LRUCache) Put(key, value string) {
	node, ok := cache.data[key]
	if ok {
		node.value = value
		cache.root.moveToBack(node)
		return
	}
	if cache.size == len(cache.data) {
		temp := cache.root.Front()
		cache.root.remove(temp)
		delete(cache.data, temp.key)
	}
	node = &Node{
		key:   key,
		value: value,
	}
	cache.root.appendToBack(node)
	cache.data[key] = node
}

func (cache *LRUCache) Get(key string) string {
	node, ok := cache.data[key]
	if ok {
		cache.root.moveToBack(node)
		return node.value
	}
	return ""
}

func main() {
	cache := NewLRUCache(2)
	cache.Put("1", "1")
	cache.Put("2", "2")
	fmt.Println(cache.Get("1"))

	cache.Put("3", "3")
	fmt.Println(cache.Get("2"))
	fmt.Println(cache.data)

	cache.Put("4", "4")
	fmt.Println(cache.data)

	fmt.Println(cache.Get("1"))
	fmt.Println(cache.Get("3"))
	fmt.Println(cache.Get("4"))

}
