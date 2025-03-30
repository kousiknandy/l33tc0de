class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt, mx = 0, 0
        for g in gain:
            alt += g
            mx = max(mx, alt)
        return mx
