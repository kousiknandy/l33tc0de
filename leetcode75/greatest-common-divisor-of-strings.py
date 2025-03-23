class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        pref = ""
        ans = ""
        l = 0
        while True:
            if str1[l] != str2[l]: break
            pref += str1[l]
            l += 1
            if len(str1) % l == 0 and len(str2) % l == 0:
                b = len(str1) // l
                d1 = False
                # print("\n1:", pref, b,l)
                for i in range(b):
                    # print(str1[i*l:i*l+l], end=" ")
                    if pref != str1[i*l:i*l+l]: break
                else:
                    d1 = True
                    b = len(str2) // l
                    d2 = False
                    # print("\n2:", b,l)
                    for i in range(b):
                        # print(str1[i*l:i*l+l], end=" ")
                        if pref != str2[i*l:i*l+l]: break
                    else:
                        ans = pref
            if l >= len(str1) or l >= len(str2): break
        return ans
