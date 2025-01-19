class Solution:
    def minMoves(self, nums: List[int]) -> int:
        l = 0
        s = 0
        m = 1e10
        for n in nums:
            l += 1
            s += n
            m = min(m,n) 
        return s - l*m
