def square(n):
    if n == 0: return 0
    if n < 0: n = -n
    return (square(n//2)<<2) + (n&1)*(((n//2)<<2)+1)

print(square(0))
print(square(1))
print(square(2))
print(square(4))
print(square(7))
print(square(100))
print(square(10000))
print(square(100000000))
print(square(-50))
