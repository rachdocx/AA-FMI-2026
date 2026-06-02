
n = int(input())
xmin = -9999999999
xmax = 9999999999
ymin = -9999999999
ymax = 9999999999

for _ in range(n):
    a, b, c = map(int, input().split())
    if a != 0:      #verticale
        val = -c / a
        if a > 0:
            if val < xmax:
                xmax = val
        else:
            if val > xmin:
                xmin = val
    elif b != 0:    #orizontale
        val = -c / b
        if b > 0:
            if val < ymax:
                ymax = val
        else:
            if val > ymin:
                ymin = val
if xmin > xmax or ymin > ymax:
    print("VOID")
elif xmin != -9999999999 and xmax != 9999999999 and ymin != -9999999999 and ymax != 9999999999:
    print("BOUNDED")
else:
    print("UNBOUNDED")