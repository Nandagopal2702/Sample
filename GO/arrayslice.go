// package main

// import (
// 	"fmt"
// )

// func main() {
// 	arr1 := []int{1, 2, 3, 4, 5, 6, 7, 8}

// 	myslice := arr1[2:6]

// 	fmt.Println(myslice)
// 	fmt.Println(len(myslice))
// 	fmt.Println(cap(myslice))

// }

// Access element from the slice

// package main

// import (
// 	"fmt"
// )

// func main() {
// 	myslice := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}

// 	fmt.Println(myslice[5])
// 	fmt.Println(myslice[2])
// 	fmt.Println(myslice[8])
// }

// comparing slice

// package main

// import "fmt"

// func main() {
// 	var n []int
// 	fmt.Println(n == nil) // true

// 	m := []int{}
// 	fmt.Println(m == nil) // false
// }

// appending slice

package main

import "fmt"

func main() {
	src := []int{10, 20, 30}
	dst := make([]int, len(src))
	nn := copy(dst, src)
	fmt.Println(src, dst, nn)
}
