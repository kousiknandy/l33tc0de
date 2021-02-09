class Solution:    
    def checkwithStack(self, s, stack, lazy = True):
        if len(s) == 0 and len(stack) == 0: return True
        #print(s, stack)
        for i, c in enumerate(s):
            if c == "(":
                stack.append(c)
                continue
            if c == ")":
                try:
                    t = stack.pop()
                except IndexError:
                    return False
                if t == "(":
                    continue
                if t == "*":
                    r1 = r2 = r3 = False
                    s1 = stack[:]
                    r1 = self.checkwithStack(s[i:], s1, lazy)
                    if not r1:
                        s1 = stack[:]
                        s1.append("(")
                        r2 = self.checkwithStack(s[i:], s1, lazy)
                    if not r1 and not r2:
                        s1 = stack[:]
                        s1.append(")")
                        r3 = self.checkwithStack(s[i:], s1, lazy)
                    return r1 or r2 or r3
                if t == ")":
                    stack.append(")")
                    stack.append(")")
                    continue
            if c == "*":
                if lazy:
                    stack.append(c)
                    continue
                else:
                    r1 = r2 = r3 = False
                    s1 = stack[:]
                    s1.append("(")
                    r1 = self.checkwithStack(s[i+1:], s1, lazy)
                    if not r1:
                        s1 = stack[:]
                        r2 = self.checkwithStack(s[i+1:], s1, lazy)
                    if not r1 and not r2:
                        s1 = stack[:]
                        r3 = self.checkwithStack(")" + s[i+1:], s1, lazy)
                    return r1 or r2 or r3
        if lazy:
            s1 = "".join(stack)
            return self.checkwithStack(s1, [], False)
        return len(stack) == 0
                
    def checkValidString(self, s: str) -> bool:
        stack = []
        if len(s) == 0: return True
        if s[0] == ")": return False
        return self.checkwithStack(s, stack)

S = Solution()

print(S.checkValidString("((()()))"))  # true
print(S.checkValidString("((()()))(")) # false
print(S.checkValidString("((()())))")) # false
print(S.checkValidString("(((())))"))  # true
print(S.checkValidString("("))         # false
print(S.checkValidString(")"))         # false

print(S.checkValidString("(*)"))       # true
print(S.checkValidString("*)"))        # true
print(S.checkValidString("**)"))       # true
print(S.checkValidString("(*"))        # true
print(S.checkValidString("(****"))     # true
print(S.checkValidString("(*()"))      # true
print(S.checkValidString("((*")) # false
print(S.checkValidString("((()())((()))(*")) # false
print(S.checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*")) # false
print(S.checkValidString("((*")) # false

print(S.checkValidString("((*)"))        # true
print(S.checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))
