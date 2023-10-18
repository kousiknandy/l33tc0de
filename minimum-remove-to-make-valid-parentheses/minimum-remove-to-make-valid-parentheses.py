class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        p, q = [], []
        for i in range(len(s)):
            if s[i] == "(": 
                p.append(i)
                continue
            if s[i] == ")":
                if len(p): p.pop()
                else: q.append(i)
        r = ""
        for i in range(len(s)):
            if i in p + q: continue
            r += s[i]
        return r
