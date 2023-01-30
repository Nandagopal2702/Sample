package main

import "fmt"

func Insertion_sort(A []int) {
	n := len(A)
	for i := 1; i < n; i++ {
		cvalue := A[i]
		position := i
		for position > 0 && A[position-1] > cvalue {
			A[position] = A[position-1]
			position -= 1
		}
		A[position] = cvalue
	}
}

func main() {
	A := []int{3, 5, 8, 9, 6, 2}
	fmt.Println("Original array : ", A)
	Insertion_sort(A)
	fmt.Println("Sorted array : ", A)
}
