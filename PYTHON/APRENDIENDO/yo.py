listaed = []
x = 0
while  x<10 :
    x+=1
    listaed = int(input("Ingrese edad: "))
    
lo=listaed.sort()
print(lo)

print(f"EL mayor es: {max(lo)} por lo cual sera el profesor")
print(f"El menor es: {min(lo)} por lo cual sera el asistente del profesor")
