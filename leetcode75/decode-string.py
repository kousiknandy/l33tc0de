class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        sbuf, nbuf = "", ""
        for c in s:
            # print(stack,sbuf,nbuf)
            if c.isalpha():
                sbuf += c
                continue
            if c.isdecimal():
                if sbuf: 
                    stack.append(sbuf)
                    sbuf = ""
                nbuf += c
            if c == "[":
                n = int(nbuf)
                stack.append(n)
                nbuf = ""
            if c == "]":
                n = stack.pop()
                sbuf = n * sbuf
                if len(stack) >= 1 and isinstance(stack[-1], str):
                    b = stack.pop()
                    sbuf = b + sbuf
        b = stack.pop() if len(stack) >= 1 else ""
        return b + sbuf 
