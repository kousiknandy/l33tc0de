kick = "KICK"
start = "START"
T = int(input())
for t_c in range(1, T+1):
    book = str(input())
    kix = []
    stx = []
    l   = len(book)
    for ix, c in enumerate(book):
        for key, queue in [(kick, kix), (start, stx)]:
            if c == key[0]:
                if ix <= l - len(key):
                    if book[ix:ix+len(key)] == key:
                        queue.append(ix)
    #print(kix, stx)
    k, s = len(kix), len(stx)
    i = j = 0
    count = 0
    for i, k in enumerate(kix):
        while stx[j] < kix[i] + len(kick):
            j += 1
            if j >= len(stx):
                break
        if j >= len(stx):
            break
        count += len(stx) - j
    print("Case #{}: {}".format(t_c, count))
