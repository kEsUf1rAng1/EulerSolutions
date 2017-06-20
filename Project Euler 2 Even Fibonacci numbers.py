import sys
t = int(input().strip())
for a0 in range(t):
    a = 1
    b = 1
    n = int(input().strip())
    summ = a + b
    finalsum = 0
    while summ < n:
        summ = a + b
        if summ % 2 == 0 and summ < n:
            finalsum = finalsum + summ
        a = b
        b = summ
    print(finalsum)