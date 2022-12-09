// package main

// import (
// 	"fmt"
// )

// func main() {
// 	var input string

// 	fmt.Println("Type your Name : ")
// 	fmt.Scanln(&input) // taking input from user
// 	fmt.Println("You entered the Name : ", input)
// }

package main

import (
	"fmt"
)

func main() {
	var a int
	var b int

	fmt.Scanln(&a, &b)
	fmt.Println(a, b)

}
