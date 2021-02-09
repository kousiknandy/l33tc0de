class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        buf = ""
        sz  = 0
        mult = 1
        for x in S:
            if x >= "a" and x <= "z":
                if mult > 1:
                    print(" ", buf, sz, mult, K%len(buf))
                    newsz = sz * mult
                    if newsz >= K:
                        return buf[(K-1) % len(buf)]
                    buf = buf * mult
                    mult = 1
                    sz = newsz
                buf += x
                sz  += 1
                print("  ", buf, sz, mult, K%len(buf))
                if sz >= K:
                    return buf[K-1]
                continue
            if x >= "0" and x <= "9":
                mult *= int(x)
        else:
            print(buf, mult, K%len(buf))
            if mult > 1:
                newsz = sz * mult
                if newsz >= K:
                    return buf[(K-1) % len(buf)]
            
S = Solution()
print(S.decodeAtIndex(S = "leet2code3", K = 10)) #o
print(S.decodeAtIndex(S = "ha22", K = 5)) #h
print(S.decodeAtIndex(S = "a2345678999999999999999", K = 1))   #a
print(S.decodeAtIndex("a2b3c4d5e6f7g8h9", 9)) #b
