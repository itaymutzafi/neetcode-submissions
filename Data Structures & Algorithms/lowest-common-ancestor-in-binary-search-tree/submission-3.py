# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # the LCA in binary search tree, is the last node that is p <= node.val <= q
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < q.val and root.val < p.val:
                root = root.right
            else:
                return root