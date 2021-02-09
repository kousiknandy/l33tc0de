T = int(input())
for testcase in range(1,T+1):
    N, B = map(int, input().split())
    A = list(map(int, input().split()))
    A = sorted(A)
    count = 0
    for a in A:
        if B >= a:
            count += 1
            B -= a
        else:
            break
    print("Case #{}: {}".format(testcase, count))
