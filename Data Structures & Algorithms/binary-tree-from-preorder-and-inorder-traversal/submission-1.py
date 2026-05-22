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

        ind_map = {val: i for i, val in enumerate(inorder)}
        pre_ind = 0   
        
        def dfs(l, r):
            nonlocal pre_ind
            if l > r:
                return None

            curr_val = preorder[pre_ind]
            root = TreeNode(curr_val)
            pre_ind +=1
            mid = ind_map[curr_val]

            root.left = dfs(l, mid-1)
            root.right = dfs(mid + 1, r)
            return root
        
        return dfs(0, len(inorder) - 1)
        
        
        
         
