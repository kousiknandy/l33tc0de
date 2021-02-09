from collections import deque 

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        solution = deque()
        if (numerator < 0 and denominator > 0) or \
           (numerator > 0 and denominator < 0):
            solution.append("-")
        numerator = abs(numerator)
        denominator = abs(denominator)
        integer_part = numerator // denominator
        solution.extend(str(integer_part))
        rem = numerator % denominator
        decimal_place = len(solution)
        if rem:
            solution.append(".")
            decimal_place += 1
        memo = dict()
        while rem:
            if rem in memo:
                solution.insert(memo[rem],"(")
                solution.append(")")
                break
            memo[rem] = decimal_place
            rem *= 10
            nextdigit = rem // denominator
            rem = rem % denominator
            solution.append(str(nextdigit))
            decimal_place += 1
        return "".join(solution)

S = Solution()
print(S.fractionToDecimal(29, 4))
print(S.fractionToDecimal(29, 7))
print(S.fractionToDecimal(700, 3))
print(S.fractionToDecimal(-50, 8))

