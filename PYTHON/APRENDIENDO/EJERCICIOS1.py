otrosmin= 2.5
otrosmax = 7
otrosprom = 4
estecurso = 1.5
crudoprom = 5
crudodalto = 3.5

tiempovacioprom = 100 - otrosprom * 1000 // crudoprom / 10
tiempovaciodalto = 100 - estecurso * 1000 // crudodalto / 10

# se puede hacer de otra forma con round(el numero , la cantidad de decimales),ejemplo:(12.0873479,3)=12.087
difmin = 100 - estecurso / otrosmin * 100
difmax = 100 - estecurso * 1000 // otrosmax / 10
difprom  = 100 - estecurso / otrosprom * 100
print("---------------")
print(f"El curso de Dalto dura un {difmin}% menos que el mas rapido")
print(f"El curso de Dalto dura un {difmax}% menos que el mas lento")
print(f"El curso de Dalto dura un {difprom}% menos que el promedio")
print("---------------")

print(f"Un curso promedio elimia un {tiempovacioprom}% de contenido vacio")
print(f"Un curso de Dalto  elimina un {tiempovaciodalto}% de contenido vacio")
print("---------------")
tiempoequivalente = otrosprom *100 // estecurso / 10
tiempoequivalentereves = estecurso *100 // otrosprom / 10
print(f"Ver 10 horas de este curso equivale a {tiempoequivalente} horas en otro")
print(f"Ver 10 horas de otro curso equivale a {tiempoequivalentereves} horas en Daltocurso")
print("---------------")
