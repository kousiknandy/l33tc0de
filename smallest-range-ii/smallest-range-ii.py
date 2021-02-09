from typing import List

class Solution:
    def try_plusminus(self, A, K, minimum, maximum, d = 0):
        #print(" " * d, A, "<", minimum, maximum, ">")
        
        if len(A) == 0:
            if minimum is not None and maximum is not None:
                return maximum - minimum
            else:
                return 0
        skip = 0
        while True:
            valmin = A[skip] - K
            valplu = A[skip] + K
            newmin1 = minimum if minimum is not None and minimum < valmin else valmin
            newmax1 = maximum if maximum is not None and maximum > valmin else valmin
            newmin2 = minimum if minimum is not None and minimum < valplu else valplu
            newmax2 = maximum if maximum is not None and maximum > valplu else valplu
            if newmin1 != minimum or newmin2 != minimum:
                break
            if newmax1 != maximum or newmax2 != maximum:
                break
            skip += 1
            if skip >= len(A):
                break
        newdiff_m = self.try_plusminus(A[skip+1:], K, newmin1, newmax1, d+skip)
        newdiff_p = self.try_plusminus(A[skip+1:], K, newmin2, newmax2, d+skip)
        return min(newdiff_m, newdiff_p)
    
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A = sorted(A)
        diff = self.try_plusminus(A, K, None, None)
        return diff


S = Solution()
print(S.smallestRangeII([1],0))   #0
print(S.smallestRangeII([0,10],2)) #6
print(S.smallestRangeII([1,3,6],3)) #3

print(S.smallestRangeII([8038,9111,5458,8483,5052,9161,8368,2094,8366,9164,53,7222,9284,5059,4375,2667,2243,5329,3111,5678,5958,815,6841,1377,2752,8569,1483,9191,4675,6230,1169,9833,5366,502,1591,5113,2706,8515,3710,7272,1596,5114,3620,2911,8378,8012,4586,9610,8361,1646,2025,1323,5176,1832,7321,1900,1926,5518,8801,679,3368,2086,7486,575,9221,2993,421,1202,1845,9767,4533,1505,820,967,2811,5603,574,6920,5493,9490,9303,4648,281,2947,4117,2848,7395,930,1023,1439,8045,5161,2315,5705,7596,5854,1835,6591,2553,8628], 4643))
