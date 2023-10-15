class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        delta = [p[0]-p[1] for p in zip(gas,cost)]
        c, p, s, n = 0, 0, 0, len(gas)
        print(delta)
        for i in range(2*n):
            i %= n
            s += delta[i]
            if s < 0:
                c = p = i+1
                s = 0
                continue
            c += 1
            if c - p == n: break
        else: return -1
        return p 
