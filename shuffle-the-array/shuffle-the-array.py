from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        def swap(x, n):
            y = (x-1)//2+n if x %2 else x//2
            print(x, y, end=", ")
            return y
        swapwith = lambda x: 2*x if x < n else 2*(x-n)+1
        res = [nums[swap(i,n)] for i in range(2*n)]
        return res
        
S = Solution()
print(S.shuffle([1,3,5,7,9, 2,4,6,8,10], 5)) 
