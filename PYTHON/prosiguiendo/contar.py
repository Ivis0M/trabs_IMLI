import random 

def dd():
    resultado = random.randint(1,6)
    return resultado

lanzamiento = dd()
print(f"EL lanzamiento del dado dió: {lanzamiento}")