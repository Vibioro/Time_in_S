D = int(input("Введите секунды: "))

L = 0
X = 0
C = D
V = D // 60

while C >= 60:
    C -= 60

if V >= 60:
    while V >= 60:
        V -= 60
        X += 1
    if X >= 24:
        while X >= 24:
            X -= 24
            L += 1

print(f"{L}:{X}:{V}:{C}")
