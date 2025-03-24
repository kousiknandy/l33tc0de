class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [x for x in nums if x]
        if len(nums) - len(arr) >= 2:
            return [0] * len(nums)
        prod = 1
        for a in arr: prod *= a
        if len(nums) - len(arr) == 1:
            l = nums.index(0)
            return ([0] * l) + [prod] + ([0] * (len(nums) - l - 1))
        return [prod//x for x in nums]
