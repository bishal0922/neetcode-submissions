class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #k that will be the topk frequencies


        freq = Counter(nums) # O(n) space O(n) time

        bucket = [[] for i in range(len(nums) + 1)]

        for num, count in freq.items():
            #bucket store freq and the nums
            bucket[count].append(num)
        
        res = []

        #Iterate from the back

        for i in range(len(bucket)- 1, 0, -1):
            #we are in a array
            for num in bucket[i]:
                res.append(num)

                if len(res) == k: return res
                

        return None
