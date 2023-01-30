package main

import "fmt"

func Merge_sort(A []int, left int, right int) {
	if left < right {
		mid := (left + right) / 2
		Merge_sort(A, left, mid)
		Merge_sort(A, mid+1, right)
		Merge(A, left, mid, right)
	}
}
func Merge(A []int, left int, mid int, right int) {
	i := left
	j := mid + 1
	k := left
	B := []int{}
	for i <= mid && j <= right {
		if A[i] < A[j] {
			B[k] = A[i]
			i += 1
			k += 1
		} else {
			B[k] = A[j]
			j += 1
			k += 1
		}
	}
	for i <= mid {
		B[k] = A[i]
		i += 1
		k += 1
	}
	for j <= right {
		B[k] = A[j]
		j += 1
		k += 1
	}

	for x := left; x <= right; x++ {
		A[x] = B[x]
	}
}

func main() {
	A := []int{3, 5, 8, 9, 6, 2}
	fmt.Println(A)
	Merge_sort(A, 0, len(A)-1)
	fmt.Println(A)
}
