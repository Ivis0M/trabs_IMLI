import pandas as pd
import seaborn as sea
import matplotlib.pyplot as mat

df = df = pd.read_csv("archivos_problemas\\bigotes.csv")
sea.boxplot(x="categoria",y="valor",data=df)

mat.show()