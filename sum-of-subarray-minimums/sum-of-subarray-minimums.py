from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        subsum = 0
        for l in range(1,len(arr)+1):
            minq = []
            for i in range(l):
                for j in range(len(minq)-1, -1, -1):
                    if minq[j][0] > arr[i]:
                        minq.pop(j)
                    else: break
                minq.append((arr[i],i))
            for i in range(len(arr)-l+1):
                #print(l, i, minq, arr[i:i+l])
                subsum += minq[0][0]
                if minq[0][1] <= i:
                    minq.pop(0)
                for j in range(len(minq)-1, -1, -1):
                    if i+l < len(arr) and minq[j][0] > arr[i+l]:
                        minq.pop(j)
                    else: break
                if i+l < len(arr):
                    minq.append((arr[i+l],i+l))
        return subsum

S = Solution()
print(S.sumSubarrayMins([3,1,2,4])) # 17
print(S.sumSubarrayMins([11,81,94,43,3])) # 444
