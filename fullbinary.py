class Node : 
    def __init__ (self,item) :
        self.item = item 
        self.leftChild = None 
        self.rightChild = None 
def isFullTree(root) : 
    if root is None : 
        return True 
    if root.leftChild is None and root.rightChild is not None : 
        return True
    if root.leftChild is not None and root.rightChild is not None : 
        return (isFulltree(root.leftchild) and isFullTree(root.rightChild))
    return False 
root= Node(1)
root.leftChild = Node(2)
root.rightChild = Node(3)
root.leftChild.leftChild = Node(4)
root.leftchild.rightChild = Node(5)
if isFullTree(root) :
    print("The tree is a full binary tree")
else : 
    print("The tree is not a full binary tree")