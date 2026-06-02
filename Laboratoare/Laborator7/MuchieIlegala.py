def poz_cerc(xa, ya, xb, yb, xc, yc, xd, yd):
    valA = (xa ** 2 + ya ** 2) - (xd ** 2 + yd ** 2)
    valB = (xb ** 2 + yb ** 2) - (xd ** 2 + yd ** 2)
    valC = (xc ** 2 + yc ** 2) - (xd ** 2 + yd ** 2)
    det = (
            ((xa - xd) * (yb - yd) * valC
             + (ya - yd) * valB * (xc - xd)
             + valA * (xb - xd) * (yc - yd)) -
            (valA * (yb - yd) * (xc - xd)
             + (xa - xd) * valB * (yc - yd)
             + (ya - yd) * (xb - xd) * valC)
    )
    return det

xa, ya = map(int, input().split())
xb, yb = map(int, input().split())
xc, yc = map(int, input().split())
xd, yd = map(int, input().split())

res = poz_cerc(xa, ya, xb, yb, xc, yc, xd, yd)

if res > 0:
    print("AC: ILLEGAL")
    print("BD: LEGAL")
elif res < 0:
    print("AC: LEGAL")
    print("BD: ILLEGAL")
else:
    print("AC: LEGAL")
    print("BD: LEGAL")