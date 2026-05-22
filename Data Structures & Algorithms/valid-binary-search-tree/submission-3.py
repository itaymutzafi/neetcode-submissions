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
        return self.dfs(root.left, min(root.val, high_bound), low_bound) and self.dfs(root.right, high_bound, max(low_bound, root.val))
        
            
        # if not root:
        #     return 
        # left = self.isValidBST(root.left)
        # right = self.isValidBST(root.right)

        #         5
        #     3       7
        #   2   4   6   8
        
        # # each leaf return True
        # then 3 return True
        # but how we know that 4 is <= 5 and not 7? 
        # since right now we know that 4 >= 3 but no that 3 <= 4 <= 5
        # track all parents over the traversal. and you have to be lower / greater than your parents

        