# crear una calculadora en base a opciones
def calc():
    opcion = int(input("Elija una opcion. 1.Sumar - 2.Restar - 3.Multiplicar  "))
    if opcion == 1:
        print("USTED ELIGIO LA OPCION SUMAR: ")
        num1 = int(input("Ingrese primer numero: "))
        num2 = int(input("Ingrese segundo numero: "))
        tots = num1 + num2
        print(f"El total es: {tots}")
    elif opcion == 2:
        print("USTED ELIGIO LA OPCION RESTAR: ")
        num1 = int(input("Ingrese primer numero: "))
        num2 = int(input("Ingrese segundo numero: "))
        tots = num1 - num2
        print(f"El total es: {tots}")
    elif opcion == 3:
        print("USTED ELIGIO LA OPCION MULTIPLICAR: ")
        num1 = int(input("Ingrese primer numero: "))
        num2 = int(input("Ingrese segundo numero: "))
        tots = num1 * num2
        print(f"El total es: {tots}")
    else:
        print("NO SE ENCONTRO UNA OPCION DADO SU PARAMETRO")
        return calc()
calc()
