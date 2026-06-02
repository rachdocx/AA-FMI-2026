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
    q =(x, y)
    if segment(puncte[0], puncte[1], q) or segment(puncte[0], puncte[-1], q):
        print("BOUNDARY")
        continue
    if orientare(puncte[0], puncte[1], q) < 0 or orientare(puncte[0], puncte[-1], q) > 0:
        print("OUTSIDE")
        continue

    st = 1
    dr = n-1
    while dr > st + 1:
        mid = (st + dr)//2
        if orientare(puncte[0], puncte[mid], q) >= 0:
            st = mid
        else:
            dr = mid

    if segment(puncte[st], puncte[dr], q):
        print("BOUNDARY")
    elif orientare(puncte[st], puncte[dr], q) > 0:
        print("INSIDE")
    else:
        print("OUTSIDE")


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
    q =(x, y)
    if segment(puncte[0], puncte[1], q) or segment(puncte[0], puncte[-1], q):
        print("BOUNDARY")
        continue
    if orientare(puncte[0], puncte[1], q) < 0 or orientare(puncte[0], puncte[-1], q) > 0:
        print("OUTSIDE")
        continue

    st = 1
    dr = n-1
    while dr > st + 1:
        mid = (st + dr)//2
        if orientare(puncte[0], puncte[mid], q) >= 0:
            st = mid
        else:
            dr = mid

    if segment(puncte[st], puncte[dr], q):
        print("BOUNDARY")
    elif orientare(puncte[st], puncte[dr], q) > 0:
        print("INSIDE")
    else:
        print("OUTSIDE")