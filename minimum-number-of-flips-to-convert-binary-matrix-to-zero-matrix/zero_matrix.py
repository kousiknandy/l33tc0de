def flatten(mat):
    r = len(mat)
    c = len(mat[0])
    s = bytearray()
    for i in range(r):
        for j in range(c):
            s.append(mat[i][j]+48)
    return s, r, c

def flip(s, r, c, r1, c1):
    if r1 < 0 or r1 > r-1:
        return
    if c1 < 0 or c1 > c-1:
        return
    o = c*r1+c1
    try:
        if s[o] == 48:
            s[o] = 49
        else:
            s[o] = 48
    except:
        pass
    #print(s.decode(), r1, c1)

def flip_neighbours(s, r, c, r1, c1):
    flip(s, r, c, r1, c1)
    flip(s, r, c, r1+1, c1)
    flip(s, r, c, r1-1, c1)
    flip(s, r, c, r1, c1+1)
    flip(s, r, c, r1, c1-1)

def neighbours(s, r, c):
    for i in range(r):
        for j in range(c):
            t = bytearray(s)
            flip_neighbours(t, r, c, i, j)
            yield t

def bfs(s, r, c):
    d = 1
    if s.decode() == "0"*r*c:
        return 0
    q = [(x,d) for x in neighbours(s, r, c)]
    v = [x[0].decode() for x in q]
    #print(q, v)
    while len(q):
        i, d = q.pop(0)
        if i.decode() not in v:
            v.append(i.decode())
        for j in neighbours(i, r, c):
            if j.decode() not in v:
                if (j,d+1) not in q:
                    q.append((j, d+1))
        if i.decode() == "0"*r*c:
            return d
    return -1
        
if __name__ == "__main__":
    s, r, c = flatten([[0], [1], [1]])
    print(s, r, c)
    q = bytearray(s)
    flip_neighbours(q, r, c, 0, 0)
    print(q)
    p = bfs(s, r, c)
    print(p)
    s, r, c = flatten([[1,1,1],[1,0,1],[0,0,0]])
    print(s, r, c)
    # q = bytearray(s)
    # flip_neighbours(q, r, c, 0, 2)
    # print(q)
    # q = bytearray(s)
    # flip_neighbours(q, r, c, 1, 0)
    # print(q)
    p = bfs(s, r, c)
    print(p)
    s, r, c = flatten([[0,0,0],[0,0,0],[0,0,0]])
    print(s, r, c)
    p = bfs(s, r, c)
    print(p)
    s, r, c = flatten([[1,1],[1,0]])
    print(s, r, c)
    p = bfs(s, r, c)
    print(p)
    s, r, c = flatten([[0]])
    print(s, r, c)
    p = bfs(s, r, c)
    print(p)
    s, r, c = flatten([[1,0,1],[1,0,1],[0,0,0]])
    print(s, r, c)
    p = bfs(s, r, c)
    print(p)
    s, r, c = flatten([[1,0,0],[1,0,0]])
    print(s, r, c)
    p = bfs(s, r, c)
    print(p)
