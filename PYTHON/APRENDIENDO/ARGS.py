#FORMA OPTICA(*args)
def suma(nombre, *numeros):
    return f"{nombre} la suma de tus numeros es: {sum(numeros)}"

resultado = suma("IVIS",5,5,5,5)
print(resultado)
# FORMA NO OPTICA
def suma(numeros):
    numerossumados= 0
    for num in numeros:
        numerossumados = numerossumados + num
    return numerossumados
resultado = suma([5,5,5,5])
print(resultado)



