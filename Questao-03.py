# Achar Mediana de Duas Listas

def mediana_duas_listas(U, V):
    tamanho = len(U)
    
    inicio = 0
    fim = tamanho
    
    while inicio <= fim:
        meioU = (inicio + fim) // 2
        meioV = tamanho - meioU
        
        if meioU == 0:
            esqU = float('-inf')
        else:
            esqU = U[meioU - 1]
            
        if meioU == tamanho:
            dirU = float('inf')
        else:
            dirU = U[meioU]
            
        if meioV == 0:
            esqV = float('-inf')
        else:
            esqV = V[meioV - 1]
            
        if meioV == tamanho:
            dirV = float('inf')
        else:
            dirV = V[meioV]
            
        if esqU <= dirV and esqV <= dirU:
            return max(esqU, esqV)
            
        elif esqU > dirV:
            fim = meioU - 1
            
        else:
            inicio = meioU + 1
