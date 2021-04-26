class Solution:
    def maxValue(self, n, index, maxSum):
        def test(a):
            b = max(a - index, 0)
            res = (a + b) * (a - b + 1) / 2
            b = max(a - ((n - 1) - index), 0)
            res += (a + b) * (a - b + 1) / 2
            return res - a

        maxSum -= n
        left, right = 0, maxSum
        while left < right:
            mid = (left + right + 1) / 2
            print mid, test(mid)
            if test(mid) <= maxSum:
                left = mid
            else:
                right = mid - 1
        return left + 1

S = Solution()
#print(S.maxValue(4,2,6))    # 2
#print(S.maxValue(3,2,148))  # 50
#print(S.maxValue(6,1,10))   # 3
print(S.maxValue(4,0,4))    # 1

