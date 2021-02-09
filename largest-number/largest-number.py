from typing import List

def pad(func):
    def wrapper(self, other):
        if len(self.n) < len(other.n):
            pad = self.n[-1]
            l = len(other.n) - len(self.n)
            left = self.n + pad * l
            right = other.n
        elif len(self.n) > len(other.n):
            pad = other.n[-1]
            l = len(self.n) - len(other.n)
            left = self.n
            right = other.n + pad * l
        else:
            left = self.n
            right = other.n
        return func(left, right)
    return wrapper

class Numb:
    def __init__(self, n):
        self.n = str(n)

    def __eq__(self, other):
        return self.n == other.n

    #@pad
    def __lt__(left, right):
        #return left < right
        return int(left.n + right.n) < int(right.n + left.n)

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted(nums, reverse=True, key=lambda x: Numb(x))
        print(nums)
        return "".join([str(x) for x in nums])

n1 = Numb(3)
n2 = Numb(34)
n3 = Numb(31)
print(n1 < n2)
print(n1 < n3)
print(n3 < n2)

    
S = Solution()
print(S.largestNumber([3,30,34,5,9]))
print(S.largestNumber([3,300,340,304,30]))
print(S.largestNumber([21,2]))
print(S.largestNumber([111311, 1113]))
print(S.largestNumber([1, 10, 100, 1000]))

