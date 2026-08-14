class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        def countpalindrome(s, l, r):
            best = 0
            while l >=0 and r < len(s) and s[l] == s[r]:
                best+=1
                l-=1
                r+=1
            
            return best

        for i in range(len(s)):
            result +=countpalindrome(s, i, i+1) #even
            result +=countpalindrome(s, i, i) #odd

        return result


        #iterate through the string
            #check for palidrome
                # res# count be odd 
                # count the even
        
        #dfe check pali( stakes int he string, l and right)

            #while left and right in bounds and l == r: # it is a palindorme
                #we found one
                #search out wide
        