class Node:
    __slots__ = "element","next"

    def __init__(self,element,next):
        self.element = element
        self.next = next

class Queueslinked:

    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    def __len__(self):
        return len(self.size)
    
    def isempty(self):
        return  self.size == 0
    
    def enqueue(self,e):
        newest = Node(e,None)
        if self.isempty():
            self.front = newest
        else:
            self.rear.next = newest
        self.rear = newest
        self.size += 1

    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
            return
        e = self.front.element
        self.front = self.front.next
        self.size -= 1
        if self.isempty():
            self.rear = None
        return e

    def first(self):
        if self.isempty():
            print("Queue is empty")
            return
        return self.front.element

    def Display(self):
        p = self.front
        while p:
            print(p.element,end="->")
            p = p.next
        print()

QL = Queueslinked()
QL.enqueue(10)
QL.enqueue(20)
QL.enqueue(30)
QL.enqueue(40)
QL.enqueue(50)

print(QL.dequeue())
print(QL.first())
QL.Display()
