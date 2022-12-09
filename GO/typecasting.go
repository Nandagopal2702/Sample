// package main

// import (
// 	"fmt"
// )

// func main() {
// 	var float_value float32 = 9.81       // varible assigned as float
// 	var int_value int = int(float_value) // vaiable converted to int

// 	fmt.Println(float_value)
// 	fmt.Println(int_value)
// }

// package main

// import (
// 	"fmt"
// )

// var float_value float32 = 9.81    // varible assigned as float

// func main() {
// 	var int_value int = int(float_value) // vaiable converted to int

// 	fmt.Println(float_value)
// 	fmt.Println(int_value)
// }

package main

import (
	"fmt"
)

func main() {
	A := 9.81
	B := int(A)

	fmt.Println(A)
	fmt.Println(B)
}
