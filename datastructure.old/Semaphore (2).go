package main

import (
	"fmt"
	"sync"
	"time"
)

type Semaphore struct {
	condition sync.Cond
	value     int
	mutex     sync.Mutex
}

func NewSemaphore(value int) *Semaphore {
	s := new(Semaphore)
	s.value = value
	s.mutex = sync.Mutex{}
	s.conditon = sync.NewCond(m)
	return s
}

func (s *Semaphore) Acquire(blocking bool, timeout time.Time) {

}

func (s *Semaphore) Release() {
}
