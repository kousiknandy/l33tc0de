from typing import List

class Solution:
    def isAdditiveNumber(self, num: str, adds: List = []) -> bool:
        print(" "*len(adds), adds, num)
        if len(num) == 0:
            if len(adds) < 3: return False
            n_0 = adds[0]
            n_1 = adds[1]
            for i in range(2, len(adds)):
                n_2 = adds[i]
                if n_2 != n_1 + n_0: return False
                n_0, n_1 = n_1, n_2
            return True
        if len(adds) < 2:
            answer = False
            for i in range(1, len(num)+1):
                n_2 = int(num[:i])
                if n_2 and num[0] == "0": continue
                nadds = adds[:]
                nadds.append(n_2)
                answer |= self.isAdditiveNumber(num[i:], nadds)
                if answer: break
            return answer
        n_0 = adds[-2]
        n_1 = adds[-1]
        answer = False
        for i in range(1, len(num)+1):
            n_2 = int(num[:i])
            if n_2 and num[0] == "0": continue
            if n_2 == n_1 + n_0:
                nadds = adds[:]
                nadds.append(n_2)
                answer |= self.isAdditiveNumber(num[i:], nadds)
                if answer: break
        return answer
        

S = Solution()
print(S.isAdditiveNumber("112358"))
print(S.isAdditiveNumber("199100199"))
print(S.isAdditiveNumber("15163147"))
print(S.isAdditiveNumber("1564628364"))
print(S.isAdditiveNumber("156465647"))
print(S.isAdditiveNumber("1564656470"))
print(S.isAdditiveNumber("1023"))
print(S.isAdditiveNumber("100000000000"))
print(S.isAdditiveNumber("10000000110000000"))
print(S.isAdditiveNumber("10000000110000001"))
print(S.isAdditiveNumber("101"))
