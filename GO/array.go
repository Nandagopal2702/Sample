// package main

// import "fmt"

// func main() {
// 	var arr1 = [5]int{10, 20, 30, 40, 50}   // using var keyword
// 	arr2 := [6]float32{1.2, 2.1, 3.3, 4.4}  // using sign :=
// 	fmt.Println(arr1)
// 	fmt.Println(arr2)
// }

//  Access the elements from array

// package main

// import "fmt"

// func main() {
// 	arr1 := [...]int{1, 2, 3, 4, 5, 6, 7, 8, 9} // using [...] you enter the elements how much ever you want

// 	fmt.Println(arr1[0], arr1[3]) // access the elements of the array by indexes of the array

// }

// change the elements of the array

// package main

// import (
// 	"fmt"
// )

// func main() {
// 	arr1 := [...]int{1, 2, 3, 4, 5, 6, 7, 8, 9}
// 	arr1[3] = 50
// 	arr1[5] = 60
// 	fmt.Println(arr1)
// }

// Array Initialization

// package main

// import (
// 	"fmt"
// )

// func main() {
// 	arr1 := [5]int{}              // not initialized
// 	arr2 := [6]int{1, 2, 3}       // partially initialized
// 	arr3 := [5]int{1, 2, 3, 4, 5} // fully initialized

// 	fmt.Println(arr1)
// 	fmt.Println(arr2)
// 	fmt.Println(arr3)
// }

// Initialize only specific elements

// package main

// import (
// 	"fmt"
// )

// func main() {
// 	arr1 := [8]int{1: 20, 3: 60}
// 	fmt.Println(arr1)
// }

// Find the length of the array

// package main

// import (
// 	"fmt"
// )

// func main() {
// 	arr1 := [...]int{1, 2, 6, 5, 4, 8, 9, 5, 6, 8, 56, 62}

// 	fmt.Println(len(arr1))
// }

// 2D array

// package main

// import "fmt"

// func main() {
// 	arr := [3][3]int{
// 		{2, 6, 5},
// 		[3]int{3, 6, 5},
// 		[3]int{9, 8, 7},
// 	}
// 	fmt.Println(arr)
// }

// Keyed elements

// package main

// import "fmt"

// func main() {
// 	arr := [4]int{
// 		0: 3,
// 		2: 4,
// 		3: 5,
// 		1: 6,
// 	}
// 	fmt.Println(arr)
// }

// package main

// import "fmt"

// func main() {
// 	arr := [7]int{2: 50, 5: 60}
// 	fmt.Println(arr)
// }

// package main

// import "fmt"

// func main() {
// 	arr := [8]string{
// 		0: "Nandu",
// 		6: "Gopal",
// 		"devaraj",  // this will go to last index if the index is not mentioned
// 		4: "!!!",
// 	}
// 	fmt.Printf("%#v\n", arr)
// }

// package main

// import "fmt"

// func main() {
// 	arr := [7]bool{2: true, 5: false}
// 	fmt.Println(arr)
// }

package main

import "fmt"

func main() {
	arr := [4]int{}
	fmt.Printf("%T\n", arr)
}
