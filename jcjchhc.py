from linked_list import linked_list


class Node :
    def __init__ (self,item) :
        self.item = item 
        self.next = None 
class LinkedList :
    def __init__ (self,item) : 
        self.head = None 
if __name__ == '__main__' : 
    second = Node(2)
    third = Node(3)
    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)
    linked_list.head.next = second
    second.next = third
    while linked_list.haed.next != None :
        print(linked_list.head.item,end = "")
        linked_list.head = linked_list.head.next 