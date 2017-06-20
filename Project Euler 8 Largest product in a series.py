t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    temp = [int(d) for d in num ]
    prodlist = []
    for i in range(n-k):
        mul = 1
        for j in range(i, i+k):
            mul *= temp[j]
        prodlist.append(mul)
    print(max(prodlist))