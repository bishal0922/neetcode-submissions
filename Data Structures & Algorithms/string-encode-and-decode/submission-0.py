class Solution:

    def encode(self, strs: List[str]) -> str:
        #length#word


        encoded = []
        for word in strs:
            encoded.append(str(len(word)))
            encoded.append('#')
            encoded.append(word)

        return "".join(encoded)

    def decode(self, s: str) -> List[str]:

        # 5#Hello3#Gay
        # [Hello, Gay]
        output = []
        i=0
        while i < len(s):
            # get the first number 
            # stop till #

            # then get the [curr pointer: curr pointer +length of word]

            ptr = i

            while s[ptr] != '#':
                ptr +=1
            
            length = int(s[i:ptr])


            # start = ptr + 1
            # end = start + length

            # word = s[start:end]
            # output.append(word)

            word = s[ptr+1:ptr+1+length]

            output.append(word)

            i = ptr+length+1

        return output
