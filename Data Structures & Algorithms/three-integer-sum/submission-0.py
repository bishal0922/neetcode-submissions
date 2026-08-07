class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        n = len(nums)
        res = set()

        for i in range(n):

            comp = 0 - nums[i]

            j = i +1
            k = n - 1

            while j < k:
                total = nums[j] + nums[k]
                if total == comp:
                    res.add(tuple([nums[i], nums[j], nums[k]]))
                    j+=1
                    k-=1
                elif total > comp: 
                    k-=1
                elif total < comp: 
                    j+=1

            
        return list(res)



        