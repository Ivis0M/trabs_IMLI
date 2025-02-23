import pandas as pd
import matplotlib.pyplot as mat
import seaborn as sea

df = pd.read_csv("archivos_problemas\\pedos.csv")
sea.lineplot(x="fecha",y="pedos",data=df)

mat.plot("01-09",17,"o")
mat.show()