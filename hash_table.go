package main

import (
	"fmt"
)

type dictht struct {
	table    **dictEnrty
	size     uint
	sizemask uint
	used     uint
}

type dictEntry struct {
	key   interface{}
	value interface{}
	next  *dictEntry
}

type dict struct {
	ht [2]dictht
}
