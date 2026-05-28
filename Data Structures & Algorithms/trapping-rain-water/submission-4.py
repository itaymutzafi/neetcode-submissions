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
        
        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        res = 0
        
        while left < right:
            if height[left] < height[right]:
                left +=1
                if max_left > height[left]:
                    res += max_left - height[left]
                else:
                    max_left = height[left]            
            else:
                right -=1
                if max_right > height[right]:
                    res += max_right - height[right]
                else:
                    max_right = height[right]

        return res
                
            

                