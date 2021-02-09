from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        bump = False
        l = len(nums)
        if l < 2:
            return True
        i = 0
        while True:
            if nums[i] <= nums[i+1]:
                i += 1
                if i == l-1:
                    break
                else:
                    continue
            if bump:
                return False
            bump = True
            if i > 0 and i < l-1:
                if not (nums[i+1] >= nums[i-1]):
                    if i < l-2:
                        if not (nums[i+2] > nums[i]):
                            return False
            i += 1
            if i == l-1:
                break
        return True

S = Solution()
print(S.checkPossibility([1,2,4,5,3]))
print(S.checkPossibility([3, 1]))
print(S.checkPossibility([2, 3, 2, 3]))
print(S.checkPossibility([2, 3, 3, 2, 4]))
print(S.checkPossibility([4, 2, 3]))
print(S.checkPossibility([4, 2, 1]))
print(S.checkPossibility([1, 2, 6, 3, 4]))
print(S.checkPossibility([1, 2, 6, 1, 4]))

