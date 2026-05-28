class Solution:
    def trap(self, height: List[int]) -> int:       
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
                
            

                