class Solution:    
    def isValidSudoku(self, board: List[List[str]]) -> bool:    
        for r in range(len(board)):
            seen = set()
            for c in range(len(board[0])):
                if board[r][c] in seen:
                    print(f"have problem in r {r}, seen is {seen} and board[r][c] is {board[r][c]}")
                    return False
                if board[r][c] != ".":
                    seen.add(board[r][c])
        
        for c in range(len(board[0])):
            seen = set()
            for r in range(len(board)):
                if board[r][c] in seen: 
                    return False
                if board[r][c] != ".":
                    seen.add(board[r][c])
        
        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                seen = set()
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        if board[r][c] in seen:
                            return False
                        if board[r][c] != ".":
                            seen.add(board[r][c])
        
        return True
        
        
            