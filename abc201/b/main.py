N = int(input())
data = []
for i in range(N):
    S, T = map(str, input().split())
    T = int(T)
    data.append([T, S])
data.sort(reverse=True)
print(data[1][1])
