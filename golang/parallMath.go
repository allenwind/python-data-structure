package main

import (
	"fmt"
	_ "runtime"
	_ "sync"
)

func sum(values []int, result chan int) {
	sum := 0
	for _, value := range values {
		sum += value
	}
	result <- sum
}

// 0-7 size 8
// 0-2 2-4 4-6 6-8
func parallize(values []int) int {
	//n := runtime.GOMAXPROCS(2)
	//fmt.Printf("parall size is %v\n", n)

	result := make(chan int, 2)

	length := len(values)
	go sum(values[:length/2], result)
	go sum(values[length/2:], result)

	sum := 0
	for item := range result {
		sum += item
	}

	return sum
}

func goparallize(c chan int, r chan int) {
	sum := 0
	for {
		number, ok := <-c
		if !ok {
			r <- sum
			return
		}
		sum += number
	}
}

func main() {
	values := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	r := make(chan int)
	c := make(chan int)

	go goparallize(c, r)
	go goparallize(c, r)

	for item := range values {
		c <- item
		println(item)
	}

	sum := 0
	for i := range r {
		sum += i
	}
	fmt.Println(sum)
}
