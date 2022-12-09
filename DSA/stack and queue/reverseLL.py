class Node:
    __slots__ = "element","next"

    def __init__(self,element,next):
        self.element = element
        self.next = next

class ReverseLL:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __len__(self):
        return self.size
        
    def isempty(self):
        return self.size == 0
    
    def Display(self):
        p = self.head
        while p:
            print(p.element,end="--->")
            print(p.next)
            p = p.next
        print()

    def addlast(self,e):
        newest = Node(e,None)
        if self.isempty():
            self.head = newest
            self.tail = newest
        else:
            self.tail.next = newest
        self.tail = newest
        self.size += 1

    



o1 = ReverseLL()
o1.addlast(10)
o1.addlast(20)
o1.addlast(30)
o1.addlast(40)
o1.addlast(50)
o1.pop()
o1.Display()
