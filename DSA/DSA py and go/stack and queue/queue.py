class Queuesarray:

    def __init__(self):
        self.data = []
    
    def __len__(self):
        return len(self.data)
    
    def isempty(self):
        return len(self.data) == 0
    
    def enqueue(self,e):
        return self.data.append(e)

    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
            return
        return self.data.pop(0)
    
    def first(self):
        if self.isempty():
            print("Queue is empty")
            return
        return self.data[0]

Q = Queuesarray()
Q.enqueue(10)
Q.enqueue(20)
Q.enqueue(30)
Q.enqueue(40)
Q.enqueue(50)
print(Q.dequeue())
print(Q.data)
print(Q.first())