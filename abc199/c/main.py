N = int(input())
S = input()
Q = int(input())
T = []
A = []
B = []
for i in range(Q):
    t, a, b = map(int, input().split())
    T.append(t)
    A.append(a)
    B.append(b)

Sl = list(S)
left = Sl[:N]
right = Sl[N:]

for i in range(Q):
    if T[i] == 1:
        left[A[i] - 1], right[B[i] - 1 - N] = right[B[i] - 1 - N], left[A[i] - 1]
    elif T[i] == 2:
        left, right = right, left
        print(left)
        print(right)
Sl = left + right
answer = "".join(Sl)
print(answer)
