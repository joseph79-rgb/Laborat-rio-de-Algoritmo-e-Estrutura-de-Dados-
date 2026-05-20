#O maior numero impar

import random
k = int(input("Digite o tamanho do seu vetor:"))
v = []
for _ in range(k):
    v.append(random.randint(0,100))
print(v)

maior = None
for numero in v:
    if numero % 2 != 0:
        maior = numero
        break
for i in range(len(v)):
    if v[i] % 2 != 0 and v[i] > maior:
        maior = v[i]
print(f"O maior eh {maior}")

