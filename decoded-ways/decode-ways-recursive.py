class Solution:
    def numDecodings(self, s: str) -> int:
        print(" ", s)
        n = 0
        if len(s) == 1:
            return 0 if s == "0" else 1 
        if len(s) == 2:
            v = int(s)
            if v == 0:
                return 0
            if v % 10 == 0:
                if v in [10, 20]:
                    return 1
                return 0
            if v <= 9:
                return 0
            if v <= 26:
                return 2
            return 1
        if s[0] == "0":
            return 0
        if s[0] == "1":
            if s[1] != "0":
                n += self.numDecodings(s[1:])
            n += self.numDecodings(s[2:])
        elif s[0] == "2":
            if s[1] in ["1", "2", "3", "4", "5", "6"]:
                n += self.numDecodings(s[1:])
            n += self.numDecodings(s[2:])
        else:
            n += self.numDecodings(s[1:])
        print(n)
        return n


S = Solution()
# print(S.numDecodings("12"))  #2 
# print(S.numDecodings("226"))  #3
# print(S.numDecodings("1532"))  #2
# print(S.numDecodings("00"))  #0
# print(S.numDecodings("01"))  #0
# print(S.numDecodings("101"))  #1
# print(S.numDecodings("230"))  #0
print(S.numDecodings("9272971672512277354953939427689518239714228293463398742522722274929422229859968434281231132695842184"))



