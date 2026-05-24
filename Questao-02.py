# O Segundo Maior Impar
import random
k = int(input("Digite o tamanho do seu vetor:"))
v = []
for _ in range(k):
    v.append(random.randint(0,100))
if k <= 0:
	print("Digite um tamanho valido")
else:
	print(v)
	maior = None
	segMaior = None
	for numero in v:
	    if numero % 2 != 0:
	        if maior is None or numero > maior:
		        segMaior = maior
		        maior = numero
	        elif numero != maior and (segMaior is None or numero > segMaior):
	        	segMaior = numero
	 
	if maior == None:
		print("Não há numeros impares")
	elif segMaior == None:
		print(f"Há somente um numero impar, o {maior}")
	else:
		print(f"Maior: {maior}")
		print(f"Segundo Maior: {segMaior}")
