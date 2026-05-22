# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0

        def inorder(root: Optional[TreeNode]) -> Optional[TreeNode]:
            if not root:
                return              
            left_node = inorder(root.left)
            nonlocal cnt
            cnt +=1
            if cnt == k:
                return root.val
            right_node = inorder(root.right)
            return left_node if left_node else right_node


            
        return inorder(root)
