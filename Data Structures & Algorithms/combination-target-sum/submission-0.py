class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        i = 0



        def dfs(i, solve, total):
            if total == target:
                res.append(solve.copy())
                return
            if i >= len(nums) or total > target:
                return

            solve.append(nums[i])
            dfs(i, solve, total + nums[i])
            solve.pop()
            dfs(i +1 , solve, total)
        
        dfs(i, [], 0)

        return res
        