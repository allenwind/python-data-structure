package main

import (
	"fmt"
	"time"
)

func fib(n uint) uint {
	if n == 0 || n == 1 {
		return 1
	} else {
		return fib(n-1) + fib(n-2)
	}
}

type Fib func(n uint) uint

func timedFunc(f Fib) Fib {
	return func(n uint) uint {
		defer func(t time.Time) {
			fmt.Println("elapsed time is ", time.Since(t))
		}(time.Now())
		return f(n)
	}
}

func main() {
	fib_timer := timedFunc(fib)
	fmt.Println(fib_timer(30))
}
