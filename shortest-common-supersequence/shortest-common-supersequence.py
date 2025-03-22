class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)
        if str1 == str2: return str1
        dp = [[()]* m for _ in range(n)]
        subseq = 0
        matches = ()
        for diag in range(m+n-1):
            r = min(diag, n-1)
            c = diag - r
            l = min(diag+1, min(m,n))
            for i in range(l):
                # print(r,c, text2[r], text1[c], end=", ")
                if str2[r] == str1[c]:
                    if r == 0 or c == 0: dp[r][c] = (str2[r],)
                    else: dp[r][c] = (*dp[r-1][c-1], str2[r])
                else:
                    lf = dp[r][c-1] if c>0 else ()
                    tp = dp[r-1][c] if r>0 else ()
                    dp[r][c] = lf if len(lf) > len(tp) else tp
                if len(dp[r][c]) > subseq:
                    subseq = len(dp[r][c])
                    matches = (r,c)
                r -= 1
                c += 1
                if c > m-1: break
        # print(matches, dp[matches[0]][matches[1]])
        i, j, k = 0, 0, 0
        lcs = dp[matches[0]][matches[1]] if matches else ()
        ans = ""
        while i < m or j < n:
            if k < len(lcs) and str1[i] == lcs[k] and str2[j] == lcs[k]:
                ans += lcs[k]
                i += 1
                j += 1
                k += 1
                continue
            if i < m and (k >= len(lcs) or lcs[k] != str1[i]):
                ans += str1[i]
                i += 1
            if j < n and (k >= len(lcs) or lcs[k] != str2[j]):
                ans += str2[j]
                j += 1
        return ans
