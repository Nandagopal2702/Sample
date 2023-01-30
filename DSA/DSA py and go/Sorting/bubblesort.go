package main

import "fmt"

func Bubble_sort(A []int) {
	n := len(A)
	for i := n - 1; i >= 0; i-- {
		for j := 0; j < i; j++ {
			if A[j] > A[j+1] {
				A[j], A[j+1] = A[j+1], A[j]
			}
		}
	}
}

func main() {
	A := []int{3, 5, 8, 9, 6, 2}
	fmt.Println("Original array : ", A)
	Bubble_sort(A)
	fmt.Println("Sorted array : ", A)
}
