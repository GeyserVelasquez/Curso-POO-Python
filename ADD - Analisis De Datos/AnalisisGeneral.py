import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar el archivo CSV en un DataFrame de pandas
# Un DataFrame es una estructura de datos bidimensional, similar a una tabla de base de datos
df = pd.read_csv('ADD/datos.csv')
print("Contenido del DataFrame:")
print(df)

# Calcular el total por producto multiplicando la cantidad por el precio
df['Total'] = df['Cantidad'] * df['Precio']
print("\nDataFrame con columna 'Total':")
print(df)

# Agrupar los datos por producto y sumar los ingresos para cada producto
ingresos_por_producto = df.groupby('Producto')['Total'].sum()
print("\nIngresos por producto:")
print(ingresos_por_producto)

# Filtrar ventas de un producto específico (por ejemplo, 'Camiseta')
ventas_camiseta = df[df['Producto'] == 'Camiseta']
print("\nVentas del producto 'Camiseta':")
print(ventas_camiseta)

# Usar numpy para realizar operaciones estadísticas sobre el precio y la cantidad
# np.mean calcula el promedio, np.std calcula la desviación estándar, y np.median calcula la mediana
promedio_precio = np.mean(df['Precio'])
desviacion_precio = np.std(df['Precio'])
mediana_cantidad = np.median(df['Cantidad'])

print(f"\nPromedio del precio: {promedio_precio}")
print(f"Desviación estándar del precio: {desviacion_precio}")
print(f"Mediana de la cantidad: {mediana_cantidad}")

# Graficar histogramas para visualizar la distribución de precios y cantidades
# Un histograma muestra la frecuencia de los datos en diferentes intervalos
plt.hist(df['Precio'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribución de Precios')  # Título del gráfico
plt.xlabel('Precio')  # Etiqueta del eje x
plt.ylabel('Frecuencia')  # Etiqueta del eje y
plt.axvline(promedio_precio, color='red', linestyle='dashed', linewidth=2, label='Promedio')  # Línea de promedio
plt.legend()  # Mostrar leyenda
plt.show()  # Mostrar el gráfico

plt.hist(df['Cantidad'], bins=10, color='lightgreen', edgecolor='black')
plt.title('Distribución de Cantidades')
plt.xlabel('Cantidad')
plt.ylabel('Frecuencia')
plt.axvline(mediana_cantidad, color='orange', linestyle='dashed', linewidth=2, label='Mediana')  # Línea de mediana
plt.legend()
plt.show()

# Gráfico de barras para mostrar los ingresos totales por producto
# Un gráfico de barras compara las cantidades en categorías
plt.bar(ingresos_por_producto.index, ingresos_por_producto.values, color='purple')
plt.title('Ingresos por Producto')
plt.xlabel('Producto')
plt.ylabel('Ingresos')
plt.show()

# Gráfico de dispersión para analizar la relación entre cantidad y precio
# Un gráfico de dispersión muestra cómo dos variables están relacionadas
plt.scatter(df['Cantidad'], df['Precio'], color='r')
plt.title('Relación entre Cantidad y Precio')
plt.xlabel('Cantidad')
plt.ylabel('Precio')
plt.show()

# Gráfico de la función seno usando numpy
# np.linspace genera valores igualmente espaciados, np.sin calcula el seno
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
plt.plot(x, y, color='blue', linestyle='-', label='sin(x)')
plt.title('Gráfico de la función seno')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()
plt.show()
