import pandas as pd
import seaborn as sea
import matplotlib.pyplot as mat

df = df = pd.read_csv("archivos_problemas\\dispersion.csv")
sea.scatterplot(x="tiempo",y="dinero",data=df)


mat.show()