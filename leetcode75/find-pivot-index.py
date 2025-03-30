class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tot = 0
        for n in nums: tot += n
        ls, rs = 0, tot 
        for i in range(len(nums)):
            if i > 0: ls += nums[i-1]
            rs -= nums[i]
            if ls == rs: return i
        return -1
