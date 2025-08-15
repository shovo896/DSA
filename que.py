class Queue () : 
    def __init__ (self, k) : 
        self.k = k 
        self.queue = [None] * k 
        self.head = self.tail = -1 
    def enqueue (self,data ) :
        if (self.tail == self.k - 1) :
            print(" The queue is full\n ") 
        elif (self.head == -1) :
            self.head = 0 
            self.tail = 0 
            self.queue(self.tail) =data 
            def dequeue(self) : 
                if (self.head == -1) : 
                    print (" The queue is empty\n") 
                    def dequeue (self) : 
                        if (self.head ==-1): 
                            print ("The queue is empty \n ") 
                        elif (self.head == self.tail) : 
                            temp= self.queqe[self.head]
                            self.head = self.head+1 
                            return temp 
     def printQueue (self) : 
        if (self.head == -1 ) : 
            print (" No element in the queque")
        else : 
            for i in range (self.head,self.tail+1) :
                print(self.queue[i],end="")
            print()
obj = queque(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
print(" Initial queue")
obj.printQueue()
obj.dequeue()
print("After removing an element from the queue ")
obj.printQueue()
                             
