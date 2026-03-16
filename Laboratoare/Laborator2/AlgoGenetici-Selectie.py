a, b, c = map(float, input().split())

n = int(input())

values = list(map(float, input().split()))

def fitness(x):
    return a * x ** 2 + b * x + c

sum = 0

for x in values:
    sum += fitness(x)

fitnesses = []

for x in values:
    fitnesses.append(fitness(x))

sum1 = 0.0
print(f"{sum1:.6f}")
for nota in fitnesses:
    sum1 += nota
    capat = sum1 / sum

    print(f"{capat:.6f}")




