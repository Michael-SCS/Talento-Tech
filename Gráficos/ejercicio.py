from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource

# Configurar la salida en un archivo HTML
output_file("estudiantes_por_clase.html")

# Datos
clases = ['Clase A', 'Clase B', 'Clase C', 'Clase D']
estudiantes = [20, 30, 15, 25]

source = ColumnDataSource(data=dict(clases=clases, estudiantes=estudiantes, color=['blue', 'green', 'red', 'yellow']))

# Crear gráfico de barras
p = figure(x_range=clases, height=350, title='Estudiantes por clase', toolbar_location=None, tools='')
p.vbar(x='clases', top='estudiantes', width=0.9, color='color', legend_field='clases', source=source)

# Personalizar gráfico
p.xgrid.grid_line_color = None
p.y_range.start = 0
p.legend.orientation = "horizontal"
p.legend.location = "top_center"

# Mostrar el gráfico
show(p)
