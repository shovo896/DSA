#searching a key On a B tree in python 
class BTreeNode:
    def __init__(self,leaf=False):
        self.leaf=leaf
        self.keys=[]
        self.child=[]
class Btree:
    def __init__(self,t):
        self.root = BTreeNode(True)
        self.t=t
        #Insert a key 
        def insert (self,k):
            root=self.root 
            if len(root.keys) == (2*self.t)-1:
                temp=BTreeNode()
                self.root=temp
                temp.child.insert(0,root)
                self.split_child(temp,0)
                self.insert_non_full(temp,k)
            else:
                self.insert_non_full(root,k)

     #insert non full 
    def insert_non_full(self,x,k):
        i=len(x.keys)-1 
        if x.leaf :
            x.keys.append((None,None))
            while i >= 0 and k[0] < x.keys[i][0]:
                x.keys[i+1] =x.keys[i]
                i-=1
                x.keys[i+1]=k 
        else:
            while i >=0 and k[0] < x.keys[i][0] :
                i+=1
            self.insert_non_full(x.child[i],k)

            #split the child 
    def split_child(self,x,i):
        t=self.t
        y=x.child[i]
        z=BTreeNode(y.leaf)
        x.child.insert(i+1,z)
        x.keys.insert(i,y.keys[t-1])
        z.keys=y.keys[t:(2*t)-1]
        y.keys=y.keys[0:t-1]
        if not y.leaf :
            z.child=y.child[t:2*t]
            y.child=y.child[0:t]
    #delete a node 
    def delete(self,x,k):
        t=self.t
        i=0
        while i <len(x.keys)  and k[0] > x.keys[i][0]:
            i+=1
        if x.leaf:
            if i<len(x.keys) and x.keys[i][0]==k[0]:
                x.keys.pop(i)
                return 
        else:
            if < len(x.keys) and x.keys[i][0]==k[0]:
                return self.delete_internal_node(x,k,i)
    #case 3 : key is not found in internal node 
            if len(x.chilc[i].keys) < t : 
                self.fill(x,i)
            self.delete(x.child[i],k)
    def delete_internal_node(self,x,k,i)  :
        t=self.t
        #case 2a:predecessor has enough keys 
        if len(x.child[i].keys)  >= t :
            pred_key = self.get_predecessor(x,i)
            x.keys[i] =pred_key
            self.delete(x.child[i+1],pred_key)
        elif len(x.child[i+1].keys) >= t :
            succ_key=self.get_sucessor(x,i)
            x.keys[i]=succ_key
            self.delete(x.child[i+1],succ_key)
        else :
            self.merge(x,i)
            self.delete(x.child[i],k)
    def get_predecessor(self,x,i):
        cur=x.child[i+1]
        while not cur.leaf :
            cur=cur.child[0]
        return cur.keys[0]
    #Merge function to merge two children 
    def merge(self,x,i):
        t=self.t
        child= x.child[i]
        sibling =x.child[i+1]
        #Merge key from x to child 
        child.keys.append(x.keys[i])
        #Append siblings keys to child 
        child.keys.extend(sibling.keys)
        #If sibling has children ,append them to child
        if not child.leaf:
            child.child.extend(sibling.child)
        #Remove the key from x  and delete sibling from the child list
        x.keys.pop(i)
        x.child.pop(i+1)
        if len(x.keys)==0:
            self.root=child
        #Fill function to ensure child which has only one tree
        def fill(self,x,i):
            t=self.t
            #Borrow from  the privious sibling
            if i != 0 and len(x.child[i-1].keys)  >= t :
                self.borrow_from_prev(x,i)
            elif i != 0 and len(x.child[i+1].keys) >= t :
                self.borrow_from_next(x,i)
            #Merge with siblings 
            else :
                if i != len(x.child)-1:
                    self.merge(x,i)
                else :
                    self.marge(x,i-1)
        def borrow_from_prev(self,x,i):
            child=x.child[i]
            sibling=x.child[i-1]
            #Move the last key from the sibling 
            child.keys.insert(0,x.keys[i-1])
            x.keys[i-1]=sibling.keys.pop()
            #Move the last child of sibling to child if sibling is not leaf 
            if not child.leaf :
                child.child.insert(0,sibling.child.pop())
        def borrow_from_next(self,x,i):
            child-=x.child[i]
            sibling=x.child[i+1]
            #Move the first key from the siblings 
            child.keys.append(x.keys[i])
            x.keys[i] =sibling.keys.pop(0)      
            if not child.leaf:
                child.child.append(sibling.child.pop(0))  
        #print the tree 
        def print_tree(self,x,l=0):
            print("Level",l,"",len(x.keys),end=":")  
            for i in x.keys:
                print(i,end="") 
            print()  
            l+=1 
            if len(x.child) > 0:
                for i in x.child:
                    self.print_tree(i,l)
#Example usage 
B=BTree(3)
for i in range(10):
    B.insert(i,2*i)
B.print_tree(B.root,(8,))
B.delete(B.root,(8,))
print("\n")
B.print_tree(B.root)