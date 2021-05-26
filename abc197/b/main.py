H, W, X, Y = map(int, input().split())
S = []
for i in range(H):
    s = input()
    S.append(s)
X = X - 1
Y = Y - 1

curX = X
curY = Y

answer = 0
for i in range(H):
    curX = curX - i
    print("X=", curX, "Y=", curY)
    if curX >= 0:
        if S[curX][Y] == ".":
            answer += 1
        else:
            break

curX = X
for i in range(1, H):
    curX = curX + i
    if curX < W:
        if S[curX][Y] == ".":
            answer += 1
        else:
            break

for i in range(1, W):
    curY = curY - i
    if curY >= 0:
        if S[X][curY] == ".":
            answer += 1
        else:
            break

curY = Y
for i in range(1, W):
    curY = curY + i
    if curY < H:
        if S[X][curY] == ".":
            answer += 1
        else:
            break

print(answer)
