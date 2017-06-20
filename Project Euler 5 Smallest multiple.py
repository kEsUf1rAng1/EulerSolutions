t = int(input().strip())


def maxpower(p, n):
    t = int(n / p)
    for i in range(1, t + 2):
        if p ** i > n:
            return p ** (i - 1)
        elif p ** i == n:
            return p ** i
    return p


def isprime(num):
    i = 2

    if num == 1:
        return False

    while i * i <= num:
        if num % i == 0:
            return False
        else:
            i += 1
    return True


for a0 in range(t):
    n = int(input().strip())
    if n == 0:
        mul = 0
    else:
        mul = 1

    for i in range(1, n + 1):
        if i <= n and isprime(i):
            mul = mul * maxpower(i, n)
        if i > n:
            break
    print(mul)
