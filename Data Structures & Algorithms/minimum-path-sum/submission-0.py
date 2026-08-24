class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        INF = float('inf')

        dp = [[INF] * (n+1) for _ in range(m+1)]
        dp[m-1][n-1] = grid[m-1][n-1]

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                low = min(dp[i+1][j], dp[i][j+1]) 

                dp[i][j] = min(dp[i][j], low+grid[i][j])

        
        return dp[0][0]

