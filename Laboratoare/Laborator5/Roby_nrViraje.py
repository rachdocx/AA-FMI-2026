n = int(input())

puncte = []
for _  in range(n):
    a, b = map(int, input().strip().split())
    puncte.append((a, b))

left = 0
right = 0
touch = 0

for i in range(1, n - 1):

    lst = puncte[i - 1]
    now = puncte[i]
    nxt = puncte[i + 1]           #det(last, now, next)
                                            # 1 1 1
    det = (lst[0] * now[1] + now[0] * nxt[1] +nxt[0] * lst[1]) -(lst[1] * now[0] + now[1] * nxt[0] + nxt[1] * lst[0])

    if det > 0:
        left += 1
    elif det < 0:
        right += 1
    else:
        touch +=1

lst = puncte[n - 2]
now = puncte[n - 1]
nxt = puncte[0]

det = (lst[0] * now[1] + now[0] * nxt[1] + nxt[0] * lst[1]) - (lst[1] * now[0] + now[1] * nxt[0] + nxt[1] * lst[0])

if det > 0:
    left += 1
elif det < 0:
    right += 1
else:
    touch += 1

print(f"{left} {right} {touch}")



