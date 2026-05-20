class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_water = 0
        
        while l < r:
            width = r - l
            if heights[l] < heights[r]:
                min_height = heights[l]
                l += 1
            else:
                min_height = heights[r]
                r -= 1
                
            max_water = max(max_water, min_height * width)
       
        return max_water