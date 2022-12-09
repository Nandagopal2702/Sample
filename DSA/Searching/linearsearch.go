package main

import "fmt"

func Linear_search(A []int, key int) int {
	index := 0
	for index < len(A) {
		if A[index] == key {
			return index
		}
		index += 1
	}
	return -1
}

func main() {
	A := []int{2, 6, 5, 4, 8, 9, 7, 1, 3}
	fmt.Println(Linear_search(A, 9))
}
