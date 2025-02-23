# Usando continues e if en un ciclo for
hamburguesa = ["pan","pepinillos","tomate","lechuga","queso","carne","aderezo"]

elementonodeseado =input("Que elemento no desea en su hamburguesa? ")

for elemento in hamburguesa:
    if elemento==elementonodeseado:
        break
    print(f"Su hamburguesa contendra: {elemento}")

# evitar que el bucle siga ejecutandose, se utiliza el break, este termina el ciclo for incluso si hay un else despues
# recorrer cadena de texto
cadena = "hola perrito sexoanal"
for letra in cadena:
    print(letra)
    
numeros = [2,4,6,8]
numeros_duplicados = [x*2 for x in numeros]
print(f"Los numeros de la lista son: {numeros}")
print(f"Y los numeros duplicados son: {numeros_duplicados}")


