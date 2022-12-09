package main

import "fmt"

type Node struct {
	element int
	next    *Node
}

type Circular_LL struct {
	head *Node
	tail *Node
	size int
}

func (CL *Circular_LL) Len() int {
	return CL.size
}

func (CL *Circular_LL) Display() {
	p := CL.head
	i := 0
	for i < CL.Len() {
		fmt.Printf("%v --->", p.element)
		fmt.Println(p.next)
		p = p.next
		i += 1
	}
}

func (CL *Circular_LL) addLast(newest *Node) {
	if CL.size == 0 {
		newest.next = newest
		CL.head = newest
	} else {
		newest.next = CL.tail.next
		CL.tail.next = newest
	}
	CL.tail = newest
	CL.size += 1
}

func (CL *Circular_LL) addfirst(newest *Node) {
	if CL.size == 0 {
		newest.next = newest
		CL.head = newest
		CL.tail = newest
	} else {
		CL.tail.next = newest
		newest.next = CL.head
	}
	CL.head = newest
	CL.size += 1
}

func (CL *Circular_LL) addany(newest *Node, position int) {
	p := CL.head
	i := 0
	for i < position-1 {
		p = p.next
		i += 1
	}
	newest.next = p.next
	p.next = newest
	CL.size += 1
}

func (CL *Circular_LL) removefirst(*Node) (e int) {
	if CL.size == 0 {
		fmt.Println("Circular list is empty")
		return
	}
	e = CL.head.element
	CL.tail.next = CL.head.next
	CL.head = CL.head.next
	CL.size -= 1
	if CL.size == 0 {
		CL.head = nil
		CL.tail = nil
	}
	return e
}

func (CL *Circular_LL) removelast(*Node) (e int) {
	if CL.size == 0 {
		fmt.Println("Circular list is empty")
		return
	}
	p := CL.head
	i := 1
	for i < CL.Len()-1 {
		p = p.next
		i += 1
	}
	CL.tail = p
	p = p.next
	CL.tail.next = CL.head
	e = p.element
	CL.size -= 1
	return e
}

func (CL *Circular_LL) removeany(_ *Node, position int) (e int) {
	p := CL.head
	i := 1
	for i < position-1 {
		p = p.next
		i += 1
	}
	e = p.next.element
	p.next = p.next.next
	CL.size -= 1
	return e
}

func main() {
	C := Circular_LL{}
	node1 := &Node{element: 10}
	node2 := &Node{element: 20}
	node3 := &Node{element: 30}
	node4 := &Node{element: 40}
	node5 := &Node{element: 50}
	node6 := &Node{element: 60}
	node7 := &Node{}

	C.addLast(node1)
	C.addLast(node2)
	C.addLast(node3)
	C.addfirst(node4)
	C.addfirst(node5)
	C.addany(node6, 2)
	C.removeany(node7, 3)

	C.Display()
}
