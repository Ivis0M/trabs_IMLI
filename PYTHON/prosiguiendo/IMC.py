def IMC():
    kilos = float(input("Ingrese su peso en kg: "))
    estatura = float(input("Ingrese su estatura en metros: "))
    indice = kilos/(estatura**2)
    print(f"Su indice de masa corporal es: {round(indice,2)}")
    
    if indice<18.5:
        print("Rango de peso muy bajo")
    elif indice<24.9:
        print("Buen rango de peso")
    elif indice>24.9 and indice<70:
        print("Rango de peso muy alto")
    elif indice>100:
        print("CUIDADO")
        
IMC()