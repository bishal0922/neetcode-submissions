class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        store = defaultdict(list)

        for word in words:
            bucket = [0] * 26
            for w in word:
                bucket[ord(w) - ord('a')]+=1

            store[tuple(bucket)].append(word)
        
        return list(store.values())



        