package main

import "fmt"

func main() {
	var val1 int
	var ptr *int // pointer variable
	fmt.Scanln(&val1)
	ptr = &val1 // 12
	*ptr++
	fmt.Println(val1)
	fmt.Println(ptr)  // pointer
	fmt.Println(*ptr) // dereffering operator
	// (*) => Dereffering or indirection operator
}
