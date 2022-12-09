package main

import "fmt"

type Node struct {
	element int
	next    *Node
}

type Linked_list struct {
	head *Node
	tail *Node
	size int
}

func (LL *Linked_list) Len() int {
	return LL.size
}

func (LL *Linked_list) Display() {
	p := LL.head
	for p != nil {
		fmt.Printf("%v -->", p.element)
		fmt.Println(p.next)
		p = p.next
	}
}

func (LL *Linked_list) addLast(newest *Node) {
	if LL.size == 0 {
		LL.head = newest
	} else {
		LL.tail.next = newest
	}
	LL.tail = newest
	LL.size += 1
}

func (LL *Linked_list) addfirst(newest *Node) {
	if LL.size == 0 {
		LL.head = newest
		LL.tail = newest
	} else {
		newest.next = LL.head
		LL.head = newest
	}
	LL.size += 1
}

func (LL *Linked_list) addany(newest *Node, position int) {
	p := LL.head
	i := 0
	for i < position-1 {
		p = p.next
		i += 1
	}
	newest.next = p.next
	p.next = newest
	LL.size += 1
}

func (LL *Linked_list) search(n *Node, key int) (index int) {
	p := LL.head
	index = 0
	for p != nil {
		if p.element == key {
			return index
		}
		p = p.next
		index += 1
	}
	return -1
}

func (LL *Linked_list) deletefirst(*Node) (e int) {
	if LL.size == 0 {
		fmt.Println("List is empty")
		return
	}
	e = LL.head.element
	LL.head = LL.head.next
	LL.size -= 1
	if LL.size == 0 {
		LL.tail = nil
	}
	return
}

func (LL *Linked_list) deleteany(_ *Node, position int) (e int) {
	p := LL.head
	i := 0
	for i < position-1 {
		p = p.next
		i += 1
	}
	e = p.next.element
	p.next = p.next.next
	LL.size -= 1
	return e
}

func (LL *Linked_list) deletelast(*Node) (e int) {
	if LL.size == 0 {
		print("Linked list is empty")
		return
	}
	p := LL.head
	i := 1
	for i < LL.Len()-1 {
		p = p.next
		i += 1
	}
	LL.tail = p
	p = p.next
	e = p.element
	LL.tail.next = nil
	LL.size -= 1
	return e
}

func main() {
	L := Linked_list{}
	node1 := &Node{element: 10}
	node2 := &Node{element: 20}
	node3 := &Node{element: 30}
	node4 := &Node{element: 40}
	node5 := &Node{element: 50}
	node6 := &Node{element: 60}
	node7 := &Node{}

	// n := &Node{element: 40}
	// node7 := &Node{element: 100}
	// node8 := &Node{element: 200}

	L.addLast(node1)
	L.addLast(node2)
	L.addLast(node3)
	L.addfirst(node4)
	L.addfirst(node5)
	L.addfirst(node6)
	L.deletelast(node7)
	// L.addany(node7, 4)
	// L.addany(node8, 2)
	// node10 := &Node{}
	// node11 := &Node{}
	// DA := L.deleteany(node10, 3)
	// fmt.Println("Removed element : ", DA)
	// L.deletefirst(node11)
	// i := L.search(n, 90)
	// fmt.Println(i)
	fmt.Println(L.size)
	L.Display()

}
