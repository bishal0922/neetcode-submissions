class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #anagram is prety much Counter(s) = Counter(t)

        # iterate through strs, get the Counter, group the ones with similar counter

        #dict that with [] -> [[], []...]
        map = defaultdict(list)
        print(map)
        for s in strs:
            #compute the 0-2
            bucket = [0] * 26
            for c in s:
                bucket[ord(c) - ord('a')]+=1

            print(tuple(bucket))
            map[tuple(bucket)].append(s)


        return list(map.values())
        