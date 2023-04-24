class Solution:
    @lru_cache
    def substr_check(self, i, j):
        if len(self.s) - i < len(self.t) - j: return 0
        if i == len(self.s): return 0
        # print(self.s[i:], self.t[j:])
        while self.t[j] != self.s[i]: 
            i += 1
            if i >= len(self.s): return 0
        if j == len(self.t) - 1:
            p1 = 1
        else:
            p1 = self.substr_check(i+1, j+1)
        p2 = self.substr_check(i+1, j)
        return p1 + p2

    def numDistinct(self, s: str, t: str) -> int:
        self.s = s
        self.t = t
        return self.substr_check(0,0)
