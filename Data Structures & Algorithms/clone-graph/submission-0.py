"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# undirected -> it means that all the neighbors are two sided
# iterate over the whole graph with dfs, create a hashmap, and then iterate again

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        d = {}
        
        def dfs(node):
            if not node or node in d:
                return
            clone = Node(node.val)
            d[node] = clone
            for neigh in node.neighbors:
                dfs(neigh)
              
        dfs(node)
        
        for old_node in d:
            for neigh in old_node.neighbors:
                d[old_node].neighbors.append(d[neigh])

        return d[node] if node else None
                    