from typing import List

class Solution:
    def searchnear(self, arr, x, delt=True):
        for idx, v in enumerate(arr):
            if v < x:
                continue
            if v == x:
                arr.remove(v)
                return v
            if delt:
                arr.remove(v)
                return v
            if idx == 0:
                break
            v = arr[idx-1]
            arr.remove(v)
            return v
        return None

    def splitArraySameAverage(self, A: List[int]) -> bool:
        arr = sorted(A)
        left = []
        right = arr
        if len(arr) < 2:
            return False
        rightavg = sum(right)/len(right)
        v = self.searchnear(right, rightavg)
        left.append(v)
        leftavg = v
        righavg = sum(right)/len(right)
        while leftavg != rightavg:
            delt = leftavg < rightavg
            v = self.searchnear(right, rightavg, delt)
            if not v:
                break
            if len(right) == 0:
                break
            left.append(v)
            rightavg = sum(right)/len(right)
            leftavg = sum(left)/len(left)
            print(left, leftavg, right, rightavg)
        return leftavg == rightavg

S = Solution()
#print(S.splitArraySameAverage([1,2,3,4,5,6,7,8]))
#print(S.splitArraySameAverage([2,12,18,16,19,3]))
print(S.splitArraySameAverage([10,29,13,53,33,48,76,70,5,5]))
