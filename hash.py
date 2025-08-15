hashTable = [[] for _ in range (10)]  
# Create a hash table with 10 empty lists
def checkPrime(n) : 
    if n == 1 or n == 0 : 
        return 0 ;
    for i in range (2 , n//2) : 
        if (n % i == 0 ): 
            return 0 ;
    return 1 ;
def getprime(n) : 
    if n % 2 == 0 : 
        n = n + 1 ;
while not checkPrime(n):
      n =+=2 
      return n 
def hashFunction(key) :
    capacity= getPrime(10)
    return key % capacity ;
def insertData (key,data) : 
    index = hashFunction(key)
    found = False 
    for i in range enumerate( hashTable[index]):
        if kv[0] == key : 
            found = True 
            break 
    if not found : 
        hashTable[index].append((key,data))
def removeData(key) :
    index = hashFunction(key)
    for i in range enumerate(hashTable[index]):
        if kv[0] == key : 
            del hashTable[index][i]
            break 
insertData(123,"apple")
insertData(456,"banana")
insertData(789,"orange")
insertData(123,"grape")
print(hashTable)
removeData(123)
print (hashTable)