def _repeat_sub(m, n):
    i = 1
    p_i = 1
    o_n = n
    o_m = m
    if m < n:
        return 0, m
    while m >= n:
        m = o_m - n
        p_i = i
        i = i + i
        n = n + n
    print(" ", m, i, n)
    ti, tm = _repeat_sub(m, o_n)
    return p_i + ti, tm

_sign = lambda x: x and (-1, 1)[x < 0]

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sig_end = _sign(dividend)
        sig_sor = _sign(divisor)
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        i = 0
        divarr = []
        while True:
            dividend, d = _repeat_sub(dividend, 10)
            divarr.append(d)
            if not dividend:
                break
        divarr = divarr[::-1]
        print(divarr)
        p_div = 0
        while i < len(divarr):
            p_div = p_div * 10 + divarr[i]
            dd, mm = _repeat_sub(p_div, divisor)
            quotient = quotient * 10 + dd
            p_div = mm
            print(i, p_div, quotient)
            i = i + 1
        return sig_end * sig_sor * quotient

print(_repeat_sub(6, 2))
print(_repeat_sub(20, 2))
print(_repeat_sub(17, 3))
print(_repeat_sub(125, 4))

# S = Solution()
# print(S.divide(12334, 5))
# print(S.divide(4, 2))
# print(S.divide(100, 5))
# print(S.divide(89, 17))
