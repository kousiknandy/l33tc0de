class Solution:

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        self.sat = sorted(satisfaction, reverse=True)
        w, x, m = 0, 0, 0
        for v in self.sat:
            x += v
            w += x
            m = max(m, w)
            if x < 0: break
        return m
