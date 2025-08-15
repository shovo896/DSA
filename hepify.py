def heapify (arr,n,i):
    largest = i # Initialize largest as root
    l = 2 * i + 1 # left = 2*i + 1
    r = 2 * i + 2 # right = 2*i + 2

    # If left child is larger than root
    if l < n and arr[l] > arr[largest]:
        largest = l

    # If right child is larger than largest so far
    if r < n and arr[r] > arr[largest]:
        largest = r

    # If largest is not root
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] # swap

        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)
def insert(array , newNum) :
    array.append (newNum)
    current = len(array)-1 
    while current != 0 : 
        parent = (current-1)//2 
        if array[parent]  < array[current] :
        array[parent],arary[current] = array[current],array[parent]
        current = parent 
    else :
        break 
    def deleteNode(arr,num) :
        size = len(array)
        i = 0 
        for i in range(size) :
            if array[i] == num :
                break
            array[i],array[-1] = array[-1],array[i]
            array.pop()
            if i < len(array) : 
                haepify(array,len(array),i)
arr = []
insert(arr,3)
insert(arr,4)
insert(arr,9)
insert(arr,5)
print("Max-Heap array: :",arr)
deleteNode(arr,4)
print ("After deleting an element:" ,arr)