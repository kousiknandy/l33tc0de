class Solution:
    def isMatch(self, s: str, p: str, d=1) -> bool:
        print(" " * d, s, p)
        if not p:
            return True if not s else False
        if not s:
            return True if all([y == "*" for y in p]) else False
        i = 0
        for j, c in enumerate(p):
            if i == len(s):
                return True if all([y == "*" for y in p[j:]]) else False
            if c == s[i]:
                i += 1
                continue
            if c == '?':
                i += 1
                continue
            if c != "*":
                return False
            if j == len(p)-1:
                return True
            k = j + 1
            while p[k] == "*":
                k += 1
                if k == len(p):
                    return True
            r1 = self.isMatch(s[i:], p[k:], d+1)
            if not r1:
                if i < len(s) - 1 and p[k] not in ["?", "*"]:
                    while not s[i+1] == p[k]:
                        i += 1
                        if i == len(s)-1:
                            return False
                r2 = self.isMatch(s[i+1:], p[k-1:], d+1)
            return r1 or r2
        return True if i == len(s) else False
        
S = Solution()
print(S.isMatch("zzzzzzz", "*a")) #False
print(S.isMatch("", "*")) #True
print(S.isMatch("x", "**")) #True
print(S.isMatch("abbbb", "?*b**"))
print(S.isMatch("x", "x")) #True
print(S.isMatch("aa", "a")) #False
print(S.isMatch("aa", "*")) #True
print(S.isMatch("cb", "?a")) #False
print(S.isMatch("adceb", "*a*b")) #True 
print(S.isMatch("acdcb", "a*c?b")) # False
print(S.isMatch("aaaaaaaa", "a*")) #True
print(S.isMatch("aaaaaaa", "*a"))  #True
print(S.isMatch("ho", "ho**"))  #True
print(S.isMatch("dsahdakjdhaddho", "**ho"))  #True
print(S.isMatch("babaaababaabababbbbbba", "***bba"))
print(S.isMatch("babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab", "*bba*a*bbba*aab*b")) # False
print(S.isMatch("hi", "*?"))
# print(S.isMatch("bbaaaabaaaaabbabbabbabbababaabababaabbabaaabbaababababbabaabbabbbbbbaaaaaabaabbbbbabbbbabbabababaaaaa",
#                 "******aa*bbb*aa*a*bb*ab***bbba*a*babaab*b*aa*a****"))
print(S.isMatch("babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb",
                "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"))
