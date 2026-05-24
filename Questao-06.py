# Menor Diferença
import random
v = []
t = int(input("Digite o tamanho:"))
for _ in range(t):
	v.append(random.randint(0,99))
if t <= 0:
	print("Insira um tamanho valido.")
elif t == 1:
	print("Precisa de pelo menos dois numeros")
else:
	print(v)
	menorDiff = abs(v[0] - v[1])
	A = v[0]
	B = v[1]
	
	for i in range(len(v)):
		for j in range(i+1,len(v)):
			diffAtual = abs(v[i] - v[j])
			if diffAtual < menorDiff:
				menorDiff = diffAtual
				A = v[i]
				B = v[j]
	print(f"O par {A} e {B} possuem a menor diferença")
