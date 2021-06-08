N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    if A[i] <= 10:
        A[i] = 0
    elif A[i] > 10:
        A[i] = A[i] - 10

answer = 0
for i in A:
    answer += i

print(answer)