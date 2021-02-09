from typing import List

class Solution:
    def canPartition_bottomup(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False
        total //= 2
        mem = [[False for _ in range(total+1)] for _ in range(len(nums))]
        for i in range(len(nums)):
            mem[i][0] = True
        for s in range(1, total+1):
            mem[0][s] = True if nums[0] == s else False
        for i in range(1, len(nums)):
            for s in range(1, total+1):
                if mem[i-1][s]:
                    mem[i][s] = True
                else:
                    mem[i][s] = mem[i-1][s-nums[i]] if s >= nums[i] else False
            for i in range(len(nums)): print(mem[i])
            else: print()
        return mem[len(nums)-1][total]

    def canPartition_topdown(self, nums: List[int]) -> bool:
        def print_mem(func):
            def inner_func(mem, nums, curindex, total):
                r = func(mem, nums, curindex, total)
                print(curindex, total)
                for i in range(len(nums)): print(mem[i])
                else: print()
                return r
            
            return inner_func

        @print_mem
        def canPartition_topdown_recursive(mem, nums, curindex, total):
            if total == 0: return True
            if len(nums) == 0 or curindex >= len(nums): return False
            if mem[curindex][total] is not None:
                return mem[curindex][total]
            if total >= nums[curindex]:
                r = canPartition_topdown_recursive(mem, nums, curindex+1, total-nums[curindex])
                if r:
                    mem[curindex][total] = True
                    return True
            r = canPartition_topdown_recursive(mem, nums, curindex+1, total)
            mem[curindex][total] = r
            return r

        total = sum(nums)
        if total % 2: return False
        total //= 2
        mem = [[None for _ in range(total+1)] for _ in range(len(nums))]
        return canPartition_topdown_recursive(mem, nums, 0, total)

    canPartition = canPartition_topdown

S = Solution()
print(S.canPartition(nums = [1,5,11,5]))
