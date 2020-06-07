package main

import (
	"container/list"
	"fmt"
)

type LRUCache struct {
	Size  int
	list  *list.List
	cache map[string]*list.Element
}
type Entry struct {
	Key   string
	Value interface{}
}

func NewLRUCache(size int) *LRUCache {
	return &LRUCache{
		Size:  size,
		list:  list.New(),
		cache: make(map[string]*list.Element),
	}
}
func (c *LRUCache) Add(key string, value interface{}) {
	if c.cache == nil {
		c.cache = make(map[string]*list.Element)
		c.list = list.New()
	}
	// 获取到缓存后把它已到双链表最前，表示最热数据
	if e, ok := c.cache[key]; ok {
		c.list.MoveToFront(e)
		e.Value.(*Entry).Value = value
		return
	}
	entry := &Entry{Key: key, Value: value}
	e := c.list.PushFront(entry)
	c.cache[key] = e
	// 缓存有限，把最不热的数据移走
	if c.Size != 0 && c.list.Len() > c.Size {
		e := c.list.Back()
		if e != nil {
			c.list.Remove(e)
			delete(c.cache, e.Value.(*Entry).Key)
		}
	}
}
func (c *LRUCache) Get(key string) interface{} {
	if c.cache == nil {
		return nil
	}
	if e, ok := c.cache[key]; ok {
		c.list.MoveToFront(e)
		return e.Value.(*Entry).Value
	}
	return nil
}
func (c *LRUCache) Remove(key string) {
	if c.cache == nil {
		return
	}
	if e, ok := c.cache[key]; ok {
		c.list.Remove(e)
		delete(c.cache, e.Value.(*Entry).Key)
	}
}
func (c *LRUCache) Len() int {
	return c.list.Len()
}
func main() {
	cache := NewLRUCache(2)
	cache.Add("a", 1)
	cache.Add("b", 2)
	cache.Add("c", 3)
	fmt.Println(cache.Get("a"))
	fmt.Println(cache.Get("b"))
	fmt.Println(cache.Get("c"))
}
