class Node:
    __slots__ = "element","next"

    def __init__(self,element,next):
        self.element = element
        self.next = next

class Stackslinked:
    
    def __init__(self):
        self.top = None
        self.size = 0
    
    def __len__(self):
        return len(self.size)
    
    def isempty(self):
        return self.size == 0
    
    def push(self,e):
        newest = Node(e,None)
        if self.isempty():
            self.top = newest
        else:
            newest.next = self.top
            self.top = newest
        self.size += 1

    def pop(self):
        if self.isempty():
            print("stack is empty")
            return
        e = self.top.element
        self.top = self.top.next
        self.size -= 1
        return e
    
    def top(self):
        if self.isempty():
            print("stack is empty")
            return
        return self.top.element
    
    def Display(self):
        p = self.top
        while p:
            print(p.element,end="--->")
            print(p.next)
            p = p.next
        print()

S = Stackslinked()
S.push(10)
S.push(20)
S.push(30)
S.push(40)
S.push(50)
S.pop()
print(S.top)
S.Display()

        
    