package main

import (
	"fmt"
)

func main() {
	a := 10
	b := 20
	c := 30

	fmt.Println(a > b && b < c)
	fmt.Println(a > b || b < c)
	fmt.Println(!(a > b && b < c))

}
