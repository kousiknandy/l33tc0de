class Solution:
    def removeStars(self, s: str) -> str:
        l = list(s)
        s,f = 0,0
        for i in range(len(l)):
            if l[i] != '*':
                l[s] = l[i]
                s += 1
            else:
                s -= 1
        return ''.join(l[:s])
