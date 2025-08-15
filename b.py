class BTreeNode : 
    def __init__(self,leaf=False): 
        self.leaf = leaf 
        self.keys = []
        self.child = []
class Btree : 
    def __init__(self,t) :
        self.root = BTreeNode(True)
        self.t = t 
    def insert (self,t):
        root = self.root 
        if len(root.keys) == (2*self.t) -1 : 
            temp = BtreeNode()
            self.root = temp
            temp.child.insert(0,root)
            temp.split_child(temp,0)
            temp.insert_non_full(temp,k)
        else : 
            self.insert_non_full(root,k)
    def insert_non_full(self,x,k) :
        i=len(x.keys) - 1 
        if x.leaf :
            x.keys.append((None,None))
            while i>= 0 and k[0] < x.keys[i][0] :
                x.keys[i+1]=x.keys[i]
                i -= 1
                x.keys[i+1] = k 
        else :
            while i >=0 and k[0] < x.keys[i][0]:
                i -= 1 
                i+= 1 
                if len(x.child[i].keys) == 2*self.t-1 : 
                    self.split.child(x,i)
                    if k[0]  > x.keys[i][0] : 
                        i += 1 
                    self.insert_non_full(x.child[i],k)
    def  delete_internal_node(self,x,k,i):
        t = self.t 
        if  len(x,child[i].keys) >= t :
            pred_key = self.get_predecessor(x,i)
            x.keys[i] = pred_key 
            self.delete(x.child[i],pred_key)
        elif len(x.child[i+1].keys) >= t :
            succ_key = self.key.sucessor(x,i)
            x.keys[i] = succ_key 
            self.delete(x.child[i+1],succ_key) 
        else :
            self.merge(x,i) 
            self.delete(x.child[i],k)
    def get_predecessor(self,x,i):
        cur = x.child[i]
        while not cur.leaf :
            cur = cur.child[len(cur.child)-1]
            return cur.keys[len(cur.keys)-1]
    def get_sucessor(self,x,i) :
        cur = x.child[i+1]
        while not cur.leaf :
            cur=cur.child[0]
            return cur.keys[0]
    def merge (self,x,i) :
        t = self.t
        child = x.child[i]
        sibling = x.child[i+1]     
        child.keys.append(x.keys[i]) 
        child.keys.extend(sibling.child) 
        if not child.leaf :
            child.child.extend(sibling.child)
        x.keys.pop(i)
        x.child.pop(i+1)
        if len(x.keys) == 0 :
            self.root = child 
    def fill (self,x,i) :
        t=self.t 
        if i !=0 and len(x.child[i-1].keys) >= t :
            self.borrow_from_prev(x,i)
        elif i != len(x.child) -1 and len(x.child(i+1).keys) >= t : 
             self.borrow_from_next(x,i)
        else : 
             if i !=len(x.child): 
                self.merge(x,i) 
             else : 
                 self.merge(x,1-i)

    def borrow_from_prev(self,x,i): 
        child=x.child[i]
        sibling = x.child[i-1]
        child.keys.insert(0,siblingkeys.pop())
        if not child.leaf : 
            child.child.insert(0,sibling.child.poo())
    def borrow_from_next(self,x,i) : 
        child = x.child[i]
        sibling = x.child[i+1]
        child.keys.append(x.keys[i])
        x.keys[i] = sibling.keys.pop(0)
        if not child.leaf : 
            child.child.append(sibling.child.pop(0))
    def print_tree(self,x,l=0): 
        print("Level",l,"",len(x.keys),end="")
        for i in x.keys : 
            print(i,end="")
            print()
            l+=1
            if len(x.child) > 0 : 
                for i in child : 
                    self.print_tree(i,1)
B = Btree(3) 
for i in range(10):
    B.insert(i, 2 * i)  # Insert key-value pair
    if B.root:          # Check if the root exists before attempting deletion
        B.delete(B.root)
    print("\n")  
    if B.root:          # Print tree only if the root is valid
        B.print_tree(B.root)
    else:
        print("Tree is empty.")
