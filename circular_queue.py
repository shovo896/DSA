class CircularQueue:
       def __init__(self,size):
              self.size = size
              self.queue=[None]*size 
              self.front=-1 
              self.rear=-1 
       def enqueue(self,value):
              if(self.rear +1) % self.size == self.front:
                     print("Queue is full")
                     return  
