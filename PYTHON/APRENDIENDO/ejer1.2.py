# las personas hablan 2 palabras por minuto
# pedir texto e identificar en cuanto tiempo aprox se diria y cuantas palabras dijo
texto = input("Ingrese el texto: ")
resultado = texto.split(" ")
cantidad = len(resultado)

tiempo_en_decirlo = cantidad / 2
print(f"Dijiste {cantidad} palabras")
print("-----------------")
print(f"Tardarias {tiempo_en_decirlo} segundos en decirlo")

if tiempo_en_decirlo > 60:
    print("Para flaco, tampoco te pedi un testamento")

tiempo_dalto = tiempo_en_decirlo * 0.30
print(f"Dalto tardaria {tiempo_dalto} segundos en decirlo")
