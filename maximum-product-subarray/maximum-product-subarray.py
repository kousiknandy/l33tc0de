from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mproductx = [(0, 0)] * (len(nums)+1)
        mproductx[len(nums)] = (1, 1)
        results = []
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                results.append(mproductx[i+1][0])
            mxm = max(nums[i], mproductx[i+1][0]*nums[i], mproductx[i+1][1]*nums[i])
            mnm = min(nums[i], mproductx[i+1][1]*nums[i], mproductx[i+1][0]*nums[i])
            mproductx[i] = (mxm, mnm)
        print(mproductx, results)
        if results:
            return max(mproductx[0][0], max(results))
        else:
            return mproductx[0][0]
    
S = Solution()
print(S.maxProduct([2,3,-2,4]))
print(S.maxProduct([-3,-1,-1]))
print(S.maxProduct([0,2]))
print(S.maxProduct([3,-1,4]))
