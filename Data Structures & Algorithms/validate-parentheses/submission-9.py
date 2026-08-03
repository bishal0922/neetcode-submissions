class Solution:
    def isValid(self, s: str) -> bool:
        #use stack
        match = {
            #end, start
            ')': '(',
            ']': '[',
            '}': '{'
        }
        print(match)

        stack = []
        #pop nd append

        #consume string
        for c in s:
            if c in match:
                if stack and match[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

            #if its an ending we're consuming, pop the starting half
        
        return True if len(stack) == 0 else False 