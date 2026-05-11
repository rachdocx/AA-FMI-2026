n = int(input())

for _ in range(n):
    px, py, qx, qy, rx, ry = map(int, input().strip().split())
    det = (px * qy + qx * ry + rx * py) - (py * qx + qy * rx + ry * px)

    if det > 0:
        print("LEFT")
    if det < 0:
        print ("RIGHT")
    if det == 0:
        print("TOUCH")
