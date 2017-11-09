package main

import (
	"fmt"
	"sync"
	"time"
)

type Semaphore struct {
	value int
	cond  *sync.Cond
}

func NewSemaphore(value int) *Semaphore {
	if value < 0 {
		panic("semaphore initial value must be >= 0")
	}
	mutex := new(sync.Mutex)
	semaphore := &Semaphore{
		value: value,
		cond:  sync.NewCond(mutex),
	}
	return semaphore
}

func (s *Semaphore) acquire(blocking bool, timeout time.Time) bool {
}

func (s *Semaphore) release() {
}
