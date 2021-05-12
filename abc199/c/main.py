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

for i in range(Q):
    if T[i] == 1:
        Sl[A[i] - 1], Sl[B[i] - 1] = Sl[B[i] - 1], Sl[A[i] - 1]
    elif T[i] == 2:
        Sl = Sl[N:] + Sl[:N]
answer = ""
for i in range(len(Sl)):
    answer += Sl[i]
print(answer)
