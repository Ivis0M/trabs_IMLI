# verificar si el numero que ingresa el usuario es par o impar

def parimp(num):
    if num % 2==0:
        return ("El numero es par")
    else:
        return ("El numero es impar")
    
num = int(input("Ingrese un numero: ")) 

print(parimp(num))