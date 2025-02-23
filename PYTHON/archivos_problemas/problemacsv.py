# Cambiar el tipo de dato de iuna columna, meeeeh
import pandas as pd
df = pd.read_csv("archivos_problemas\\datitos.csv")
df["edad"] = df["edad"].astype(str)
# print(type(df["edad"][0]))

# Remplazando un dato por otro mi daug
df["nombre"].replace("Ivis","Pelon",inplace=True)
# z

# Eliminar filas incompletas
# loca = df.dropna()
# print(loca)

df = df.drop_duplicates()
print(df)
df.to_csv("archivos_problemas\\datitoslimpitos.csv")