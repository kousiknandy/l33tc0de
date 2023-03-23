class Solution:
    def base_repr(self, n, b):
        digits = []
        if n == 0: return [0]
        i = 1
        while n > 0:
            n, d = divmod(n, b**i)
            digits.append(d)
            i += 1
        return digits

    def is_palindrome(self, arr):
        l = len(arr)
        for i in range(l//2):
            if arr[i] != arr[l-i-1]: return False
        return True

    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2,n-1):
            if not self.is_palindrome(self.base_repr(n, i)): return False
        return True
