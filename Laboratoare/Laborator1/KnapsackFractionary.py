n, C = map(int, input().split())
S = 0.0
valori = list(map(int, input().split()))
greutati = list(map(int, input().split()))

unitate = []

for i in range(n):
    unitate.append((valori[i] / greutati[i], valori[i], greutati[i]))

unitate.sort(reverse=True)

for i in range(n):
    if unitate[i][2] <= C:
        S += unitate[i][1]
        C -= unitate[i][2]
    else:
        S += unitate[i][1] * (C / unitate[i][2])
        C = 0;
        break;

print(S)

