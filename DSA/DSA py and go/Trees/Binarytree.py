from queueslinked import Queueslinked

# Creating Node class

class Node:
    __slots__ = "element","left","right"

    def __init__(self,element,left=None,right=None):
        self.element = element
        self.left = left
        self.right = right

class BinaryTree:

    def __init__(self):
        self.root = None
    
    def maketree(self,e,left,right):
        self.root = Node(e,left.root,right.root)

    def preorder(self,troot):
        if troot:
            print(troot.element,end=" ")
            self.preorder(troot.left)
            self.preorder(troot.right)

    def inorder(self,troot):
        if troot:
            self.inorder(troot.left)
            print(troot.element,end=" ")
            self.inorder(troot.right)
    
    def postorder(self,troot):
        if troot:
            self.postorder(troot.left)
            self.postorder(troot.right)
            print(troot.element,end=" ")
        
    def levelorder(self):
        Q = Queueslinked()
        t = self.root
        print(t.element,end=" ")
        Q.enqueue(t)
        while not Q.isempty():
            t = Q.dequeue()
            if t.left:
                print(t.left.element,end=" ")
                Q.enqueue(t.left)
            if t.right:
                print(t.right.element,end=" ")
                Q.enqueue(t.right)

    def count(self,troot):
        if troot:
            x = self.count(troot.left)
            y = self.count(troot.right)
            return x + y + 1
        return 0

    def height(self,troot):
        if troot:
            x = self.height(troot.left)
            y = self.height(troot.right)
            if x > y:
                return x + 1
            else:
                return y + 1
        return 0


x = BinaryTree()
y = BinaryTree()
z = BinaryTree()
r = BinaryTree()
s = BinaryTree()
t = BinaryTree()
a = BinaryTree()
x.maketree(40,a,a)
y.maketree(60,a,a)
z.maketree(20,x,a)
r.maketree(50,a,y)
s.maketree(30,r,a)
t.maketree(10,z,s)
print("Inorder Traversal")
t.inorder(t.root)
print()
print("Preorder Traversal")
t.preorder(t.root)
print()
print("Postorder Traversal")
t.postorder(t.root)
print()
print("Levelorder Traversal")
t.levelorder()
print()
print("Number of Nodes")
print(t.count(t.root))
print()
print("Height of the BinaryTree")
print(t.height(t.root)-1)