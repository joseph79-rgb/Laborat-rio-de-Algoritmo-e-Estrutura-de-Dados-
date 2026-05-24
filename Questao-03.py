# Busca Aproximada
 import random

v = []
t = int(input("Digite o tamanho:"))
for _ in range(t):
   v.append(random.randint(0,100))
if t <= 0:
   print("Insira um tamanho válido.")
   
else:
	print(v)
	achei = 0
	menorDiff = 0
	k = int(input("Digite seu numero:"))
	for i in range(len(v)):
		if v[i] == k:
			achei = 1
			print(f"Sim, o {k} esta presente")
			break
	
	if achei == 0:
		menorDiff = abs(v[0] - k)
		maisProx = v[0]
		for i in range(len(v)):
			diffAtual = abs(v[i] - k)
			if diffAtual < menorDiff:
				menorDiff = diffAtual
				maisProx = v[i]
		print(f"({k} nao foi achado, mas {maisProx} eh o mais proximo.")
