class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        rows = len(board)
        cols = len(board[0])

        def helper(s, i, j):
            if i >= len(board) or i < 0 or j >= len(board[0]) or j < 0 or board[i][j] is None:
                return False
            curr = board[i][j]
            s.append(curr)
            board[i][j] = None
            if "".join(s) == word:
                return True
            
            for dx, dy in self.dirs:
                if helper(s, i + dx, j + dy):
                    return True
            s.pop()
            board[i][j] = curr
            return False

        
        for i in range(rows):
            for j in range(cols):
                tmp = []        
                if helper(tmp, i, j):
                    return True
        return False
            