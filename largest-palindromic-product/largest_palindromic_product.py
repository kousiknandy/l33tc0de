class Solution:
    def largestPalindrome(self, n: int) -> int:
        maxn = int("9"*n)
        minn = int("1" + "0"*(n-1))
        round_sz  = 200 * n
        iteration = 0
        product   = 0
        while True:
            strt  = maxn - iteration * round_sz
            if strt < minn: break
            for i in range(strt, strt - round_sz, -1):
                if i < minn: break
                for j in range(i, strt - round_sz, -1):
                    if j < minn: break
                    test = i * j
                    r    = test
                    revt = 0
                    while r:
                        revt = revt * 10 + r % 10
                        r //= 10
                    if test == revt:
                        print(test, "=", i, "*", j, "(", product, ")", iteration, round_sz)
                        product = max(product, test)
                        break
            if product:
                return product % 1337
            iteration += 1
        return 0

S = Solution()
for x in range(1, 9):
    print(x, S.largestPalindrome(x))

                    
