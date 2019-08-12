package main

type Element struct {
	next *Element
	list *List

	Value interface{}
}

func (e *Element) Next() *Element {
	if p := e.next; e.list != nil && p != &e.list.root {
		return p
	}
	return nil
}

// List's Head
type Head struct {
	next *Element
	tail *Element
}

type List struct {
	root Head
	len  int
}

func (l *List) Init() *List {
	l.root.next = &l.root
	l.root.tail = &l.root
	l.len = 0
	return l
}

func (l *List) Len() int {
	return l.len
}

func (l *List) Front() *Element {
	if l.len == 0 {
		return nil
	}
	return l.root.next
}

func (l *List) Back() *Element {
	if l.len == 0 {
		return nil
	}
	return l.root.tail
}

func (l *List) insert(e, at *Element) *Element {
	// 在元素at后插入值e元素
	n := at.next

	// 如果at是最后一个元素，修改tail
	if at == l.root.tail {
		l.root.tail = e
	}

	at.next = e
	e.next = n
	l.len++
	return e
}

func (l *List) insertValue(value interface{}, at *Element) *Element {
	return l.insert(&Element{Value: value}, at)
}

func (l *List) remove(e *Element) *Element {
	// 单链表诡异的地方到了
	//
	if l.root.tail == e {
		// 最后结点的处理方法
		// 如果不使用sential方法
		// 这种情况只能遍历了

	}
	n = e.next
	e.Value = n.Value
	e.next = n.next
	l.len--
	return e
}

func (l *List) Remove(e *Element) interface{} {
	if e.list == l {
		l.remove(e)
	}
	return e.Value
}

func (l *List) PushFront(v interface{}) *Element {
	return l.insertValue(v, &l.root)
}

func (l *List) PushBack(v interface{}) *Element {
	return l.insertValue(v, l.root.prev)
}

func (l *List) InsertAfter(v interface{}, mark *Element) *Element {
	if mark.list != l {
		return nil
	}
	return l.insertValue(v, mark)
}

func (l *List) Pop() *Element {
}

func (l *List) Popleft() *Element {
}

func (l *List) Clear() *List {
}

func (l *List) reverse() *List {
}

func (l *List) Reverse() *List {
}

func (l *List) Index(e *Element) int {
}

func (l *List) extend(lst *List) *List {
}

func (l *List) sort() {
}
