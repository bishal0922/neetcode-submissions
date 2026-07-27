class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = Counter(nums)
        maxn = 0
        output = 0
        for x, y in map.items():
            if y > maxn:
                output = x
                maxn = y

        return output

        