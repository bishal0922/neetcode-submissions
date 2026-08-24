class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[ROWS-1][COLS-1] == 1: return 0
        if obstacleGrid[0][0] == 1: return 0
        dp = [[0] * (COLS + 1) for _ in range(ROWS+1)]
        dp[ROWS-1][COLS-1] = 1

        for i in range(ROWS):
            for j in range(COLS):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = '#'

        print(dp)



        for i in range(ROWS-1, -1,-1):
            for j in range(COLS-1,-1,-1):
                if dp[i][j] == '#': continue

                #sum of right and down
                    #if right is # use 0
                right = 0 if dp[i][j+1]== '#' else dp[i][j+1]
                down = 0 if dp[i+1][j]== '#' else dp[i+1][j]

                dp[i][j] += right+down
        
        return dp[0][0]



        