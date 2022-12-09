// Declaring a constant

// package main

// import (
// 	"fmt"
// )

// const PI float64 = 3.14

// func main() {
// 	fmt.Println("the value of pi is :", PI)
// }

// Typed constants

// package main

// import (
// 	"fmt"
// )

// const A int = 1              //  In this int datatype is declared

// func main() {
// 	fmt.Println(A)
// }

// Untyped constants

// package main

// import (
// 	"fmt"
// )

// const A = 1 //  In this datatype is not declared

// func main() {
// 	fmt.Println(A)
// }

// constants unchangeable and readonly

// package main

// import (
// 	"fmt"
// )

// func main() {
// 	const A = 1
// 	A := 2 // you will get error as (cannot assign to A)
// 	fmt.Println(A)
// }

//  multiple constant variables

package main

import (
	"fmt"
)

const (
	A int     = 10
	B float64 = 3.14
	C string  = "Nandu"
)

func main() {
	fmt.Println(A)
	fmt.Println(B)
	fmt.Println(C)
}
