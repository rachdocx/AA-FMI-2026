def test_orientare(p1, p2, p3):
    return (p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]) - (p1[1] * p2[0] + p2[1] * p3[0] + p3[1] * p1[0])


n = int(input())
puncte = []
for _ in range(n):
    a, b = map(int, input().strip().split())
    puncte.append((a, b))
#punctul asta e sigur in acoperirea convexa, punctul cel mai din stanga jos
minI = 0
for i in range(1, n):
    if puncte[i][1] < puncte[minI][1] or (puncte[i][1] == puncte[minI][1] and puncte[i][0] < puncte[minI][0]):
        minI = i

puncte = puncte[minI:] + puncte[:minI]
puncte.append(puncte[0])

l = [puncte[0], puncte[1]]
for i in range(2, len(puncte)):
    l.append(puncte[i])
    while len(l) > 2 and test_orientare(l[-3], l[-2], l[-1]) <= 0:
        l.pop(-2)
l.pop()

print(len(l))
for p in l:
    print(f"{p[0]} {p[1]}")