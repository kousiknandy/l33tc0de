class Solution:
    def convertToTitle(self, n: int) -> str:
        title = []
        while n > 0:
            let = n % 26
            n = (n - 1) // 26
            title.insert(0, chr(ord('A')+((let-1)%26)))
        return "".join(title)

S = Solution()
print(S.convertToTitle(1))
print(S.convertToTitle(26))
print(S.convertToTitle(27))
print(S.convertToTitle(28))
print(S.convertToTitle(100))
print(S.convertToTitle(701))
print(S.convertToTitle(1000000))
