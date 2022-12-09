package main

import (
	"fmt"
)

func main() {
	var input int

Loop:
	fmt.Println("Hai dude you can't vote")
	fmt.Println("enter your age:")

	fmt.Scanln(&input)

	if input <= 18 {
		goto Loop
	} else {
		fmt.Println("You can vote")
	}
}
