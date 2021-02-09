class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        l1 = len(s1)
        l2 = len(s2)
        i = j = 0
        offsetmap = {}
        while True:
            if s1[i % l1] != s2[j % l2]:
                i += 1
                continue
            if j % l2 == 0:
                try:
                    c1 = offsetmap[i % l1]
                    c2 = j
                    r2 = - ( -(n2 * l2) // c2)
                    r1 = i * r2
                    print(" ", r1, r2, c1, c2, offsetmap)
                    return (l1 * n1) // r1
                except KeyError:
                    if j >= l2*n2:
                        print(" ", l1 * n1,  i, offsetmap)
                        return (l1 * n1) // i   # wrong
                    offsetmap[i % l1] = i
            j += 1
            i += 1

S = Solution()
print(S.getMaxRepetitions(s1="acb", n1=4, s2="ab", n2=2)) # 2
print(S.getMaxRepetitions(s1="acb", n1=1, s2="acb", n2=1)) # 1
print(S.getMaxRepetitions(s1="aaa", n1=3, s2="aa", n2=1)) # 4
print(S.getMaxRepetitions("bacaba", 3,"abacab",1)) # 2
