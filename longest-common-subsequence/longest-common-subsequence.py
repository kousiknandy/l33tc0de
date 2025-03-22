class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0]* m for _ in range(n)]
        subseq = 0
        for diag in range(m+n-1):
            r = min(diag, n-1)
            c = diag - r
            l = min(diag+1, min(m,n))
            for i in range(l):
                # print(r,c, text2[r], text1[c], end=", ")
                if text2[r] == text1[c]:
                    if r == 0 or c == 0: dp[r][c] = 1
                    else: dp[r][c] = dp[r-1][c-1] + 1
                else:
                    lf = dp[r][c-1] if c>0 else 0
                    tp = dp[r-1][c] if r>0 else 0
                    dp[r][c] = max(lf,tp)
                subseq = max(subseq, dp[r][c])
                r -= 1
                c += 1
                if c > m-1: break
        return subseq
