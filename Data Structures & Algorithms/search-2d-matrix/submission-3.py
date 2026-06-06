class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:      
        rows, cols = len(matrix), len(matrix[0]) 

        def binary_search(L, target):
            l, r = 0, len(L) - 1
            
            while l <= r:
                mid  = (l + r) // 2
                if L[mid] == target:
                    return True
                if L[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return False



        for r in range(rows):
            if matrix[r][0] <= target <= matrix[r][-1]:
                return binary_search(matrix[r], target)        
        return False

        
                

        
        

        
        