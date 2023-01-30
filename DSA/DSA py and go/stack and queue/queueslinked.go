package main

type Node struct {
	element int
	next    *Node
}

type Queueslinked struct {
	front *Node
	rear  *Node
	size  int
}

func (QL *Queueslinked) Len() int {
	return QL.size
}

func (QL *Queueslinked) enqueue(newest *Node) {
	if QL.size == 0 {
		QL.front = newest
		QL.rear = newest
	} else {
		newest.next = QL.front
		QL.front = newest
	}
	QL.size += 1
}
