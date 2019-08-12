package main

import (
	"bytes"
	"sync"
	"sync/atomic"
)

const (
	loadFactor     float64 = 0.8
	bucketNumber   int     = 16
	bucketMaxSize  uint64  = 1000
	maxConcurrency int     = 65536
)

type Bucket interface {
	Put(p Pair, lock sync.Locker) (bool, error)
	Get(key string) Pair
	GetFirstPair() Pair
	Delete(key string, lock sync.Locker) bool
	Clear(lock sync.Locker)
	Size() uint64
	String() string
}
