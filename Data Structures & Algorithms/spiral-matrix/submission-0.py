class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0]) if rows else 0
        
        left, right = 0, cols - 1
        top, bottom = 0, rows - 1
        res = []

        while left <= right and top <= bottom:
            for i in range(left, right + 1):
               res.append(matrix[top][i]) 
            top +=1
            
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -=1

            if left <= right and top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -=1
            
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left +=1
            
        return res

        # [1,2,3,4]
        # [5,6,7,8]
        # [9,10,11,12]

        # top = 1
        # right = 2
        # bottom = 1

                