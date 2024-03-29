class Node:
    __slots__ = 'element','next'

    def __init__(self,element,next):
        self.element = element
        self.next = next

class Linked_list:
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
        else:
            self.tail.next = newest
        self.tail = newest
        self.size += 1

    def addfirst(self,e):
        newest = Node(e,None)
        if self.isempty():
            self.head = newest
            self.tail = newest
        else:
            newest.next = self.head
            self.head = newest
        self.size += 1

    def addany(self,e,position):
        newest = Node(e,None)
        p = self.head
        i = 0
        while i < position -1:
            p = p.next
            i += 1
        newest.next = p.next
        p.next = newest
        self.size += 1

    def search(self,key):
        p = self.head
        index = 0
        while p:
            if p.element == key:
                return index
            p = p.next
            index += 1
        return "Element is Not Present"
    
    def deletefirst(self):
        if self.isempty():
            print("List is empty")
            return
        e = self.head.element
        self.head = self.head.next
        self.size -= 1
        if self.isempty():
            self.tail = None
        return e

    def deletelast(self):
        if self.isempty():
            print("List is empty")
            return
        p = self.head
        i = 1
        while i < len(self)-1:
            p = p.next
            i += 1
        self.tail = p
        p = p.next
        e = p.element
        self.tail.next = None
        self.size -= 1 
        return e

    def deleteany(self,position):
        p = self.head
        i = 0
        while i < position-1:
            p = p.next
            i += 1
        e = p.next.element
        p.next = p.next.next
        self.size -= 1
        return e

    def insertsorted(self,e):
        newest = Node(e,None)
        if self.isempty():
            self.head = newest
        else:
            p = self.head
            q = self.head
            while p and p.element < e:
                q = p
                p = p.next
            if p == self.head:
                newest.next = self.head
                self.head = newest
            else:
                newest.next = q.next
                q.next = newest
        self.size += 1

