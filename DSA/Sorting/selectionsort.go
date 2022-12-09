package main

import "fmt"

func Selection_sort(A []int) {
	n := len(A)
	for i := 0; i < n-1; i++ {
		position := i
		for j := i + 1; j < n; j++ {
			if A[j] < A[position] {
				position = j
			}
		}
		A[i], A[position] = A[position], A[i]
	}
}

func main() {
	A := []int{3, 5, 8, 9, 6, 2}
	fmt.Println("Originl array : ", A)
	Selection_sort(A)
	fmt.Println("Sorted array", A)

}
