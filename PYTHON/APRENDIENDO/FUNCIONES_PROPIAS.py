def sexo():
    print("HOLA MUCHACHOS SOY MUY BUENO EN PSEINT PERO EN PYTHON ME COTORREAN ENTERITO")
contador = 0   
while contador<20:
    contador+=1
    sexo()
    
def saludar(nombre,sexualidad):
    sexualidad=sexualidad.lower()
    if (sexualidad == "mujer"):
        adjetivo = "chavala"
    elif (sexualidad == "hombre"):
        adjetivo = "chavalo"
    print(f"Hola {nombre}, como estas {adjetivo} ")
saludar("Fernando","hombre")


