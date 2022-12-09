// package main

// import (
// 	"fmt"
// )

// func main() {
// 	for i := 0; i <= 5; i++ {
// 		if i == 3 { // here the value 3 has been skipped from the printing
// 			continue
// 		}
// 		fmt.Println(i)
// 	}
// }

package main

import (
	"fmt"
)

func main() {
	for i := 0; i <= 5; i++ {
		if i < 3 { // here the value less than 3 has been skipped from the printing
			continue
		} else if i == 5 { // here the value 5 has been skipped from the printing
			continue
		}
		fmt.Println(i)
	}
}
