package main

import (
	"fmt"
)

func main() {
	adj := [3]string{"Big", "Small", "Tasty"}
	fruits := [4]string{"apple", "mango", "pineapple", "guva"}

	for i := 0; i < len(adj); i++ {
		for j := 0; j < len(fruits); j++ {
			fmt.Println(adj[i], fruits[j])
		}
	}
}
