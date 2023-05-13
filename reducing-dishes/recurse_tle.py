class Solution:
    @lru_cache
    def like_time(self, i, t):
        if i >= len(self.sat): return 0
        c = self.sat[i]*t + self.like_time(i+1, t+1)
        d = self.like_time(i+1, t)
        return max(c,d)

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        self.sat = sorted(satisfaction)
        return self.like_time(0,1)
