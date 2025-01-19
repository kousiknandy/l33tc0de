class Solution:
    def minMoves(self, nums: List[int]) -> int:
        l = len(nums)
        s = 0
        m = 1e10
        for n in nums:
            s += n
            m = m if m < n else n
        return s - l*m
