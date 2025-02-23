import pandas as pd
import seaborn as sea
import matplotlib.pyplot as mat

df = df = pd.read_csv("archivos_problemas\\cofla.csv")
sea.barplot(x="fuente",y="ingresos",data=df)
totalingresos = df["ingresos"].sum()
print(f"El total de ingresos que tiene coflita es: {totalingresos}")
mat.show()