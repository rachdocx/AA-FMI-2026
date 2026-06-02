def orientare(p1, p2, p3):
    return (p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]) - (p1[1] * p2[0] + p2[1] * p3[0] + p3[1] * p1[0])

def segment(p1, p2, p):
    if orientare(p1, p2, p) != 0:
        return False
    elif min(p1[0], p2[0]) <= p[0] <= max(p1[0], p2[0]) and min(p1[1], p2[1]) <= p[1] <= max(p1[1], p2[1]):
        return True

n = int(input())
puncte = []
for _ in range(n):
    x, y = map(int, input().split())
    puncte.append((x, y))
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    q = (x, y)

    pe_margine = False
    intersectii = 0
    for i in range(n):
        p1 = puncte[i]
        p2 = puncte[(i + 1) % n]
        if segment(p1, p2, q):
            pe_margine = True
            break

        if (p1[1] > q[1]) != (p2[1] > q[1]):
            conditie_y = True
        else:
            conditie_y = False

        if conditie_y:
            if p1[1] < p2[1]:
                if orientare(p1, p2, q) > 0:
                    intersectii += 1
            else:
                if orientare(p2, p1, q) > 0:
                    intersectii += 1

    if pe_margine:
        print("BOUNDARY")
    elif intersectii % 2 == 1:
        print("INSIDE")
    else:
        print("OUTSIDE")