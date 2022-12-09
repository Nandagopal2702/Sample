package main

import "fmt"

type StackArray struct {
	data []int
	size int
}

func (SA *StackArray) Len() int {
	return len(SA.data)
}

func (SA *StackArray) push(e int) {
	SA.data = append(SA.data, e)
}

func (SA *StackArray) pop() (b int) {
	if len(SA.data) == 0 {
		fmt.Println("Stack is empty")
		return
	} else {
		b := SA.data[len(SA.data)-1]
		SA.data = SA.data[0 : len(SA.data)-1]
		return b

	}
}

// func (SA *StackArray) top()(slice int){
// 	if SA.Len() == 0 {
// 		fmt.Println("Stack is empty")
// 		return
// 	}
// 	a := SA.data

// }

func main() {
	S := StackArray{}
	S.push(10)
	S.push(20)
	S.push(30)
	S.push(40)
	S.push(50)
	fmt.Println(S.pop())
	fmt.Println(S.data)
	S.push(100)
	S.push(200)
	fmt.Println(S.pop())
	fmt.Println(S.data)

}
