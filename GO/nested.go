package main

import (
	"fmt"
)

func main() {
	time := 12
	if time == 12 {
		fmt.Println("You can work now")
		if time <= 12 {
			fmt.Println("Go and do work from home")
			if time >= 12 {
				fmt.Println("Work as well as eat lunch!")
			}
		}
	}
}
