from datetime import datetime
def tuedad():
    dato = int(input("Ingrese su año de nacimiento: "))
    fecha = datetime.now().year
    edad = fecha - dato
    print(f"Su edad es: {edad}")

tuedad()