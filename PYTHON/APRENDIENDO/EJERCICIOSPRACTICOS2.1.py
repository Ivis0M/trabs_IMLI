# pedir edades de los alumnos y ordenarlas de mayor a menor
# cual es el mayor y cual es el menor
# el mayor sera erl profesor y el menor su asitente

def obtener_compañero(cantidad):
    compañeros = []
    for i in range(cantidad):
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))
        compañero =(nombre, edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return asistente,profesor
asistente,profesor = obtener_compañero(10)
print(f"El profesor es: {profesor} y su asistente es: {asistente}")




    
    
    
    

