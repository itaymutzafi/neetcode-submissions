# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # the LCA in binary search tree, is the last node that is p <= node.val <= q
        if not root:
            return
        if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
            return root
        left_LCA = self.lowestCommonAncestor(root.left, p, q)
        right_LCA = self.lowestCommonAncestor(root.right, p, q)
        return left_LCA if left_LCA else right_LCA
            
        