class Node:
    __slots__ = 'element','next'

    def __init__(self,element,next):
        self.element = element
        self.next = next

class DEqueuelinked:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

        
    def __len__(self):
        return self.size      
    
    def isempty(self):
        return self.size == 0

    def Display(self):
        p = self.front
        while p:
            print(p.element,end="--->")
            print(p.next)
            p = p.next
        print()
    
    def addlast(self,e):
        newest = Node(e,None)
        if self.isempty():
            self.front = newest
        else:
            self.rear.next = newest
        self.rear = newest
        self.size += 1

    def addfirst(self,e):
        newest = Node(e,None)
        if self.isempty():
            self.front = newest
            self.rear = newest
        else:
            newest.next = self.front
            self.front = newest
        self.size += 1
    
    def removefirst(self):
        if self.isempty():
            print("List is empty")
            return
        e = self.front.element
        self.front = self.front.next
        self.size -= 1
        if self.isempty():
            self.rear = None
        return e

    def removelast(self):
        if self.isempty():
            print("List is empty")
            return
        p = self.front
        i = 1
        while i < len(self)-1:
            p = p.next
            i += 1
        self.rear = p
        p = p.next
        e = p.element
        self.rear.next = None
        self.size -= 1 
        return e

o1 = DEqueuelinked()
o1.addlast(10)
o1.addlast(20)
o1.addlast(30)
o1.addfirst(40)
o1.addfirst(50)
o1.removefirst()
o1.removelast()
# o1.front()
# o1.rear()
o1.Display()
