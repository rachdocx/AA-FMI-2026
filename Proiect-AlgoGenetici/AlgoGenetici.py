with open("input.txt", 'r') as f:
    linii = f.readlines()

dimensiunePopulatie = int(linii[0].strip())
a, b = map(float, linii[1].split())
coeficienti = [float(x) for x in linii[2].split()]
precizie = int(linii[3].strip())
probRecombinare = float(linii[4].strip())
probMutatie = float(linii[5].strip())
nrEtape = int(linii[6].strip())


def dimensiuneCromozom(a, b, p):
    needed = (b - a) * (10 ** p)
    l = 0
    while (1 << l) < needed:
        l += 1
    d = (b - a) / ((1 << l) - 1)

    return l, d

import random
def generarePopulatie(dimPop, dimCrom):
    populatie = []
    for _ in range(dimPop):
        cromozom = ""
        for _ in range(dimCrom):
            cromozom = cromozom + (random.choice(["0", "1"]))
        populatie.append(cromozom)
    return populatie


dimCrom, l = dimensiuneCromozom(a, b, precizie)

print(generarePopulatie(dimensiunePopulatie, dimCrom))

# print(dimensiunePopulatie)
# print(a, b)
# print(coeficienti)
# print(precizie)
# print(probRecombinare)
# print(probMutatie)
# print(nrEtape)