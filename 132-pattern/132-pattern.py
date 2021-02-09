from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        mstack = []
        if len(nums) < 3: return False
        smax = -2**32
        for i in range(len(nums)-1, -1, -1):
            if (nums[i] < smax): return True
            while len(mstack) and mstack[-1] < nums[i]:
                smax = mstack.pop()
            mstack.append(nums[i])
            print(nums[i], smax, mstack)
        return False

S = Solution()
print(S.find132pattern([3, 1, 4, 2]))
print(S.find132pattern([3, 5, 0, 3, 4]))
