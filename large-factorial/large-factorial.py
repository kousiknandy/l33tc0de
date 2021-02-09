def multiply(str, n):
    c = 0
    res = []
    for s in str[::-1]:
        i = int(s)
        p = i * n + c
        res.append(chr(48 + (p%10)))
        c = p // 10
    if c > 0:
        res.append(chr(48 + (c%10)))
        if c >= 10:
            res.append(chr(48 + (c//10)))
    return res[::-1]

class Solution:
    # @param A : integer
    # @return a strings
    def solve(self, A):
        f = ["1"]
        for i in range(A):
            f = multiply(f, (i+1))
            #print(f)
        return "".join(f)

# print(multiply("1211", 3))
# print(multiply("100", 7))
# print(multiply("7788", 8))
# print(multiply("99", 9))

S = Solution()
print(S.solve(1))
print(S.solve(5))
print(S.solve(20))
print(S.solve(99))

