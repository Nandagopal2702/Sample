// value declaration with initial value

// package main

// import (
// 	"fmt"
// )

// func main() {
// 	var student1 = "Nandu"
// 	var student2 = "John"
// 	x := 20

// 	fmt.Println(student1)
// 	fmt.Println(student2)
// 	fmt.Println(x)
// }

// value declaration without initial value

// package main

// import (
// 	"fmt"
// )

// func main() {
// 	var a string
// 	var b int
// 	var c bool
// 	fmt.Println(a)
// 	fmt.Println(b)
// 	fmt.Println(c)
// }

// value Assignment after declaration

// package main

// func main() {
// 	var student string
// 	student = "Nandu"           // if the variable is given and the variable is not used then the code will give you this error
// 								// error = student declared but not used
// }

package main

func main() {
	var student string
	var gravity float32 = 9.81
	student = "Nandu"
	// fmt.Println(student)
	// fmt.Println(gravity)
	_ = student // using this ( _ = variable name) will stop giving errors
	_ = gravity
}
