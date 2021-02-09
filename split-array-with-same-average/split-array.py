from typing import List

class Solution:
    def searchnear(self, arr, x, l, r, delt=True):
        if (r - l) == 1:
            if arr[l] == x:
                return arr[l]
            if delt:
                if arr[l] > x:
                    return arr[l]
                return None
            else:
                if arr[l] < x:
                    return arr[l]
                return None
        m = l + ((r -l) // 2)
        if arr[m] == x:
            return arr[m]
        

    def splitArraySameAverage(self, A: List[int]) -> bool:
        arr = sorted(A)
        length = len(A)
        fullavg = sum(A)/len(A)
        left = []
        right = arr
        
