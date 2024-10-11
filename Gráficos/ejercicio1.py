import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#Crear Dataframe
data = {'edad':[25,30,35,40,45,50,50],
'Salario':[50000,60000,75000,80000,85000,90000,95000]
}
df = pd.DataFrame(data)

#Gráfico de dispersión
sns.scatterplot(x='edad',y='Salario',data=df)
plt.title('Relación entre edad y salario')
plt.show()