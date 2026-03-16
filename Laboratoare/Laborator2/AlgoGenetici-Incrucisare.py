n = int(input())

C1 = input().strip()
C2 = input().strip()

i = int(input())
C1prime = C1[:i] + C2[i:]
C2prime = C2[:i] + C1[i:]

print(C1prime)
print(C2prime)
