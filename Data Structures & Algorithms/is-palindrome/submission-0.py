class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        s = s.lower()
        print(s)


        while left < right:
            #if either left or right non alphnum
            if not s[left].isalnum():
                left+=1
                continue
            if not s[right].isalnum():
                right-=1
                continue

            # the num is alpha numberica
            if s[left] != s[right]:
                return False
            if s[left] == s[right]:
                left+=1
                right-=1
        

        return True

