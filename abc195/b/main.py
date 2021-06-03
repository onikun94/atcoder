import math

A, B, W = map(int, input().split())
W = W * 1000

max = int(math.floor(W / A))
min = int(math.ceil(W / B))

if min > max:
    print("UNSATISFIABLE")
else:
    print(min, max)