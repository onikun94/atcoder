X, N = map(int, input().split())
p = list(map(int, input().split()))
min = 100
data = []
for i in range(102):
    data.append(1)

for i in p:
    data[i] = 0

answer = 0
if N == 0:
    answer = X
else:
    for i in range(102):
        if data[i] != 0:
            if abs(X - i) < min:
                min = abs(X - i)
                answer = i

print(answer)