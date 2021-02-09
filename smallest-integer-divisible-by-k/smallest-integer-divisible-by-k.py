class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        rem_table = set()
        N = 1
        rem = 1
        while True:
            rem %= K
            if not rem: return N
            if rem in rem_table: return -1
            rem_table.add(rem)
            N += 1
            rem *= 10
            rem += 1
            
