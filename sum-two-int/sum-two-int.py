class Solution:
    def addints(self, a: int, b: int, c: int) -> (int, int):
        addtable = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                    [3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                    [4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
                    [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
                    [6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                    [7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                    [8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                    [9, 10, 11, 12, 13, 14, 15, 16, 17, 18]]
        sum = addtable[a][b]
        digit = sum % 10
        digit = addtable[digit][c]
        carry = sum // 10
        return carry, digit
        
    def getSum(self, a: int, b: int) -> int:
        digits = lambda x: map(int, str(x)[::-1])
        a_l = list(digits(a))
        b_l = list(digits(b))
        l = max(len(a_l), len(b_l))
        c = 0
        sum = []
        for i in range(l):
            c, d = self.addints(a_l[i] if i < len(a_l) else 0,
                                b_l[i] if i < len(b_l) else 0,
                                c)
            sum.append(d)
        sum = [str(x) for x in sum[::-1]]
        return int("".join(sum))

S = Solution()
# print(S.addints(2, 3, 0))
# print(S.addints(2, 3, 1))
# print(S.addints(8, 6, 0))
# print(S.addints(8, 6, 1))
print(S.getSum(234, 694))
