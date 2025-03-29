class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        p = k
        s = sum(nums[:k])
        mx = s
        while p < len(nums):
            s += nums[p] - nums[p-k]
            mx = max(mx,s)
            p += 1
        return mx/k
