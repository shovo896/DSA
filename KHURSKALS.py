class graph:
     def __ init __(self,vertices):
         self.V=vertices
         self.graph=[]
     def __add_edge(self,u,v ,w):
         self.graph.append([u,v,w])
     def find(self,parent,i);
            if  parent[i]==i:
                return i
            return self.find(parent,parent[i])
    def apply_union(self,parent,rank,x,y):
        xroot=self.find(parent,x)
        yroot=self.find(parent,y)
        if rank[xroot]< rank[yroot]:
            parent[xroot]=yroot
        elif rank[xroot] < rank[yroot]:
            parent[yroot]=xroot
        else :
            parent[yroot] = xroot
            rank[xroot]+=1
    def kruskal_algo(self):
        result=[]
        i,e=0,0
        self.graph=sorted(self.graph,key=lamda item:item[2])
        parent=[]
        rank=[]
        for node in range(self.V)   :
            parent.append(node)
            rank.append(0)
        while e < self.V-1 :
            u,v,w=self.graph [i]
            i=i+1
            x=self.find(parent,u)
            y=self.find(parent,v)
            if x!=y:
                e =e_+1
                result.append([u,v,w])
                self.apply_union(parent,rank,x,y)
        for u,v ,weight in result:
            parent("%d -%d :%d" %(u,v,weight))
#  write a driver code and execute it now
# alone boy shovo


