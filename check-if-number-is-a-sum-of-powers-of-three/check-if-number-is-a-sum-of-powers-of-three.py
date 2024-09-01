class Solution:
    def next3(self, n, m):
        if n in [0, 1]: return True
        if m == 0: return False
        if n in [3]: return True
        if n in [2]: return False
        k = 1
        while 3**k <= n: k += 1
        k -= 1
        if k > m: return False
        # print(k, end=" ")
        return self.next3(n - 3**k, k-1)

    def checkPowersOfThree(self, n: int) -> bool:
        return self.next3(n, 100)
