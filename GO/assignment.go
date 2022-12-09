package main

import (
	"fmt"
)

func main() {
	x := 5; y := 10; z := 2; a := 50; b := 5; c := 10; d := 30; e := 40; f := 10; g := 20

	x += 5
	y -= 5
	z *= 10
	a /= 5
	b %= 2
	c &= 4
	d |= 6
	e ^= 5
	f <<= 3
	g >>= 3

	fmt.Println(x)
	fmt.Println(y)
	fmt.Println(z)
	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)
	fmt.Println(d)
	fmt.Println(e)
	fmt.Println(f)
	fmt.Println(g)
}
