class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        rows = len(board)
        cols = len(board[0])        

        def helper(i, j, word_i):
            if i >= len(board) or i < 0 or j >= len(board[0]) or j < 0 or board[i][j] is None:
                return False
            curr = board[i][j]
            if curr != word[word_i]:
                return False
            
            if word_i == len(word) - 1:
                return True

            board[i][j] = None            
            for dx, dy in self.dirs:
                if helper(i + dx, j + dy, word_i + 1):
                    board[i][j] = curr
                    return True
            
            board[i][j] = curr
            return False

        for i in range(rows):
            for j in range(cols):
                tmp = []       
                if helper(i, j, 0):
                    return True
        return False
            