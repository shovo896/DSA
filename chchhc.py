class MyCircularQueue: 
    def __init__(self,k): 
        self.k = k 
        self.queue = [None] * k 
        self.head = self.tail = -1
        def enqueue(self,data):
            if (self.tail == self.k - 1) : 
                print(" The queue is full\n") 
            elif (self.head == -1) : 
                self.head = 0 
                self.tail = 0 
                self.queue[self.tail] = data 
            else : 
                self.tail = (self.tail + 1) % self.k 
                self.queue[self.tail] = data
                def dequeue(self) :
                    if (self.head == -1) : 
                        print (" The queue is empty\n") 
                    elif (self.head == self.tail) : 
                        temp = self.queue[self.head] 
                        self.head = self.tail = -1 
                        return temp 
                    else : 
                        temp = self.queue[self.head] 
                        self.head = (self.head + 1) % self.k 
                        return temp 
                    def printQueue(self) : 
                        if (self.head == -1) : 
                            print (" No element in the queue") 
                        else : 
                            for i in range (self.head,self.tail+1) : 
                                print(self.queue[i],end="") 
                            print()
obj = MyCircularQueue(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
print("Initial queue")
obj.printCueue()
obj.dequeue()
print("After removiung an element from the queue")
obj.printQueue()
