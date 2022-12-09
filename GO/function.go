//  Simple function

// package main

// import (
// 	"fmt"
// )

// func myMessage() {
// 	fmt.Println("I just got executed guys")
// }

// func main() {
// 	myMessage()
// }

//  Multiple function

// package main

// import (
// 	"fmt"
// )

// func Names() {
// 	fmt.Println("My Name is : Nandu")
// }

// func main() {
// 	Names()
// 	Names()
// 	Names()
// 	Names()
// 	Names()
// }

//  Parameters and Arguments

// package main

// import (
// 	"fmt"
// )

// func familyName(fname string) {
// 	fmt.Println("Hello", fname, "Nice to meet u")
// }

// func main() {
// 	familyName("Nandu")
// 	familyName("Gowda")
// 	familyName("Krish")
// 	familyName("guru")
// }

//  Multiple Parameters and arguments

package main

import (
	"fmt"
)

func Greetings(names string, age int) {
	fmt.Println("Hai", names, "Your age is: ", age, "Welcome")
}

func main() {
	Greetings("Nandu", 22)
	Greetings("vinayak", 24)
	Greetings("suhas", 24)
	Greetings("moin", 24)
	Greetings("vishal", 25)
}
