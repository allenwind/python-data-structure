package main

import (
	"fmt"
	"time"
)

type Fib func(n uint) uint

func makeCache(f Fib) Fib {
	cache := make(map[uint]uint, 30)
	wrapper := func(n uint) uint {
		if r, ok := cache[n]; !ok {
			r := f(n)
			fmt.Println(cache)
			cache[n] = r
			return r
		} else {
			return r
		}
	}
	return wrapper
}

func fib(n uint) uint {
	if n == 0 || n == 1 {
		return 1
	} else {
		return fib(n-1) + fib(n-2)
	}
}

func main() {

	cache_fib := makeCache(fib)

	t1 := time.Now()
	fmt.Println(fib(30))
	fmt.Println("fib elapsed time", time.Since(t1))
	t2 := time.Now()
	fmt.Println(cache_fib(30))
	fmt.Println("cache_fib elapsed time", time.Since(t2))
}
