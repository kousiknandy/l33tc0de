from typing import List

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        for i, n in enumerate(nums):
            if i < 2: continue
            if n == 0: continue
            direx = n > 0
            nums[i] = 0
            cylen = 0
            while True:
                print(nums)
                j = (i + n) % len(nums)
                if j == i: break
                n = nums[j]
                if n == 0:
                    if cylen: return True
                    break
                if direx and n < 0: break
                if not direx and n > 0: break
                i = j
                nums[i] = 0
                cylen += 1
        return False

S = Solution()
print(S.circularArrayLoop([2,-1,1,2,2]))
print(S.circularArrayLoop([-1, 2]))
print(S.circularArrayLoop([-2,1,-1,-2,-2]))
print(S.circularArrayLoop([-1,-2,-3,-4,-5]))
print(S.circularArrayLoop([2,2,2,2,2,4,7]))
