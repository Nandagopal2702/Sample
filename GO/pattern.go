package main

import (
	"fmt"
)

func main() {
	row := make([]int, 5)
	col := make([]int, 5)

	for _, i := range row {
		_ = i
		for _, j := range col {
			fmt.Println(j, '\n')
		}
	}
}
