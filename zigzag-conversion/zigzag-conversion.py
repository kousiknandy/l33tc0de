class Solution:
    def convert(self, s: str, numRows: int) -> str:
        cycles = -(-len(s) // numRows)
        result = ""
        for i in range(numRows):
            for c in range(cycles):
                offset = c * (2*numRows-2 if numRows > 1 else 1)
                print(i,c,offset)
                try:
                    result += s[i + offset]
                except IndexError:
                    continue
                if i == 0 or i == numRows-1:
                    continue
                try:
                    result += s[2*numRows - 2 - i + offset]
                except IndexError:
                    pass
        return result
        
S = Solution()
print(S.convert("PAYPALISHIRING", 3))
print(S.convert("PAYPALISHIRING", 4))
print(S.convert("PA", 1))
