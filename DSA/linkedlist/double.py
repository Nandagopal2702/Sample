class Node:
    __slots__ = 'element','next','prev'

    def __init__(self,element,next,prev):
        self.element = element
        self.next = next
        self.prev = prev

class DoubleLinked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
   
    def __len__(self):
        return self.size  

    def isempty(self):
        return self.size == 0

    def addlast(self,e):
        newest = Node(e,None,None)
        if self.isempty():
            self.head = newest
            self.tail = newest
        else:
            self.tail.next = newest
            newest.prev = self.tail
            self.tail = newest
        self.size += 1
    
    def addfirst(self,e):
        newest = Node(e,None,None)
        if self.isempty():
            self.head = newest
            self.tail = newest
        else:
            newest.next = self.head
            self.head.prev = newest
            self.head = newest
        self.size += 1
    
    def addany(self,e,position):
        newest = Node(e,None,None)
        p = self.head
        i = 1
        while i < position-1:
            p = p.next
            i += 1
        newest.next = p.next
        p.next.prev = newest
        p.next = newest
        newest.prev = p
        self.size += 1

    def removefirst(self):
        if self.isempty():
            print("Double list is empty")
            return
        e = self.head.element
        self.head = self.head.next
        self.head.prev = None
        if self.isempty():
            self.tail = None
        self.size -= 1
        return e

    def removelast(self):
        if self.isempty():
            print("Double list is empty")
            return
        e = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
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
        p.next.prev = p
        self.size -= 1
        return e
    
    def Display(self):
        p = self.head
        while p:
            print(p.prev,end="-->  ")
            print(p.element,end="--->  ")
            print(p.next,end="--> ")
            p = p.next
            print()
        print()

o1 = DoubleLinked_list()
o1.addlast(10)
o1.addlast(20)
o1.addlast(30)
o1.addlast(40)
o1.addlast(50)
# o1.removefirst()
# o1.removelast()
o1.removeany(3)
o1.Display()