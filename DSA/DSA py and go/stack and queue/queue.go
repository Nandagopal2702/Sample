package main

import "fmt"

type Queuearray struct {
	data []int
	size int
}

func (QA *Queuearray) Len() int {
	return len(QA.data)
}

func (QA *Queuearray) enqueue(e int) {
	QA.data = append(QA.data, e)
}

func (QA *Queuearray) dequeue() (b int) {
	if QA.Len() == 0 {
		fmt.Println("Queue is empty")
		return
	} else {
		b := QA.data[0]
		QA.data = QA.data[1:QA.Len()]
		return b
	}
}

func (QA *Queuearray) first() (b int) {
	if QA.Len() == 0 {
		fmt.Println("Queue is empty")
		return
	} else {
		b := QA.data[0]
		return b
	}
}

func main() {
	Q := Queuearray{}
	Q.enqueue(10)
	Q.enqueue(20)
	Q.enqueue(30)
	Q.enqueue(40)
	Q.enqueue(50)
	fmt.Println(Q.data)
	fmt.Println(Q.dequeue())
	fmt.Println(Q.data)
	fmt.Println(Q.first())
}
