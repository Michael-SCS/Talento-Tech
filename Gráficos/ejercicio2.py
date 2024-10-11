import plotly.graph_objects as go

# Datos
productos = ['Producto A', 'Producto B', 'Producto C', 'Producto D']
ventas = [100, 150, 200, 250]

#Crear un gráfico de barras
fig = go.Figure(data=[go.Bar(x=productos, y=ventas)])

#Personalizar el gráfico
fig.update_layout(title='Ventas de productos')
xaxis_title='Productos'
yayis_title='Ventas'
fig.show()