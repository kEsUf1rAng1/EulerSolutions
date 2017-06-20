t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    maxa = int(n/3)
    maxmul = -1
    if n % 2 == 0:
        for a in range(3,maxa):
            b = int((n * (n - 2*a)) / (2 * (n - a)))
            c = n - a - b
            if a * a + b * b == c * c and b > 0 and c > 0 and a*b*c > maxmul:
                maxmul = a*b*c
    print(maxmul)