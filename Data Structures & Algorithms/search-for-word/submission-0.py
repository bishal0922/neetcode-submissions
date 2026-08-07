class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #define ROWS COWLS and visited

        ROWS, COLS = len(board), len(board[0])
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(r, c, i):
            # if len is len of our word ex cat if i = 3 we already met c, a, t
            if i == len(word):
                return True

            # if out of bounds or visited or not the char we want
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != word[i] or visited[r][c]):
                return False

            #tail
            visited[r][c] = True
            res = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or 
                dfs(r, c + 1, i + 1) or 
                dfs(r, c - 1, i + 1) 
            )
            visited[r][c] = False

            return res
            

        for r in range(ROWS):
            for c in range(COLS):
                #pass in first  char
                if dfs(r, c, 0):
                    return True


        return False


        