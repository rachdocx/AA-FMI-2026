l, k = map(int, input().split())

C = list(input().strip())

bits = map(int, input().split())
for bit in bits:
    if C[bit] == "0":
        C[bit] = "1"
    elif C[bit] == "1":
        C[bit] = "0"

print("".join(C))
