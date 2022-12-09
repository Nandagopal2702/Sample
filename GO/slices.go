// Basic way of creting slice

// package main

// import (
// 	"fmt"
// )

// func main() {
// 	my_slice := []int{1, 2, 3, 4, 5, 6}  // a slice of length-6 and capacity-6

// 	fmt.Println(my_slice)
// }

package main

import (
	"fmt"
)

func main() {
	my_slice := []int{}

	fmt.Println(len(my_slice))
	fmt.Println(cap(my_slice))
	fmt.Println(my_slice)

	my_slice2 := []string{"Go", "is", "created", "by", "Google"}

	fmt.Println(len(my_slice2))
	fmt.Println(cap(my_slice2))
	fmt.Println(my_slice2)
}
