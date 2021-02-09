T = int(input())
for testcase in range(1,T+1):
    N, X = map(int, input().split())
    A = [(-(-int(a)//X), i) for i, a in enumerate(input().split())]
    A = sorted(A)
    print("Case #{}: ".format(testcase), end="")
    for a in A: print(1 + a[1], end=" ")
    print()
