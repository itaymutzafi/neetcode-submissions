# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # 1 -> 2,3 children,..
        # 2 -> 4,5 children,..
        # 3 -> 6,7 children,...
        
        # "1$2$3$N$N$4$5"
        # [1,2,3,N,N,4,5]
        # if 2*(i+1) exist -> 2*(i+1), 2*(i+1) + 1 are the children of node(i)

        L = []
        def bfs(root):
            q = deque()
            if root:
                q.append(root)
            while q:
                for _ in range(len(q)):
                    curr = q.popleft()    
                    ch = str(curr.val) if curr else "N"
                    L.append(ch)
                    if curr:
                        q.append(curr.left)
                        q.append(curr.right)
        
        bfs(root)
        s = "$".join(L)
        return s       
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        L = data.split("$")
        q = deque()
        i = 1
        
        root = TreeNode(L[0])
        q.append(root)
        
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if L[i] != "N":
                    node = TreeNode(int(L[i]))
                    curr.left = node
                    q.append(node)
                i +=1
                if L[i] != "N":
                    node = TreeNode(int(L[i]))
                    curr.right = node
                    q.append(node)
                i +=1
        
        return root
            
            
            

                
            

