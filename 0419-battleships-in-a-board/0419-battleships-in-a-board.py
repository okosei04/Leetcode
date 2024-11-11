class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
    #     visited = set()
        ROWS = len(board)
        COLS = len(board[0])
        res = 0
        
    #     def dfs(i, j):
    #         if i < 0 or i >= ROWS or j < 0 or j >= COLS:
    #             return
            
    #         if board[i][j] == ".":
    #             return 
            
    #         if ((i,j)) in visited:
    #             return
            
    #         visited.add((i,j))
            
    #         dfs(i + 1,  j)
    #         dfs(i-1, j)
    #         dfs(i, j + 1)
    #         dfs(i, j - 1)

    #     for r in range(ROWS):
    #         for c in range(COLS):
    #             if board[r][c] == "X" and (r,c) not in visited:
    #                 dfs(r, c)
    #                 res+= 1


    #     return res

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "X":
                    if (r == 0 or board[r-1][c] == "." ) and (c == 0 or board[r][c-1] == "."):
                        res += 1

        return res