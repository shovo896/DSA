import collections
def bfs (graph,root):
    visited,queue=set(),collections.deque([root])
    visited.add(root)
    while  queue :
        vertex=queue.popleft()
        print(str(vertex)+"",end="")
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

if __name__=='__main__':
    graph={0: [1,2],1:[2],2:[3],3:[1,2]}
    print("Following in Breadth First Tranversal:")
    bfs(graph,0)
