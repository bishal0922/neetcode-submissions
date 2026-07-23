class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        N = len(nums)
        seen = {}

        for i in range(N):

            comp = target - nums[i]

            if comp in seen:
                return [seen[comp], i]
            seen[nums[i]] = i

        return [-1,-1]
            

        