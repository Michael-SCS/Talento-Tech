import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

#Generar un conjunto de datos aleatorios
np.random.seed(42)

#Caracteristicas de las viviendas
num_houses = 100
square_feet = np.random.randint(500, 4000, num_houses)
num_bedrooms = np.random.randint(1, 6
, num_houses)
num_bathrooms = np.random.randint(1, 4, num_houses)
age = np.random.randint(1, 30, num_houses)

#Precio simulado
price =(square_feet * 150)+(num_bedrooms * 20000)+(num_bathrooms * 10000)-(age*500)+np.random.normal(0,15000,num_houses)


#Crear un DataFrame
data = pd.DataFrame({'square_feet': square_feet, 'num_bedrooms': num_bedrooms, 'num_bathrooms': num_bathrooms, 'age': age, 'price': price})

#primeras filas
print(data.head())

#Visualizar la relacion entre las caracteristicas y el precio
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.scatterplot(x='square_feet', data=data, y='price')
plt.title('Price vs Square Feet')

plt.subplot(1, 2, 2)
sns.boxplot(x='num_bedrooms', data=data, y='price')
plt.title('Price vs Number of Bedrooms')
plt.tight_layout()
plt.show()

#Modelo de regresion lineal
x=data[['square_feet', 'num_bedrooms', 'num_bathrooms', 'age']]
y=data['price']

#Dividir el conjunto de datos en entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#crear el modelo
model = LinearRegression()
model.fit(x_train, y_train)

#Predecir los precios
y_pred = model.predict(x_test)


#Evaluar el modelo
print('Model Coefficients:', model.coef_)
print('Model Intercept:', model.intercept_)
print('Model Score:', model.score(x_test, y_test))

#Gráfico de comparación de precios reales y predichos

plt.figure(figsize=(12, 6))
plt.scatter(y_test, y_pred)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)])
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.title('Actual Price vs Predicted Price')
plt.show()

