H, W, X, Y = map(int, input().split())
S = []
for i in range(H):
    s = input()
    S.append(s)

count = 0
xp = X
xm = X
for i in range(W):
    print("xp=", xp, "y=", Y)
    print(S[xp - 1][Y - 1])
    if xp - 1 <= W:
        if S[xp - 1][Y - 1] == ".":
            print()
            xp = X + 1
            count += 1
        else:
            break
for i in range(W):
    if xm - 1 > 0:
        if S[xm - 1][Y - 1] == ".":
            xm = X - 1
            count += 1
        else:
            break
yp = Y
ym = Y
for i in range(H):
    if yp - 1 <= H:
        if S[X - 1][yp - 1] == ".":
            yp = Y + 1
            count += 1
        else:
            break
for i in range(H):
    if ym - 1 > 0:
        if S[X - 1][ym - 1] == ".":
            ym = Y - 1
            count += 1
        else:
            break
print(count)