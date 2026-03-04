n, gmax = map(int, input().split())
v = list(map(int, input().split()))
g = list(map(int, input().split()))

b = [0] * (gmax + 1)

for i in range(n):
    for j in range(gmax, g[i] - 1, -1):
        if b[j - g[i]] + v[i] > b[j]:
            b[j] = b[j - g[i]] + v[i]

print(b[gmax])