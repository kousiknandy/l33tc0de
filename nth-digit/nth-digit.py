class Solution:
    def nDigit(self, num, i, pos):
        #print(num, i, pos)
        for j in range(i):
            d = num % 10 
            num = num // 10
            if j == (i - pos - 1):
                break
        return d
        
    def findNthDigit(self, n: int) -> int:
        digits = 0
        i = 1
        len = 9
        while True:
            new_digits = digits + (i * len)
            if new_digits >= n:
                break
            len = len * 10
            i = i + 1
            digits = new_digits
            #print(new_digits)
        left = n - digits
        numbers = ((left -1) // i) + 1
        pos = (left - 1) % i
        if i == 1:
            num = numbers
        else:
            num = 10 ** (i-1) + (numbers - 1 )
        print(" ", numbers, i, pos, num)
        d = self.nDigit(num, i, pos)
        return d

S = Solution()

#print(S.nDigit(10 ** 1 + 15 - 1, 2, 1))
#print(S.nDigit(10 ** 3 + 15 - 1, 4, 2))
#print(S.nDigit(10 ** 5 + 1200 - 1, 6, 5))

print(S.findNthDigit(5))
print(S.findNthDigit(9))
print(S.findNthDigit(10))
print(S.findNthDigit(11))
print(S.findNthDigit(1000))
#print(S.findNthDigit(900))
#print(S.findNthDigit(5000))
#print(S.findNthDigit(200000))
