from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        if l < 2: return 0
        jump = 0
        start = 1
        end = min(nums[0], l-1)
        while start < l:
            jump += 1
            next_start = end + 1
            for j in range(start, end+1):
                end = max(end, min(j + nums[j], l-1))
            start = next_start
        return jump

S = Solution()
print(S.jump(nums = [2,3,1,1,4]))  # 2
print(S.jump(nums = [2,3,0,1,4]))  # 2
print(S.jump(nums = [2,1]))  # 1
