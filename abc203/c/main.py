N, K = map(int, input().split())
all = []

for i in range(N + 2):
    all.append(0)

for i in range(N):
    A, B = map(int, input().split())
    all.insert(A, all[A - 1] + B)

print(all)

vil = 0
money = K
for i in range(N):
    money -= 1
    money += all[i]
    vil += 1
    if money == 0:
        break
print(vil)