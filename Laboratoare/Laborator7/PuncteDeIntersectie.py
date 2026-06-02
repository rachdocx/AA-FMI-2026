def bs(v, x):
    st = 0
    dr = len(v)
    while st < dr:
        mid = (st + dr) // 2
        if v[mid] < x:
            st = mid + 1
        else:
            dr = mid
    return st

n = int(input())
segmente = []

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    if y1 == y2:
        if x1 > x2:
            x1, x2 = x2, x1
        segmente.append((x1, 1, y1))
        segmente.append((x2, 3, y1))
    else:
        if y1 > y2:
            y1, y2 = y2, y1
        segmente.append((x1, 2, y1, y2))

segmente.sort()

segmente_actuale = []
intersectii = 0

for s in segmente:
    tip = s[1]
    if tip == 1:
        y = s[2]    #inaltime segment orizontal
        poz = bs(segmente_actuale, y)   #il bagam in locul in care seg actuale ramane ordonat
        segmente_actuale.insert(poz, y)
    elif tip == 3:
        y = s[2]
        poz = bs(segmente_actuale, y)
        if poz < len(segmente_actuale) and segmente_actuale[poz] == y:  #cautam batul care s a terminat si il scoatem
            segmente_actuale.pop(poz)
    else:
        jos = s[2]
        sus = s[3]
        ijos = bs(segmente_actuale, jos)   #cu binary search cautam unde apare un bat vertical si fiind sortat pozitia
        isus = bs(segmente_actuale, sus)   #din vector ne da chiar cate intersecteaza
        intersectii += (isus - ijos)
print(intersectii)