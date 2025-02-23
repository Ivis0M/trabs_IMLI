# 2 listas, una con nombre y otra con apellidos
nombre = ["Mistic","Ivis","juleisca","Paloma","Palomota"]
apellido = ["Pequeñita","Grande","Melano","Palomototota","chica"]

with open("pepotas.txt","w",encoding=("UTF-8")) as pep:
    pep.writelines("Los datos son: \n --------\n")
    [pep.writelines(f"Nombre: {n}\nApellido: {a}\n -------------------\n")for n,a in zip(nombre,apellido)]
    
    
