class Solution:
        
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)
        f = (x for x in range(1, l) if l % x == 0)
        for p in f:
            for i in range(l//p - 1):
                # print(" ", s[p*i:p*(i+1)],"?=", s[p*(i+1):p*(i+2)])
                if s[p*i:p*(i+1)] != s[p*(i+1):p*(i+2)]:
                    break
            else:
                return True
        return False

S = Solution()
print(S.repeatedSubstringPattern("abababab"))
print(S.repeatedSubstringPattern("abcabcabcabc"))
print(S.repeatedSubstringPattern("abcabcxxabcabc"))

