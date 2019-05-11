package main

import (
	"fmt"
)

type Node struct {
	next, prev *Node
	freq       int
	list       *NodeList
	freqNode   *FreqNode
	key        string
	value      interface{}
}

type NodeList struct {
	root     Node
	len      int
	freqNode *FreqNode
}

func NewNodeList() *NodeList {
	l := new(NodeList)
	l.root.next = &l.root
	l.root.prev = &l.root
	l.len = 0
	return l
}

func (l *NodeList) Back() *Node {
	if l.len == 0 {
		return nil
	}
	return l.root.prev
}

func (l *NodeList) insert(e, at *Node) {
	n := at.next
	at.next = e
	e.prev = at
	e.next = n
	n.prev = e
	e.list = l
	l.len++
}

func (l *NodeList) remove(e *Node) *Node {
	e.prev.next = e.next
	e.next.prev = e.prev
	e.next = nil // avoid memory leaks
	e.prev = nil // avoid memory leaks
	e.list = nil
	l.len--
	return e
}

func (l *NodeList) AddToTail(node *Node) {
	fmt.Println(node)
	fmt.Println(l.root)
	l.insert(node, l.root.prev)
}

type FreqNode struct {
	next, prev   *FreqNode
	freq         int
	nodeList     *NodeList
	freqNodeList *FreqNodeList
}

func NewFreqNode(freq int, freqNodeList *FreqNodeList) *FreqNode {
	n := new(FreqNode)
	n.nodeList = NewNodeList()
	n.freq = freq
	n.freqNodeList = freqNodeList
	return n
}

func (n *FreqNode) Next() *FreqNode {
	if p := n.next; n.freqNodeList != nil && p != &n.freqNodeList.root {
		return p
	}
	return nil
}

type FreqNodeList struct {
	root FreqNode
	len  int
}

func NewFreqNodeList() *FreqNodeList {
	l := &FreqNodeList{
		root: FreqNode{
			freq:     0,
			nodeList: NewNodeList(),
		},
		len: 0,
	}
	l.root.next = &l.root
	l.root.prev = &l.root
	return l
}

func (l *FreqNodeList) MoveUp(node *Node) {
}

func (l *FreqNodeList) insert(e, at *FreqNode) {
	n := at.next
	at.next = e
	e.prev = at
	e.next = n
	n.prev = e
	e.freqNodeList = l
	l.len++
}

func (l *FreqNodeList) remove(e *FreqNode) *FreqNode {
	e.prev.next = e.next
	e.next.prev = e.prev
	e.next = nil // avoid memory leaks
	e.prev = nil // avoid memory leaks
	e.freqNodeList = nil
	l.len--
	return e
}

func (l *FreqNodeList) Back() *FreqNode {
	if l.len == 0 {
		return nil
	}
	return l.root.prev
}

func (l *FreqNodeList) Front() *FreqNode {
	if l.len == 0 {
		return nil
	}
	return l.root.next
}

func (l *FreqNodeList) AddToTail(freqNode *FreqNode) {
	l.insert(freqNode, l.root.prev)
}

type LFUCache struct {
	size         int
	cache        map[string]*Node
	freqNodeList *FreqNodeList
}

func NewLFUCache(size int) *LFUCache {
	return &LFUCache{
		size:         size,
		cache:        make(map[string]*Node),
		freqNodeList: NewFreqNodeList(),
	}
}

func (c *LFUCache) Put(key string, value interface{}) {
	node, ok := c.cache[key]
	// 存在就更新
	if ok {
		node.value = value
		node.freq++
		if node.freq == node.freqNode.Next().freq {
			nextNodeList := node.freqNode.Next().nodeList
			node.list.remove(node)
			nextNodeList.AddToTail(node)
		} else {
			/*freqNode := &FreqNode{
				freq:         node.freq,
				freqNodeList: c.freqNodeList,
				nodeList:     NewNodeList(),
			}*/
			freqNode := NewFreqNode(node.freq, c.freqNodeList)
			c.freqNodeList.insert(freqNode, node.freqNode.Next())
			freqNode.nodeList.AddToTail(node)
		}
		return
	}
	// 不存在的情况
	// 判断缓存是否满
	if len(c.cache) == c.size {
		tailList := c.freqNodeList.Back().nodeList
		tail := tailList.Back()
		tailList.remove(tail)
	}
	// 添加新的结点
	node = &Node{
		key:      key,
		value:    value,
		freq:     0,
		freqNode: c.freqNodeList.Back(),
	}
	c.cache[key] = node
	// tail freqNode的freq为0
	// c.freqNodeList.Back().freq == 0
	if c.freqNodeList.Back() == nil {
		/*freqNode := &FreqNode{
			freq:         node.freq,
			freqNodeList: c.freqNodeList,
			nodeList:     NewNodeList(),
		}*/
		freqNode := NewFreqNode(node.freq, c.freqNodeList)
		c.freqNodeList.AddToTail(freqNode)
		return
	}
	if c.freqNodeList.Back().freq == 0 {
		c.freqNodeList.Back().nodeList.AddToTail(node)
	} else {
		// tail freqNode的freq不为0
		/*freqNode := &FreqNode{
			freq:         node.freq,
			freqNodeList: c.freqNodeList,
			nodeList:     NewNodeList(),
		}*/
		freqNode := NewFreqNode(node.freq, c.freqNodeList)
		c.freqNodeList.AddToTail(freqNode)
	}
}

func (c *LFUCache) Get(key string) interface{} {
	node, ok := c.cache[key]
	if !ok {
		return nil
	}
	node.freq++
	if node.freq == node.freqNode.Next().freq {
		nextNodeList := node.freqNode.Next().nodeList
		node.list.remove(node)
		nextNodeList.AddToTail(node)
	} else {
		freqNode := &FreqNode{
			freq:         node.freq,
			freqNodeList: c.freqNodeList,
			nodeList:     NewNodeList(),
		}
		freqNode.nodeList.AddToTail(node)
	}
	return node.value
}

func main() {
	c := NewLFUCache(1)
	c.Put("a", 1)
	c.Put("b", 2)
	c.Get("a")
	c.Get("b")
}
