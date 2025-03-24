class Solution:
    def reverseWords(self, s: str) -> str:
        def rev(s, b=0, e=None):
            if e is None: e = len(s)-1
            i, j = b, e
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        def compress(s):
            i, j = 0, 0
            sp = True
            while j < len(s):
                if s[j] != " ":
                    s[i] = s[j]
                    i += 1
                    j += 1
                    sp = False
                else:
                    if not sp: 
                        s[i] = " "
                        i += 1
                    sp = True
                    j += 1
            for j in range(len(s)-i): del s[-1]
            if s[-1] == " ": del s[-1]

        s = list(s)
        rev(s)
        # print(s)
        compress(s)
        # print(s)
        i, j = 0, 0
        while j < len(s):
            while s[j] != " ": 
                j += 1
                if j == len(s): break
            rev(s, i, j-1)
            # print(i, j, s)
            i = j+1
            j += 1
        return "".join(s)
