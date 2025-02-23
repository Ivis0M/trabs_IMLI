estecurso = 1.5
minimootros = 2.5
promotros = 4
maxotros = 7 
crudodalto = 3.5
crudoprom = 5

difmasrapido = 100 - estecurso / minimootros * 100
difmaslento = 100 - estecurso / maxotros * 100
difpromedio = 100 - estecurso / promotros * 100
print(f"Este curso es: {difmasrapido}% mas rapido que el mas rapido" )
print(f"Este curso es: {round(difmaslento,1)}% mas rapido que el mas lento")
print(f"Este curso es: {difpromedio}% mas rapido que el promedio de cursos")
print("--------------------------")
vacioeste = 100 - estecurso / crudodalto * 100
vacioprom = 100 - promotros / crudoprom * 100
print(f"Este curso elimina un {round(vacioeste,1)}% de contenido vacio")
print(f"El promedio de otros cursos elimina un {vacioprom}% de contenido vacio")
print("--------------------------")

tiempo = promotros*100/estecurso/10
tiemporeves = estecurso * 100 /promotros/10
print(f"Ver 10 horas de este curso equivale a ver {round(tiempo,1)} horas de otros cursos")
print(f"Ver 10 horas otro curso equivale a ver {round(tiemporeves,1)} horas de este curso")