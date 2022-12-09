package main

import "fmt"

func main() {
	var n int
	fmt.Scanln(&n)

	for i := 1; i <= 100; i++ {
		if n%i == 0 {
			fmt.Println(i)
		}
	}
}
