n = int(input())
st = []
dr = []
jos = []
sus = []
for _ in range(n):
    a, b, c = map(int, input().split())
    if a != 0 and b ==0:      #verticale
        v = -c / a
        if a > 0:
            dr.append(v)    #blocheaza dreapta
        else:
            st.append(v)     #blocheaza stanga
    elif b != 0 and a ==0:      #orizontale
        v = -c / b
        if b > 0:
            sus.append(v)   #blocheaza in sus
        else:
            jos.append(v)   #blocheaza in jos
m = int(input())
for _ in range(m):
    x, y = map(float, input().split())
    valst = -9999999999
    for val in st:
        if val < x and val > valst:
            valst = val
    valdr = 9999999999
    for val in dr:
        if val > x and val < valdr:
            valdr = val
    valjos = -9999999999
    for val in jos:
        if val < y and val > valjos:
            valjos = val
    valsus = 9999999999
    for val in sus:
        if val > y and val < valsus:
            valsus = val
    if valst == -9999999999 or valdr == 9999999999 or valjos == -9999999999 or valsus == 9999999999:
        print("NO")
    else:
        arie = (valdr - valst) * (valsus - valjos)
        print("YES")
        print(arie)