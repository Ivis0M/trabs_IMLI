# forna para recorrer una lista obteniendo su indice
numeros = (23,28,34,44,56,2354)
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"El indice es: {indice} y el valor es: {valor}")
    
