class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        n = len(nums)

        def dfs(i):
            if i >= n:
                return 0

            if i in cache: return cache[i]
            
            res = max(dfs(i+1), nums[i] + dfs(i+2))
            cache[i] = res

            return res
        
        return dfs(0)