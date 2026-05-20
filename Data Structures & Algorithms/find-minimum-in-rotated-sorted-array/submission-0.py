class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        # the element that we want to find is the one that nums[i] > nums[i+1]
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[right]
   
                
                
            
            # len(L) = 6
            # mid = 3, so object = 6
            # mid >= left >= right
            # so the minimum is in the right part
            # so left = mid + 1
            # mid = 5, so object = 5
            # and this is the answer

            # len = 6
            # mid = 3
            # so obj = 1
            # mid <= right <= left
            # when left <= mid <= right, then we know that this is the sorted list


            
            

                    
                
                
            
            # len(L) = 6
            # mid = 3, so object = 6
            # mid >= left >= right
            # so the minimum is in the right part
            # so left = mid + 1
            # mid = 5, so object = 5
            # and this is the answer

            # len = 6
            # mid = 3
            # so obj = 1
            # mid <= right <= left
            # when left <= mid <= right, then we know that this is the sorted list


            
            
