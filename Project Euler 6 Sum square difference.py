t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sumofSquares = (2 * n * n * n + 3 * n * n + n)/6
    summ = (n * n + n)/2
    squareOfSum = summ * summ
    diff = squareOfSum - sumofSquares
    print(int(diff))