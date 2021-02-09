from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = -1, len(nums)-1
        if r < 0: return [-1, -1]
        while r - l > 1:
            m = l + (r-l)//2
            if nums[m] >= target:
                r = m
            else:
                l = m
            print(">", l, m, "(", nums[m], ")", r)
        left = r if nums[r] == target else -1
        l, r = 0, len(nums)
        while r - l > 1:
            m = l + (r-l)//2
            if nums[m] <= target:
                l = m
            else:
                r = m
            print("<", l, m, "(", nums[m], ")", r)
        right = l if nums[l] == target else -1
        if right < left:
            left, right = right, left
        return [left, right]

S = Solution()
print(S.searchRange([1,3], 1))
print(S.searchRange([5,7,7,8,8,10], 8))
