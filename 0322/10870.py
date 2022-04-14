n = int(input())
sugar = [-1] * 5002
sugar[3], sugar[5] = 1, 1

for i in range(6, n+1):
    if sugar[i-3] < 0 and sugar[i-5] > 0:
        sugar[i] = sugar[i-5] + 1
    elif sugar[i-3] > 0 and sugar[i-5] < 0:
        sugar[i] = sugar[i-3] + 1
    elif sugar[i-3] < 0 and sugar[i-5] < 0:
        sugar[i] = -1
    else:
        sugar[i] = min(sugar[i-5], sugar[i-3]) + 1

for i in range(n):
    print(i, " ", sugar[i])