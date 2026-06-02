def monoton(valori):
    semne = []
    n = len(valori)
    for i in range(n):
        dif = valori[(i + 1) % n] - valori[i]
        if dif > 0:
            semne.append(1)
        elif dif < 0:
            semne.append(-1)
    schimbari = 0
    m = len(semne)
    for i in range(m):
        if semne[i] != semne[(i + 1) % m]:
            schimbari += 1
    if schimbari == 2:
        return True
    else:
        return False

n = int(input())
xs = []
ys = []
for _ in range(n):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

if monoton(xs):
    print("YES")
else:
    print("NO")

if monoton(ys):
    print("YES")
else:
    print("NO")