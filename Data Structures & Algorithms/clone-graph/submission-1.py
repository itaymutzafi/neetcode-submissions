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
            if node in d:
                return d[node]
            clone = Node(node.val)
            d[node] = clone

            for neigh in node.neighbors:
                d[node].neighbors.append(dfs(neigh))
            return d[node]

        return dfs(node) if node else None
                    