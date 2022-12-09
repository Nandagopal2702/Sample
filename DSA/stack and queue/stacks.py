class StacksArray:

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def isempty(self):
        return self.data == 0

    def push(self,e):
        return self.data.append(e)
    
    def pop(self):
        if self.isempty():
            print("Stack is empty")
            return
        return self.data.pop()
        
    def top(self):
        if self.isempty():
            print("Stack is empty")
            return
        return self.data[-1]

S = StacksArray()
S.push(10)
S.push(20)
S.push(30)
S.push(40)
S.push(50)
print(S.data)
# S.pop()
print(S.top())
S.pop()
print(S.top())