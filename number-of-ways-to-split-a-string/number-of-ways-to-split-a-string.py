class Solution:
    def numWays(self, s: str) -> int:
        l = len(s)
        c1 = 0
        for c in s:
            if c == '1': c1 += 1
        if c1 % 3: return 0
        begin1 = 0
        begin2 = 0
        b1     = 0
        end1   = 0
        end2   = 0
        if c1:
            for i,c in enumerate(s):
                if c == '1':
                    b1 += 1
                    if b1 == c1 // 3:
                        begin1 = i
                    if b1 == (c1 // 3) + 1:
                        begin2 = i
                    if b1 == 2 * c1 // 3:
                        end1 = i
                    if b1 == (2 * c1 // 3) + 1:
                        end2 = i
                        break
            #print(c1, begin1, begin2, end1, end2)
            return ((begin2 - begin1) * (end2 - end1)) % (10**9+7)
        return ((l - 1) * (l -2) // 2) % (10**9+7)
    
S = Solution()
print(S.numWays("10101"))
