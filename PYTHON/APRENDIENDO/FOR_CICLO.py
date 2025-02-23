numeros = [35,43,67]
nombres = ["pichula", "sexoanal","patoso"]
# forma no optica que vino de mi cabeza
for numero in numeros:
    for nombre in nombres:
        print (f"lista 1: {nombre}")
        print (f"lista 2: {numero}")
# lo mismo de arriba pero ordenado(primero la lista 1 y despues la lista 2)
print("---------------------")
for numero in numeros:
    print (f"lista 1: {numero}")

for nombre in nombres:
     print (f"lista 2: {nombre}")
print("---------------------")     
 # forma optica de la primera que se muestra en este algortimo.(añadido:else con for)    
for numero,nombre in zip(numeros,nombres):
    print (f"lista 1: {nombre}")
    print (f"lista 2: {numero}")

else:
    print("El bucle termino")    
    
# todo esto funciona igual con las tuplas  igual en sets(conjuntos) pero en este caso hay excepciones(no muchas ni tan importantes)