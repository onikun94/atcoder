N = int(input())
ans = int(N / 100)
if N % 100 == 0:
    print(ans)
else:
    print(ans + 1)