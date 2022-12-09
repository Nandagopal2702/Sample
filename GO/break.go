// package main

// import (
// 	"fmt"
// )

// func main() {
// 	for i := 0; i <= 5; i++ {
// 		if i == 3 {
// 			break
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
		if i == 3 {
			continue
		} else if i == 5 {
			break
		}
		fmt.Println(i)
	}
}
