with open("input.txt", 'r') as f:
    linii = f.readlines()

dimensiunePopulatie = int(linii[0].strip())
a, b = map(float, linii[1].split())
coeficienti = [float(x) for x in linii[2].split()]
precizie = int(linii[3].strip())
probRecombinare = float(linii[4].strip())
probMutatie = float(linii[5].strip())
nrEtape = int(linii[6].strip())
import random

class Individ:
    def __init__(self, cromozom, x, fitness):
        self.cromozom = cromozom
        self.x = x
        self.fitness = fitness
        self.prob_selectie = 0.0
        self.prob_cumulata = 0.0

class AlgoritmGenetic:
    def __init__(self, dimPop, a, b, coeficienti, precizie):
        self.dimPop = dimPop
        self.a = a
        self.b = b
        self.coeficienti = coeficienti
        self.precizie = precizie
        self.l, self.dist = self.dimensiuneCromozom(self.a, self.b, self.precizie)
        self.populatie = self.generarePopulatie()
        self.probabilitateSelectie()
        self.probabilitatiCumulate()

    def dimensiuneCromozom(self, a, b, p):
        needed = (b - a) * (10 ** p)
        l = 0
        while (1 << l) < needed:
            l += 1
        d = (b - a) / ((1 << l) - 1)
        return l, d

    def decodificare(self, cromozom):
        x = int(cromozom, 2)
        x = self.a + x * self.dist
        return x

    def fitness(self, cromozom):
        numar = self.decodificare(cromozom)
        putere = numar
        res = self.coeficienti[-1]
        n = len(self.coeficienti)
        for i in range(n - 2, -1, -1):
            res += putere * self.coeficienti[i]
            putere = putere * numar
        return res

    def generarePopulatie(self):
        populatie = []
        for _ in range(self.dimPop):
            cromozom = ""
            for _ in range(self.l):
                cromozom = cromozom + (random.choice(["0", "1"]))
            x_val = self.decodificare(cromozom)
            fit_val = self.fitness(cromozom)
            populatie.append(Individ(cromozom, x_val, fit_val))
        return populatie

    def probabilitateSelectie(self):
        suma = 0.0
        for individ in self.populatie:
            suma += individ.fitness

        for individ in self.populatie:
            individ.prob_selectie = individ.fitness / suma


    def probabilitatiCumulate(self):
        suma = 0.0
        for i in range(self.dimPop - 1):
            self.populatie[i].prob_cumulata = suma
            suma += self.populatie[i].prob_selectie
        self.populatie[-1].prob_cumulata = 1

    def procesSelectie(self):
        #TODO DE REZOLVAT!
        u = random.random()

        l = 0
        r = len(self.populatie) - 1

        res = 0
        while l < r:
            mijloc = (l + r) // 2

            if(self.populatie[mijloc].prob_cumulata <= u < self.populatie[mijloc + 1].prob_cumulata):
                res = mijloc
                break

            elif(u < self.populatie[mijloc].prob_cumulata):
                r = mijloc
            else:
                l = mijloc + 1

        return res, u


    def genUrm(self, fisier):
        nextGen = []

        for _ in range(self.dimPop):
            index_individ, u = self.procesSelectie()

            temp = self.populatie[index_individ]

            clona = Individ(temp.cromozom, temp.x, temp.fitness)

            nextGen.append(clona)

            with open(fisier, 'a') as g:
                g.write(f"Pentru u = {u} alegem cromozomul {clona.cromozom} care are numarul {index_individ}\n")

        self.populatie = nextGen

    def selectieRecombinare(self, fisier):

        with open(fisier, 'a') as g:
            g.write(f"\nAcesti Cromozomi participa la selectia care are probabilitatea de recombinare {probRecombinare}: \n")

        partRecomb = []
        for i in range(self.dimPop):
            u = random.random()

            if u <= probRecombinare:
                with open (fisier, 'a') as g:
                    g.write(f"Cromozomul {i} : {self.populatie[i].cromozom} are u = {u} deci PARTICIPA\n")
                partRecomb.append(self.populatie[i])
            else:
                with open (fisier, 'a') as g:
                    g.write(f"Cromozomul {i} : {self.populatie[i].cromozom} are u = {u} deci NU PARTICIPA\n")
        return partRecomb

    #TODO:
    def recombinare(self, fisier):

        de_combinat = self.selectieRecombinare(fisier)

        with open(fisier, 'a') as g:
            g.write("\nRezultate recombinari:\n")

        n = len(de_combinat) // 2

        for i in range(n):
            crom1 = de_combinat[i]
            crom2 = de_combinat[i + n]
            punct_rupere = random.randint(1, self.l - 1)

            crom1prim = crom1.cromozom[:punct_rupere] + crom2.cromozom[punct_rupere:]
            crom2prim = crom2.cromozom[:punct_rupere] + crom1.cromozom[punct_rupere:]

            with open(fisier, 'a') as g:
                g.write(f"Combinam {crom1.cromozom} cu {crom2.cromozom} in punctul {punct_rupere} \n Rezulta: {crom1prim} si {crom2prim}\n")

            crom1.cromozom = crom1prim
            crom2.cromozom = crom2prim








    # def inlocuireCuSelectie(self, fisier):
    #     with open(fisier, 'a') as g:
    #         g.write("\nCromozomi dupa selectie:\n")
    #         nextgen = self.genUrm()
    #         for i in nextgen:
    #             g.write(f"u = {i[1]}, cromozomul {i[0]} : {self.populatie[i[0]].cromozom}\n")
    #             #TODO: TREBUIE INLOCUITA POPULATIA CU NOUA SELECTIE

    def afisareProbablilitateSelectie(self, fisier):
        with open(fisier, 'a') as g:
            g.write("\nProbabilitate Selectie:\n")
            for i in range(self.dimPop):
                g.write(f"Cromozomul {i} are Probabilitatea de Selectie {self.populatie[i].prob_selectie}\n")

    def afisareProbabilitatiCumulative(self, fisier):
        with open(fisier, 'a') as g:
            g.write("\nIntervale Probabilitati Cumulate:\n")
            for i in range(self.dimPop):
                g.write(f"{self.populatie[i].prob_cumulata} \n")

    def afisarePopulatie1(self, fisier):
        with open(fisier, 'a') as g:
            g.write("\nPopulatie la un Moment:\n")
            for i in range(self.dimPop):
                g.write(
                    f"Cromozomul {i}: {self.populatie[i].cromozom}, x = {self.populatie[i].x}, f(x) = {self.populatie[i].fitness} \n")

    def afisarePopulatie(self, fisier):
        with open(fisier, 'w') as g:
            g.write("Populatie Initiala:\n")
            for i in range(self.dimPop):
                g.write(f"Cromozomul {i}: {self.populatie[i].cromozom}, x = {self.populatie[i].x}, f(x) = {self.populatie[i].fitness} \n")



ag = AlgoritmGenetic(dimensiunePopulatie, a, b, coeficienti, precizie)
ag.afisarePopulatie("output.txt")
ag.afisareProbablilitateSelectie("output.txt")
ag.afisareProbabilitatiCumulative("output.txt")
ag.genUrm("output.txt")
ag.afisarePopulatie1("output.txt")
ag.recombinare("output.txt")

# def dimensiuneCromozom(a, b, p):
#     needed = (b - a) * (10 ** p)
#     l = 0
#     while (1 << l) < needed:
#         l += 1
#     d = (b - a) / ((1 << l) - 1)
#     return l, d
#
# def decodificare(cromozom, a, distanta):
#     x = int(cromozom, 2)
#     x = a + x * distanta
#     return x
#
# import random
# def generarePopulatie(dimPop, dimCrom):
#     populatie = []
#     for _ in range(dimPop):
#         cromozom = ""
#         for _ in range(dimCrom):
#             cromozom = cromozom + (random.choice(["0", "1"]))
#         populatie.append(cromozom)
#     return populatie
#
# def fitness(coeficienti, cromozom):
#     numar = decodificare(cromozom, a, dist)
#     putere = numar
#     res = coeficienti[-1]
#     n = len(coeficienti)
#     for i in range(n - 2, -1, -1):
#         res += putere * coeficienti[i]
#         putere = putere * numar
#     return res
#
# def probabilitateSelectie(populatie):
#     suma = sum()

# l, dist = dimensiuneCromozom(a, b, precizie)
#
# populatie = generarePopulatie(dimensiunePopulatie, l)
#
# with open("output.txt", "w") as g:
#     g.write("Populatia Initiala:\n")
#     n = len(populatie)
#     for i in range(n):
#         g.write(f"Cromozomul {i}: {populatie[i]}, x= {decodificare(populatie[i], a, dist)}, f(x) = {fitness(coeficienti, populatie[i])}\n")
#














# print(populatie)
# for i in populatie:
#     print(decodificare(i, a, dist))

# print(dimensiunePopulatie)
# print(a, b)
# print(coeficienti)
# print(precizie)
# print(probRecombinare)
# print(probMutatie)
# print(nrEtape)