class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #k that will be the topk frequencies


        freq = Counter(nums) # O(n) space O(n) time
        print(freq)


        # number, frequency in the map 


        # get the top k numbers in terms of frequency
        output = []

        for num, count in freq.items():
            output.append((count, num))

        output.sort()
        print(output)

        return [num for count, num in output[-k:]]
            

        