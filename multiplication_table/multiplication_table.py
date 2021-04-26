def table(n):
    mx = len(str(n*n))
    for i in range(1,n+1):
        for j in range(1,n+1):
            print("{product:{width}}".format(product=i*j, width=mx), end=" ")
        print()

table(5)
table(15)
table(70)

