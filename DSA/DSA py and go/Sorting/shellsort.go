package main

import "fmt"

func Shell_sort(A []int) {
	n := len(A)
	gap := n / 2
	for gap > 0 {
		i := gap
		for i < n {
			temp := A[i]
			j := i - gap
			for j >= 0 && A[j] > temp {
				A[j+gap] = A[j]
				j = j - gap
			}
			A[j+gap] = temp
			i += 1
		}
		gap = gap / 2
	}
}

func main() {
	A := []int{3, 6, 8, 9, 5, 2}
	fmt.Println(A)
	Shell_sort(A)
	fmt.Println(A)
}
