class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        # dfs problem, go through the entire grid and if its an island mark it 'x'
        def dfs(i, j):
            if (i < 0 or j < 0 or i >= ROWS or j >= COLS or grid[i][j] == 'X' or grid[i][j] == '0'):
                return 
            
            grid[i][j] = 'X'

            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i -1 , j)
            dfs(i, j - 1)

        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                #start of an island and 
                if grid[i][j] == '1':
                    dfs(i, j)
                    res+=1

        return res

        # time O(mn)           