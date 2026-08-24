class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        n = len(nums)

        for i in range(n):
            comp = target - nums[i]

            if comp in seen: return [ seen[comp], i]
        
            seen[nums[i]] = i
        
        return [-1,-1]
        