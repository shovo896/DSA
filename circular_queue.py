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
              if self.front == -1 :
                     self.front=0 
                     self.rear =(self.rear+1) % self.size 
                     self.queue[self.rear]=value 

       def dequeue(self):
              if self.front == -1 :
                     print("Queue is Empty")
                     return 
              removed =self.queue[self.front]

              if self.front == self.rear :
                     self.front = self.rear = -1
              else:
                     self.front=(self.front+1) % self.size 
                     return removed 


def display(self):
       if self.front == -1:
              print("Empty")
              return 
       i = self.front 
       while True :
              print(self.queue[i],end="")
              if i == self.rear:
                     break 
              i = (i+1) % self.size 
              print()

