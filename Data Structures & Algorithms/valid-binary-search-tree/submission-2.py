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
        left_rec = self.isValidBST(root.left)
        right_rec = self.isValidBST(root.right)
        left = self.dfs(root.left, root, "left")
        right = self.dfs(root.right, root, "right")
        return left and right and left_rec and right_rec
    
    def dfs(self, root: Optional[TreeNode], parent, direction) -> bool:
        if not root:
            return True
        if direction == "right" and root.val <= parent.val or direction == "left" and root.val >= parent.val:
            return False
        return self.dfs(root.left, parent, direction) and self.dfs(root.right, parent, direction)
            
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

        