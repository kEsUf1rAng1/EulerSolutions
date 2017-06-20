import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
        else:
            i = i + 1
    print(n)
