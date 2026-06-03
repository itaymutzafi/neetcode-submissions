# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.cnt = 0

        def dfs(root, max_node):
            if not root:
                return
            if root.val >= max_node:
                self.cnt +=1
            max_node = max(max_node, root.val)
            dfs(root.left, max_node)
            dfs(root.right, max_node)
        
        dfs(root, root.val)
        return self.cnt
                
