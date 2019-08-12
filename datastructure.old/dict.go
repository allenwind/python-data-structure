package main

type dictEntry struct {
	key   interface{}
	value interface{}
	next  *dictEntry
}

type dictht struct {
	table    **dictEntry
	size     uint
	sizemask uint
	used     uint
}

type dict struct {
	privdata  *interface{}
	ht        [2]dictht
	rehashidx uint
	iterators uint
}

type dictIterator struct {
	d                *dict
	index            uint
	table, safe      int
	entry, nextEntry dictEntry
	fingerprint      uint
}
