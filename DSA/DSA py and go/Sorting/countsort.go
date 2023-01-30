package main

import (
	"fmt"
)

func countsort(A []int) {
	n := len(A)

	// finding maxsize in the elements of array
	maxnum := A[0]
	for i := 0; i < len(A); i++ {
		if A[i] > maxnum {
			maxnum = A[i]
		}
	}
	maxsize := maxnum
	Carray := make([]int, maxsize+1)
	for i := 0; i < n; i++ {
		Carray[A[i]] += 1
	}
	i := 0
	j := 0
	for i < maxsize+1 {
		if Carray[i] > 0 {
			A[j] = i
			j += 1
			Carray[i] -= 1
		} else {
			i += 1
		}
	}

}

func main() {
	A := []int{3, 5, 8, 9, 6, 2}
	fmt.Println("Original array", A)
	countsort(A)
	fmt.Println("Sorted array", A)
}
