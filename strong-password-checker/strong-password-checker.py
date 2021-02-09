import string

def count_class(s, runs):
        low = up = dig = special = i = j = 0
        insertions = deletions = replacements = 0
        run = 1
        prev = None
        size = len(s)
        exs = ""
        for p, c in enumerate(s):
            if c in string.ascii_lowercase:
                low += 1
            elif c in string.ascii_uppercase:
                up += 1
            elif c in string.digits:
                dig += 1
            else:
                special += 1
            if c == prev:
                run += 1
            else:
                if run >= 3:
                    runs.append((run, prev))
                prev = c
                run = 1
            if p == 19:
                break
        if run >= 3:
            runs.append((run, prev))
        if size > 20:
            exs = s[20:]
        print(s, size, ":", low, up, dig, special, exs, runs)
        return low, up, dig, exs

class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        runs = []
        size = len(s)
        corrections = 0
        rundel = 0
        runins = 0
        low, up, dig, exs = count_class(s, runs)
        for r in runs:
            corrections += r[0] // 3
            changes = r[0] // 3
            runins += r[0] - 1
            for c in range(changes):
                if r[1] in string.ascii_lowercase:
                    if up == 0:
                        up += 1
                    elif dig == 0:
                        dig += 1
                    elif c == 0:
                        rundel = 1
                elif r[1] in string.ascii_uppercase:
                    if low == 0:
                        low += 1
                    elif dig == 0:
                        dig += 1
                    elif c == 0:
                        rundel = 1
                elif r[1] in string.digits:
                    if low == 0:
                        low += 1
                    elif up == 0:
                        up += 1
                    elif c == 0:
                        rundel = 1
        missing = len(list(filter(lambda x: x == 0, [low, up, dig])))
        if size < 6:
            if missing >= (6 - size):
                corrections = missing
            else:
                corrections += 6 - size
        elif size > 20:
            corrections += size - 20
            corrections -= rundel
            if missing:
                runs = []
                if len(exs) > (size - 20):
                    exs = exs[:size - 20]
                l2, u2, d2, e2 = count_class(exs, runs)
                missing = len(list(filter(lambda x: x == 0, [low+l2, up+u2, dig+d2])))    
            corrections += missing
        return corrections
            
S = Solution()
print(S.strongPasswordChecker("QQQQQ"))
print(S.strongPasswordChecker("ABABABABABABABABABAB1"))
print(S.strongPasswordChecker("ABABABABABABABABABABAB3b"))
print(S.strongPasswordChecker(""))
print(S.strongPasswordChecker("aB3"))
print(S.strongPasswordChecker("ababa"))
print(S.strongPasswordChecker("aSddd230"))
print(S.strongPasswordChecker("aaa"))
print(S.strongPasswordChecker("aaabbb"))
print(S.strongPasswordChecker("aSddw"))
print(S.strongPasswordChecker("addddddd230"))
print(S.strongPasswordChecker("435645333"))
print(S.strongPasswordChecker("12345678901234567890AAAAA"))
print(S.strongPasswordChecker("123456789012345678AAAAA"))
print(S.strongPasswordChecker("1234567890123456AAAAA"))
print(S.strongPasswordChecker("1234567890123456AAAAAababababa"))
print(S.strongPasswordChecker("1010101010aaaB10101010"))
print(S.strongPasswordChecker("aaaaaaaaaaaaaaaaaaaaa"))
print(S.strongPasswordChecker("..."))
