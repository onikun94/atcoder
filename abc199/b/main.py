N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

maxA = max(A)
minB = min(B)

if maxA > minB:
    print(0)
else:
    count = 0
    for i in range(maxA, minB + 1):
        count += 1
    print(count)
