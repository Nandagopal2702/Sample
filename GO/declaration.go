// Declaring variable outside the function, with the (var) keyword

// package main

// import (
// 	"fmt"
// )

// var a string
// var b int = 10
// var c = 20

// func main() {
// 	a = "Nandu"
// 	fmt.Println(a)   // Nandu
// 	fmt.Println(b)	 // 10
// 	fmt.Println(c)	 // 20

// }


// Declaring the variable outside the function, with ( := ) sign

package main
import (
	"fmt"
)

a := 20
b := 30

func main(){
	fmt.Println(a)		// this will give a error like (syntax error: non-declaration statement outside function body)
	fmt.Println(b)		// this will give a error like (syntax error: non-declaration statement outside function body)
}