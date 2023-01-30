class DEquearray:
    def __init__(self):
        self.data = []
    
    def __len__(self):
        return len(self.data)
    
    def isempty(self):
        return len(self.data) == 0
    
    def addfirst(self,e):
        self.data.insert(0,e)
    
    def addlast(self,e):
        self.data.append(e)

    def removefirst(self):
        if self.isempty():
            print("Queue is empty")
            return
        return self.data.pop(0)
    
    def removelast(self):
        if self.isempty():
            print("Queue is empty")
            return
        return self.data.pop()
    
    def first(self):
        if self.isempty():
            print("Queue is empty")
            return
        return self.data[0]
    
    def rear(self):
        if self.isempty():
            print("Queue is empty")
            return 
        return self.data[-1]

DE = DEquearray()
DE.addfirst(10)
DE.addfirst(20)
DE.addfirst(30)
DE.addlast(40)
DE.addlast(50)
DE.addlast(60)
print(DE.data)