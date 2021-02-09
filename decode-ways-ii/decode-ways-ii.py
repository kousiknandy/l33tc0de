def wraparound(func):
    def mod1000000007(*args):
        return func(*args) % 1000000007
    return mod1000000007

class Solution:

    @wraparound
    def numDecodings(self, s: str) -> int:
        #print(" ", s)
        if len(s) == 0:
            return 1
        if s[0] == "0":
            return 0
        if s[0] == "*":
            if len(s) >= 2:
                de = 9 * self.numDecodings(s[1:])
                if s[1] in "0123456789":
                    de += self.numDecodings(s[2:])
                if s[1] in "0123456":
                    de += self.numDecodings(s[2:])
                if s[1] == "*":
                    de += 15 * self.numDecodings(s[2:]) # 11-26
                return de
            else:
                return 9
        if s[0] == "1":
            if len(s) == 1:
                return 1
            if s[1] == "*":
                return self.numDecodings(s[1:]) + 9 * self.numDecodings(s[2:])
            else:
                return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
        if s[0] == "2":
            if len(s) == 1:
                return 1
            if s[1] == "*":
                return self.numDecodings(s[1:]) + 6 * self.numDecodings(s[2:])
            elif s[1] in "0123456":
                return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
            else:
                return self.numDecodings(s[1:]) 
        return self.numDecodings(s[1:])


S = Solution()
print(S.numDecodings("*")) #9
print(S.numDecodings("1*")) #18
print(S.numDecodings("*1")) #11
print(S.numDecodings("1")) #1
print(S.numDecodings("12")) #2
print(S.numDecodings("333")) #1
print(S.numDecodings("323")) #2
print(S.numDecodings("327")) #1
print(S.numDecodings("207")) #1
print(S.numDecodings("100")) #0
print(S.numDecodings("303")) #0
print(S.numDecodings("**")) #96
print(S.numDecodings("***")) #999
print(S.numDecodings("*1*1*0")) #404
print(S.numDecodings("*0")) #2
print(S.numDecodings("*********")) #291868912





