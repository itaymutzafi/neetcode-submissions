# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # two invariantes:
        # 1. preorder[0] is always the root of the current subtree.
        # 2. inorder.index(root) is the num of the node in the left side of root. since every node in the left of curr in the inorder list is in the left subTree.
        
        # not preorder - there isn't a root to check, the subtree is empty
        # not inorder - there aren't any node in the left of the curr root
              
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root
            
        
        
         
