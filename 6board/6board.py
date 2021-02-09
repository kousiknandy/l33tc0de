
def nextMove(current):
    for idx, val in enumerate(current):
        if val == 0:
            pos0 = idx
            break
    #swap with left
    if pos0 in [1, 2, 4, 5]:
        nlist = current.copy()
        nlist[pos0 - 1], nlist[pos0] = nlist[pos0], nlist[pos0 - 1]
        yield nlist
    #swap with right
    if pos0 in [0, 1, 3, 4]:
        nlist = current.copy()
        nlist[pos0 + 1], nlist[pos0] = nlist[pos0], nlist[pos0 + 1]
        yield nlist
    #swap with below
    if pos0 in [0, 1, 2]:
        nlist = current.copy()
        nlist[pos0 + 3], nlist[pos0] = nlist[pos0], nlist[pos0 + 3]
        yield nlist
    #swap with top
    if pos0 in [3, 4, 5]:
        nlist = current.copy()
        nlist[pos0 - 3], nlist[pos0] = nlist[pos0], nlist[pos0 - 3]
        yield nlist



def printNext(current):
    nextq = [(current, 0, 0)]
    index = 0
    for _ in range(72000):
        try:
            now, dep, par = nextq[index]
        except:
            print("Unsolvable", current)
            return -1
        if now == [1, 2, 3, 4, 5, 0]:
            dep3 = dep
            print(dep+1, now)
            while dep:
                now, dep2, par = nextq[par]
                print(dep, now)
                dep -= 1
            return dep3
        for n in nextMove(now):
            for np in nextq:
                if np[0] == n:
                    break
            else:
                #print("enqueing", n, "at", len(nextq))
                nextq.append((n, dep+1, index))
        index += 1

def test(num):
    x = printNext([1, 2, 3, 4, 5, 0])
    print(x, "\n")
    x = printNext([0, 2, 3, 4, 5, 1])
    print(x, "\n")
    x = printNext([1, 2, 3, 4, 0, 5])
    print(x, "\n")
    x = printNext([1, 2, 3, 0, 4, 5])
    print(x, "\n")
    x = printNext([1, 2, 3, 5, 4, 0])
    print(x, "\n")
    x = printNext([3, 0, 2, 1, 5, 4])
    print(x, "\n")
    x = printNext([3, 1, 2, 0, 5, 4])
    print(x, "\n")
    x = printNext([3, 4, 5, 1, 2, 0])
    print(x, "\n")
    x = printNext([3, 4, 5, 0, 1, 2])
    print(x, "\n")

def test2():
    x = printNext([4, 2, 3, 1, 5, 0])
    print(x, "\n")    
    
test(0)
