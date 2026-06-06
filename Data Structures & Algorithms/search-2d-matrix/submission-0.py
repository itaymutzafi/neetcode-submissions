class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # [0,0], [2,3] -> mid is [1,1]
        # matrix [1,1] is 11 > 10, so r_row = mid_row, r_col = mid_col - 1
        
        # 0,..,11 (included)
        
        # i = number // cols (cols = 4)
        # j = number // row (rows = 3)

        # 0 -> [0,0]
        # 11 => row = 11 // cols -> 2
        # col = 11 - (row * cols) -> 3

        # 10 => row = 10 // cols -> 2
        # col = 10 - (row * cols) -> 2
        
        # 9 => row = 9 // cols -> 2
        # col = 9 - 2 * cols => 1
        
        rows, cols = len(matrix), len(matrix[0]) 
        l, r = 0, rows * cols - 1
        
        while l <= r:
            mid = (l + r) // 2
            print(mid)
            i = mid // cols
            j  = mid - (i * cols)
            print(matrix[i][j])
            
            if matrix[i][j] == target:
                return True
            
            if matrix[i][j] < target:
                l = mid + 1
            
            else:
                r = mid - 1
        
        return False
                

        
        

        
        