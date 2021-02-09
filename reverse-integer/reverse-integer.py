class Solution:
    def reverse(self, x: int) -> int:
        sign = True if x < 0 else False
        if sign:
            x = -x
        y = 0
        while x:
            y = (10 * y) + (x % 10)
            x = x // 10
        if not (-2**31 <= y <= 2**31-1):
            y = 0
        return -y if sign else y

    
S = Solution()
print(S.reverse(15))
print(S.reverse(1500))
print(S.reverse(1005))
print(S.reverse(1))
print(S.reverse(-15))
print(S.reverse(0))
print(S.reverse(-1500))
print(S.reverse(-100005))
print(S.reverse(66666666666636464646464646464099))

