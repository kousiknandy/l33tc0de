class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        f = lambda x: int((-1+8*x)**0.5/2)
        if finalSum % 2: return []
        fs = finalSum // 2
        n = f(fs)
        if n*(n+1) > 2*fs:
            n -= 1
        res = [2*k for k in range(1, n)]
        res.append(2*fs-n*(n-1))
        return res
