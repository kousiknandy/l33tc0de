from collections import defaultdict 

def diffs(a, b):
    d = 0
    for i in range(len(a)):
        if a[i] != b[i]: d += 1
    return d == 1
    
class SolutionFound(Exception):
    pass
    
def dfs(n, m, v, l):
    if n in v: return
    v.append(n)
    if len(v) == l: raise SolutionFound()
    if n not in m: return
    for c in m[n]:
        dfs(c, m, v[:], l)
        
    
def solution(inputArray):
    m = defaultdict(list)
    for i in range(len(inputArray)):
        for j in range(i, len(inputArray)):
            if diffs(inputArray[i], inputArray[j]):
                m[i].append(j)
                m[j].append(i)                
    l = len(inputArray)
    try:
        for n in m:
            dfs(n,m,[],l)
    except:
        return True
    return False
    
