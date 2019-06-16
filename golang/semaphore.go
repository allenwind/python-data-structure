package main

import (
	"fmt"
	"time"
)

type Semaphore chan struct{}

func (s Semaphore) acquire() {
	s <- struct{}{}
}

func (s Semaphore) release() {
	<-s
}

func NewSemaphore(value uint) Semaphore {
	// 原则上，value值不能为负数
	return make(Semaphore, value)
}

func main() {
	s := NewSemaphore(2)
	go func() {
		s.acquire()
		defer s.release()
		time.Sleep(time.Second)
		fmt.Println("goroutine 1")
	}()

	go func() {
		s.acquire()
		defer s.release()
		time.Sleep(2 * time.Second)
		fmt.Println("goroutine 2")
	}()

	fmt.Println("wait here")
	s.acquire()
	fmt.Println("acquire semaphore success")
	time.Sleep(time.Second)
}
