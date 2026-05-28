class Solution:
    def trap(self, height: List[int]) -> int:
        # [0,2,0,3,1,0,1,3,2,1]
        #  ^ ^                           
        # always we look from max_left. and just increase when we have max_left <= max_right
        # max_left = 0
        # max_right = 2, so right is the new max_left.
        # right = 0, so can get 2 more water
        # then right = 3, so this is a new wall. so push the left to the right and then push right +=1
        # right is less than left, so add the water. 
        # right is less than left, so again.
        #until right == left, so don't add nothing and then do left = right.
        # and then we don't have more right >= left so don't add nothing.

        # [4,2,0,3,2,5]
        #  ^ ^
        # best_left = 4
        # right is 2, so add 2.
        # right is 
        # we need to add the r - l for the curr_window, until we have new window. 
        
        max_area = 0
        
        for i in range(len(height)):
            max_left = max_right = height[i]
            for left in range(i):
                max_left = max(max_left, height[left])
            for right in range(i, len(height)):
                max_right = max(max_right, height[right])
            
            max_area += min(max_right, max_left) - height[i]
        
        return max_area
                
            

                