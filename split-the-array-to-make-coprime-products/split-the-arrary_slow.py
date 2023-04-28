class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        @lru_cache
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        li = 0
        for ix, n in enumerate(nums):
            for i in range(len(nums)-1, li,-1):
                if gcd(n, nums[i]) != 1:
                    li = max(li, i)
                    break
            if li == len(nums) - 1: return -1
            if li == ix:
                break
        return li
