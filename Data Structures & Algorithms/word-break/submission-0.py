class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True

        print(dp)


        for i in range(len(s)-1,-1, -1):
            #at each index see if we can build the string

            for word in wordDict:
                if i+len(word)-1 < len(s) and s[i:i+len(word)] == word:
                    #it is the word
                    dp[i] = dp[i + len(word)]
                
                if dp[i]: break
        
        return dp[0]


        