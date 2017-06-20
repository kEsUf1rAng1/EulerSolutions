import math

def findprime(n, lst):
    x=lst[len(lst)-1]
    while len(lst)<n:
        x += 2
        y = math.floor(x**0.5)
        isPrime = True
        for i in lst:
            if i>y:
                isPrime = True
                break
            if x%i==0:
                isPrime = False
                break
        if isPrime:
            lst.append(x)
    return lst


t=int(input())
lst=[2,3]
for i in range(t):
    n=int(input())
    if len(lst)<n:
        lst = findprime(n,lst)
    print(lst[n-1])