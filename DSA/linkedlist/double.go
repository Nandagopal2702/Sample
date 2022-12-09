package main

import (
	"fmt"
)

type Node struct {
	element int
	next    *Node
	prev    *Node
}

type Double_LL struct {
	head *Node
	tail *Node
	size int
}

func (DL *Double_LL) Len() int {
	return DL.size
}

func (DL *Double_LL) Display() {
	p := DL.head
	i := 0
	for i < DL.Len() {
		fmt.Printf("%v -->", p.prev)
		fmt.Printf("%v -->", p.element)
		fmt.Printf("%v -->", p.next)
		fmt.Println()
		p = p.next
		i += 1
	}

}

func (DL *Double_LL) addlast(newest *Node) {
	if DL.size == 0 {
		DL.head = newest
		DL.tail = newest
	} else {
		DL.tail.next = newest
		newest.prev = DL.tail
		DL.tail = newest
	}
	DL.size += 1
}

func (DL *Double_LL) addfirst(newest *Node) {
	if DL.size == 0 {
		DL.head = newest
		DL.tail = newest
	} else {
		newest.next = DL.head
		DL.head.prev = DL.head
		DL.head = newest
	}
	DL.size += 1
}

func (DL *Double_LL) addany(newest *Node, position int) {
	p := DL.head
	i := 1
	for i < position-1 {
		p = p.next
		i += 1
	}
	newest.next = p.next
	p.next.prev = newest
	p.next = newest
	newest.prev = p
	DL.size += 1
}

func (DL *Double_LL) removefirst(*Node) (e int) {
	if DL.size == 0 {
		fmt.Println("Double list is empty")
		return
	}
	e = DL.head.element
	DL.head = DL.head.next
	DL.head.prev = nil
	if DL.size == 0 {
		DL.tail = nil
	}
	DL.size -= 1
	return e
}

func (DL *Double_LL) removelast(*Node) (e int) {
	if DL.size == 0 {
		fmt.Println("Double list is empty")
		return
	}
	e = DL.tail.element
	DL.tail = DL.tail.prev
	DL.tail.next = nil
	DL.size -= 1
	return e
}

func (DL *Double_LL) removeany(_ *Node, position int) (e int) {
	p := DL.head
	i := 1
	for i < position-1 {
		p = p.next
		i += 1
	}
	e = p.next.element
	p.next = p.next.next
	p.next.prev = p
	DL.size -= 1
	return e
}

func main() {
	D := Double_LL{}

	node1 := &Node{element: 10}
	node2 := &Node{element: 20}
	node3 := &Node{element: 30}
	node4 := &Node{element: 40}
	node5 := &Node{element: 50}
	node6 := &Node{}

	D.addlast(node1)
	D.addlast(node2)
	D.addlast(node3)
	D.addfirst(node4)
	D.addfirst(node5)
	D.removeany(node6, 3)

	D.Display()
}
