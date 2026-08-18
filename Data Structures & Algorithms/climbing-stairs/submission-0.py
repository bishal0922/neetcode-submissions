class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        

        def dfs(i):
            if i in cache:
                return cache[i]
            if i>=n:
                return i==n 
            res = dfs(i + 1) + dfs(i + 2)
            cache[i] = res
            return res
        
        return dfs(0)