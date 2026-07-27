class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # pretty much one pointer to follow 
        # one pointer to iterate through the number


        #output of the numbers after removing 'val'
        output = 0
        follower = 0

        # [1,2,3]

        for i in range(len(nums)):
            if nums[i] != val:
                nums[follower] = nums[i]
                follower += 1

            #if not val continue?
           

        return follower