# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    from collections import deque
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")
        
        def dfs(root):
            if not root:
                return 0
            left_sum = dfs(root.left) 
            right_sum = dfs(root.right)
            curr_sum = root.val
            curr_sum += left_sum if left_sum > 0 else 0
            curr_sum += right_sum if right_sum > 0 else 0
            self.max_sum = max(self.max_sum, curr_sum)
            return max(root.val, root.val + left_sum, root.val + right_sum)
        
        q = deque([root])
        
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                dfs(curr)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        
        return self.max_sum
                

        
         
