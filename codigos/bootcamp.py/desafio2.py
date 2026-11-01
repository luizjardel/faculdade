n = int(input())
codigos = list(map(int, input().split()))

suspeitos = 0

for codigo in codigos[:n]:
    if codigo <0 or codigo % 7 == 0:
        suspeitos += 1



if suspeitos == 0:
    print("LIBERAR")
elif suspeitos <= 2:
    print("REVISAR")
else:
    print("BLOQUEAR")
