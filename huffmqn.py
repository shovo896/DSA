class NodeTree(object):
    def __init__(self,left=None,right=None):
        self.left=left
        self.right=right
    def children(self):
        return (self.left,self.right)
    def nodes(self):
        ret












freq={}
for c in string :
    if c in string :
        if c in freq :
            freq[c]+=1
        else :
            freq[c]=1
freq=sorted(freq.items(),key=lambda x:x[1],reverse=True)
node=freq
while len(nodes)>1 :
    (key,c1)=nodes[-1]
    (key,c2)=nodes[-2]
    nodes=nodes[:-2]
    node=NodeTree(key1,key2)
    nodes.append((node,c1+c2))
    nodes=sorted(nodes,key=lambda x:x[1],reverse=True)
huffmanCode=huffman_code_tree(nodes[0][0])

print('Char | Huffman code')
print('--------------------------------')
for(char,frequency) in freq:
    print('%-4r | %12s'%(char,huffmanCode([char])))
