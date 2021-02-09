class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0: return 0
        count = 0
        pos   = 1
        while True:
            suffix = 10 ** (pos - 1)
            prefix = n // (10 * suffix)
            digit  = (n // suffix) % 10
            #print(prefix, digit, suffix, n % suffix)
            if digit == 0:
                count += prefix * suffix
            elif digit == 1:
                count += prefix * suffix + 1 + (n % suffix)
            else:
                count += (prefix + 1) * suffix
            pos += 1
            if not prefix: break
        return count

S = Solution()
print(S.countDigitOne(13))
