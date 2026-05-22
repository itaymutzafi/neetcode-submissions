# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.dfs(root, float("inf"), float("-inf"))
    
    def dfs(self, root: Optional[TreeNode], high_bound, low_bound) -> bool:
        if not root:
            return True
        if root.val >= high_bound:
            print("root val is:" + str(root.val) + "high_bound was" + str(high_bound))
            return False
        elif root.val <= low_bound:
            print("root val is:" + str(root.val) + "low_bound was" + str(low_bound))
            return False
        return self.dfs(root.left, root.val, low_bound) and self.dfs(root.right, high_bound, root.val)