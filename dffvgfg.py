def heapify(arr,n,i):
    largest= i 
    l= 2*i+1 
    r = 2*i+2 
    if l < n and arr[i] < arr[l] :
        largest = l 
    if r < n and arr[largest] < arr[r] :
        largest = r
        if largest != i : 
            arr[i],arr[largest]= arr [largest],arr[i]
            heapify(arr,n, largest)
def insert(array,NewNum) :
    size = len(array)
    if array == 0 : 
        array.append(NewNum)
    else: 
        array.append(newNum): 
        for i in range ((size//2),-1,-1,-1) : 
            heapify(array,size,i)
    def deleteNode(array,num) :
        size = len(array)
        i = 0 
        for i in range(0,size) : 
            if num == array[i] : 
                break 
    array[i],array[size-1] = array[size-1],array[i]
    array.pop()
    for  i in range (size//2,-1,-1,-1) : 
        heapify(array,len(array),i) 
        arr = []
        insert (arr,3)
        insert (arr,4)
        insert(arr,9)
        insert(arr,5)
        insert(arr,2)
        print(" Max-Heap array:",str(arr))
        deleteNode(arr,4)
        print(" After deleting an element:" ,+str(arr))
