from typing import List

class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        if len(x) < 4: return False
        for i in range(3, len(x)):
            if x[i] >= x[i-2] and x[i-1] <= x[i-3]: return True
            if i >= 4:
                if x[i] + x[i-4] >= x[i-2] and x[i-1] == x[i-3]: return True
            if i >= 5:
                if x[i] + x[i-4] >= x[i-2] and x[i-2] >= x[i-4] \
                   and x[i-1] + x[i-5] >= x[i-3] and x[i-1] <= x[i-3]: return True
        return False

S = Solution()
print(S.isSelfCrossing([2,1,1,2])) # true
print(S.isSelfCrossing([1,2,3,4])) # false
print(S.isSelfCrossing([1,1,1,1])) # true
print(S.isSelfCrossing([1,1,1,1])) # true
print(S.isSelfCrossing([2,1,3,2,2,2])) # true
print(S.isSelfCrossing([1,1,2,1,1])) # true
print(S.isSelfCrossing([3,3,3,2,1,1])) # false
