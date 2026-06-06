class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        curr = nums[0]
        while nums[curr] != "":
            tmp = curr
            curr = nums[curr]
            nums[tmp] = ""
        
        return curr

        # [1,2,3,4,4] -> [1,2,"","",""]
        #  0,...,n

            
            
        
            
        
        

        