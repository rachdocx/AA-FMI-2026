a, b = map(int, input().split())

n = int(input())

intervale = [] * (n + 1)

for i in range(n):
    x = list(map(int, input().split()))
    intervale.append((x[0], x[1]))

intervale.sort(key = lambda intervale: intervale[1])
print(intervale)