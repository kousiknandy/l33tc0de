class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ceildiv = lambda x, y: -(x//-y)
        hours = lambda piles, k: sum(ceildiv(p,k) for p in piles)
        hh = 1
        while hours(piles, hh) > h: hh *= 2
        l, r = hh//2, hh
        while l < r:
            m = l + (r-l)//2
            if m == 0: return ceildiv(piles[0],h)
            if hours(piles, m) > h: l = m + 1
            else: r = m
        return l
