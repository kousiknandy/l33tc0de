import string

class Solution:
    def isMatch(self, s: str, p: str, c: str = None) -> bool:
        print("s:", s, "p:", p, "(",c,")")
        if s and not p:
            if c and s[0] == c:
                return self.isMatch(s[1:], p, c)
            return False
        if not s:
            if not p:
                return True
            if len(p) > 1 and all(map(lambda x: x == "*", p[1:])):
                return True
            if len(p) > 1 and p[1] == "*":
                return self.isMatch(s, p[2:])
            return False
        if p[0] in string.ascii_lowercase:
            if len(p) > 1 and p[1] == "*":
                if self.isMatch(s, p[2:]):
                    return True
                run = 0
                while run < len(s) and s[run] == p[0]:
                    res = self.isMatch(s[run+1:], p[2:], s[0])
                    if res:
                        return res
                    run += 1
                return False
            else:
                 if s[0] != p[0]:   
                     return False
                 else:
                     return self.isMatch(s[1:], p[1:])
        elif p[0] == ".":
            if len(p) > 1 and p[1] == "*":
                if self.isMatch(s, p[2:]):
                    return True
                run = 0
                while run < len(s):
                    res = self.isMatch(s[run+1:], p[2:])
                    if res:
                        return res
                    run += 1
                return False
            else:
                return self.isMatch(s[1:], p[1:])
        elif p[0] == "*":
            run = 0
            while run < len(s) and s[run] == c:
                res = self.isMatch(s[run+1:], p[2:], s[0])
                if res:
                    return res
                run += 1
            return False
        else:
            return False

S = Solution()
print(S.isMatch("a", "aa")) #False
print(S.isMatch("abcd", "abcd"))  #True
print(S.isMatch("aaaa", "a*")) #True
print(S.isMatch("aaaaaab", "a*b")) #True
print(S.isMatch("aaaac", "a*b")) #False
print(S.isMatch("ab", ".*")) #True
print(S.isMatch("aab", "c*a*b")) #True
print(S.isMatch("mississippi", "mis*is*p*.")) #False
print(S.isMatch("a", "ab*")) #True
print(S.isMatch("ab", ".*..")) #True
print(S.isMatch("", "c*c*")) #True


