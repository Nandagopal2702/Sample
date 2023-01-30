class Node:
    __slots__ = "element","next"

    def __init__(self,element,next):
        self.element = element
        self.next = next

class CircularLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def isempty(self):
        return self.size == 0
    
    def addlast(self,e):
        newest = Node(e,None)
        if self.isempty():
            newest.next = newest
            self.head = newest
        else:
            newest.next = self.tail.next
            self.tail.next = newest
        self.tail = newest
        self.size += 1
    
    def Display(self):
        p = self.head
        i = 0
        while i < len(self):
            print(p.element,end="--->")
            print(p.next)
            p = p.next
            i += 1

    def addfirst(self,e):
        newest = Node(e,None)
        if self.isempty():
            newest.next = newest
            self.head = newest
            self.tail = newest
        else:
            self.tail.next = newest
            newest.next = self.head
        self.head = newest
        self.size += 1

    def addany(self,e,position):
        newest = Node(e,None)
        p = self.head
        i = 0
        while i < position-1:
            p = p.next
            i += 1
        newest.next = p.next
        p.next = newest
        self.size += 1

    def removefirst(self):
        if self.isempty():
            print("Circular list is empty")
            return
        e = self.head.element
        self.tail.next = self.head.next
        self.head = self.head.next
        self.size -= 1
        if self.isempty():
            self.head = None
            self.tail = None
        return e

    def removelast(self):
        if self.isempty():
            print("Circular list is empty")
            return
        p = self.head
        i = 1
        while i < len(self)-1:
            p = p.next
            i += 1
        self.tail = p
        self.tail.next = self.head
        e = p.element
        self.size -= 1
        return e

    def removeany(self,position):
        p = self.head
        i = 1
        while i < position-1:
            p = p.next
            i += 1
        e = p.next.element
        p.next = p.next.next
        self.size -= 1
        return e

o1 = CircularLinkedList()
o1.addlast(10)
o1.addlast(20)
o1.addlast(30)
o1.addlast(40)
o1.addlast(100)
o1.addlast(200)
o1.removeany(3)
o1.Display()