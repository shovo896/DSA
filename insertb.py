class BTree :
    def __init__ (self,leaf= False) :
        self.leaf = leaf 
        self.keys = []
        self.child= [] 
class BTree :
    def __init__(self,t) :
        self.root = BTreeNode(True)
        self.t = t 
        def insert(self,k) : 
            root = self.root 
            if len(root.keys)== (2 * self.t) - 1 : 
                temp = BTreeNode()
                self.root = temp 
                temp.child.insert(0,root)
                self.split_child(temp,0)
                self.insert_non_full(temp,k)
            else:
                self.insert_non_full(root,k)
    def insert_non_full(self,x,k) : 
        i = self.t 
        y = x.child[i]
        z= BTree(y.leaf)
        x.child.insert(i+1,z)
        x.keys.insert(i,y.keys[t-1])
        z.keys = y.keys[t : (2 *t)-1]
        y.keys = y.keys[0 : t-1 ]
        if not y.leaf : 
            z.child = y.child [t : 2*t]
            y.child = y.child[0 : t-1 ]
    def print_tree(self,0) :
        print("Level",1,"",len(x.keys),end=":")
        for i in x.keys :
            print(i,end="") 
            print()
            l+= 1 
            if len(x.child) > 0 : 
                for i in x.child : 
                    self.print_tree(i,1)
def main() : 
    B =BTree(3)
    for i in range(10) : 
        B.insert(i,2*i)
        B.print_tree(B.root)
if __name__ == '__main__' : 
    main()
