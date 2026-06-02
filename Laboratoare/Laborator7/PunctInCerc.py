def poz_cerc(xa, ya, xb, yb, xc, yc, x, y):
    valA = (xa ** 2 + ya ** 2) - (x ** 2 + y ** 2)
    valB = (xb ** 2 + yb ** 2) - (x ** 2 + y ** 2)
    valC = (xc ** 2 + yc ** 2) - (x ** 2 + y ** 2)
    det = (
            ((xa - x) * (yb - y) * valC
             + (ya - y) * valB * (xc - x)
             + valA * (xb - x) * (yc - y)) -

            (valA * (yb - y) * (xc - x)
             + (xa - x) * valB * (yc - y)
             + (ya - y) * (xb - x) * valC)
    )
    return det

xa, ya = map(int, input().split())
xb, yb = map(int, input().split())
xc, yc = map(int, input().split())
m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    res = poz_cerc(xa, ya, xb, yb, xc, yc,  x, y)
    if res > 0:
        print("INSIDE")
    elif res == 0:
        print("BOUNDARY")
    else:
        print("OUTSIDE")