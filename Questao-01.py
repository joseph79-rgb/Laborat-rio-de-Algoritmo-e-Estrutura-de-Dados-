#O maior numero impar
import random
k = int(input("Digite o tamanho do seu vetor:"))
v = []
for _ in range(k):
    v.append(random.randint(0,100))
if k <= 0:
	print("Insira um tamanho valido.")
else:
	print(v)
	maior = None
	for numero in v:
	    if numero % 2 != 0:
	        if maior is None or numero > maior:
	        	maior = numero
	if maior is not None:
		print(f"Maior Impar: {maior}")
	else: 
		print("Não há impares")
