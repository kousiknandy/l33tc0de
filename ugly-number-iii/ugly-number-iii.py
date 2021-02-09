from functools import reduce

def Gcd(a: int, b:int) -> int:
    while a:
        a, b = b % a, a
    return b

def Lcm(a: int, b: int) -> int:
    return (a * b) // Gcd(a, b)

def count2lcm(Z: int, a: int, b: int, c:int,
             ab: int, bc: int, ca: int,
             abc: int) -> int:
    return Z//a + Z//b + Z//c - \
        (Z//ab + Z//bc + Z//ca) + \
        Z//abc

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        ab = Lcm(a, b)
        bc = Lcm(b, c)
        ca = Lcm(a, c)
        abc = reduce(Lcm, [a, b, c])
        # Z/a + Z/b + Z/c - (Z/ab + Z/bc + Z/ca) + Z/abc = n
        n1 = count2lcm(abc, a, b, c, ab, bc, ca, abc)
        #l1 = list(filter(lambda x: x%a == 0 or x%b == 0 or x%c ==0, [x for x in range(2,abc+1)]))
        #print(n1)#, len(l1), l1)
        n2 = n // n1
        n3 = n % n1
        start = n2 * abc 
        end = (n2 + 1) * abc
        while start < end:
            mid = start + (end -start) // 2
            print(start, end)
            if count2lcm(mid, a, b, c, ab, bc, ca, abc) < n:
                start = mid + 1
            else:
                end = mid
        return start

# print(Gcd(12, 18))
# print(Gcd(15, 5))
# print(Gcd(13, 17))
# print(Lcm(6, 8))
# print(Lcm(5, 15))
# print(Lcm(13, 19))
# print(reduce(Lcm, [4, 6, 10]))
# print(reduce(Lcm, [4, 5, 10]))
#print(reduce(Lcm, [2,217983653,336916467]))

S = Solution()
print(S.nthUglyNumber(25, 4, 6, 10))
print(S.nthUglyNumber(1000000000,2,217983653,336916467))
print(S.nthUglyNumber(6,2,1,3))
