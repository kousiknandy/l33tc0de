from typing import List

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        l = len(A)
        A = A + A
        max_sum = cur_sum = None
        i = j = k = 0
        for idx, value in enumerate(A):
            if (idx - j) >= l:
                cur_sum -= A[j]
                j += 1
            if cur_sum is None or cur_sum <= 0:
                cur_sum = value
                i = idx
            else:
                cur_sum += value
            if max_sum is None or max_sum < cur_sum:
                max_sum = cur_sum
                j = i
                k = idx
            print("  ", idx, ")", cur_sum, max_sum, value, i, j, k)    
        print(" ", max_sum, j, A[j:k+1], k)
        return max_sum

S = Solution()
print(S.maxSubarraySumCircular([3,-1,2,-1]))  # 4
print(S.maxSubarraySumCircular([1,-2,3,-2]))  # 3
print(S.maxSubarraySumCircular([5,5,5]))      # 15
print(S.maxSubarraySumCircular([5,-3,4]))     # 9
print(S.maxSubarraySumCircular([3,-2,2,-3]))  # 3
print(S.maxSubarraySumCircular([-4,-2,-3]))   # -2
