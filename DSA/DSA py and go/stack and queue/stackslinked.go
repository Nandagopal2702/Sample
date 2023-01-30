package main

import "fmt"

type Node struct {
	element int
	next    *Node
}

type Stackslinked struct {
	top  *Node
	size int
}

func (SL *Stackslinked) Len() int {
	return SL.size
}

func (SL *Stackslinked) push(newest *Node) {
	if SL.size == 0 {
		SL.top = newest
	} else {
		newest.next = SL.top
		SL.top = newest
	}
	SL.size += 1
}

func (SL *Stackslinked) Display() {
	p := SL.top
	i := 0
	for i < SL.Len() {
		fmt.Printf("%v -->", p.element)
		p = p.next
		i += 1
	}
}

func (SL *Stackslinked) pop() (e int) {
	if SL.size == 0 {
		fmt.Println("Stack is empty")
		return
	}
	e = SL.top.element
	SL.top = SL.top.next
	SL.size -= 1
	return e
}

func (SL *Stackslinked) Top() (e int) {
	if SL.size == 0 {
		fmt.Println("Stack is empty")
		return
	}
	e = SL.top.element
	return e
}

func main() {
	S := Stackslinked{}
	node1 := &Node{element: 10}
	node2 := &Node{element: 20}
	node3 := &Node{element: 30}
	node4 := &Node{element: 40}
	node5 := &Node{element: 50}

	S.push(node1)
	S.push(node2)
	S.push(node3)
	S.push(node4)
	S.push(node5)

	fmt.Println("Poped element : ", S.pop())
	fmt.Println("Top element : ", S.Top())
	S.Display()
}
