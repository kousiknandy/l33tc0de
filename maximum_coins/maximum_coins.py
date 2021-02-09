T = int(input())
for t_c in range(1, T+1):
    N = int(input())
    cells = [[]] * N 
    for i in range(N):
        cells[i] = [int(x) for x in input().split()]
    maxsum = 0
    for j in range(N):
        dsum = 0
        for k in range(N-j):
            dsum += cells[k][j+k]
            print("[",k,j+k,"]", end=" ")
        if dsum > maxsum:
            maxsum = dsum
        print()
    for i in range(N):
        dsum = 0
        for k in range(N-i):
            dsum += cells[i+k][k]
            print("[",i+k,k,"]", end=" ")
        if dsum > maxsum:
            maxsum = dsum
        print()
    print("Case #{}: {}".format(t_c, maxsum))
