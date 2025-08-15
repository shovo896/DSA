class   Deque : 
    def __init__(self) : 
        self.items = []
    def isEmpty (self) : 
        return self.items == []gtt
    def addRear (self,item) : 
        self.items.append(item) 
    def addFront(self,item) :
        self.items.insert(0,item)
    def removeRear(self):
        return self.items.pop()
    def removeFront(self):
        return self.items.pop(0)
    def size(self) : 
        return len(self.items) 
d= Deque()
print(d.isEmpty()) 
d.addRear(4)
d.addRear(5)
d.addRear(6)
d.addRear(7)
d.addRear(10)
print(d.size())
print(d.isEmpty())
d.addRear(11)
print(d.removeRear())
print(d.removeFront())
d.addFront(12)
d.addRear(13)
print(d.items)

