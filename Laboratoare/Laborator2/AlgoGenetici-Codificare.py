a, b = map(float, input().split())

p = int(input())
m = int(input())

l = 0
needed = (b-a) * (10 ** p)
while 1 << l < needed: # logaritmul din enunt
    l += 1

d = (b - a) / (1 << l)

for _ in range(m):
    operatie = input()
    if operatie.lower() == "to":
        x = float(input())
        x = x - a
        x = x / d
        x = int(x)

        if x == 1 << l:
            x -= 1

        sol = format(x, f'0{l}b')
        print(sol)

    elif operatie.lower() == "from":

        bits = input().strip()

        x = int(bits, 2)
        x = a + x * d

        print(x)


