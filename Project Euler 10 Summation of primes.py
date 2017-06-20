a = [0] * 1000001
for i in range(2,1000001):
    if a[i] == 1:
        continue
    for j in range(2*i,1000001,i):
        a[j] = 1

previous = 0
for i in range(2,1000001):
    if a[i] == 0:
        a[i] = i + previous
        previous = a[i]
    else:
        a[i] = previous
for _ in range(int(input())):
    print(a[int(input())])