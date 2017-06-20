n = int(input())
for _ in range(n):
    num = int(input())
    if num % 3 == 0:
        mul3 = int(num/3) - 1
    else:
        mul3 = int(num/3)

    if num % 5 == 0:
        mul5 = int(num/5) - 1
    else:
        mul5 = int(num/5)

    if num % 15 == 0:
        mul15 = int(num/15) - 1
    else:
        mul15 = int(num/15)

    sum3 = 3 * mul3 * (mul3 + 1)
    sum5 = 5 * mul5 * (mul5 + 1)
    sum15 = 15 * mul15 * (mul15 + 1)
    finalsum = (sum3 >> 1) + (sum5  >> 1) - (sum15  >> 1)
    print(int(finalsum))