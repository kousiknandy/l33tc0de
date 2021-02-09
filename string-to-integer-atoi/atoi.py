class Solution:
    def myAtoi(self, str):
        val = 0
        sign = 1
        counting = False
        for c in str:
            if c == ' ':
                if not counting:
                    continue
                else:
                    return sign * val
            if c == '-':
                if not counting:
                    sign = -1
                    counting = True
                    continue
                else:
                    return sign * val
            if c == '+':
                if not counting:
                    sign = 1
                    counting = True
                    continue
                else:
                    return sign * val
            if c in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                val = val * 10 + int(c)
                counting = True
                if (sign * val) > (2**31-1):
                    return (2**31-1)
                if (sign * val) < -(2**31):
                    return -(2**31)
                continue
            break
        return sign * val

if __name__ == "__main__":
    S = Solution()
    print(S.myAtoi("20"))
    print(S.myAtoi("5"))
    print(S.myAtoi("20122223343"))
    print(S.myAtoi("-1"))
    print(S.myAtoi("-29129"))
    print(S.myAtoi("-20122223343"))
    print(S.myAtoi("        2013"))
    print(S.myAtoi("2012  "))
    print(S.myAtoi("    2012243  "))
    print(S.myAtoi("2012243 KKKK  "))
    print(S.myAtoi("-2012243XYZ  "))

    
