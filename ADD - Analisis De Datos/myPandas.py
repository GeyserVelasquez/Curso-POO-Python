import pandas as pd

# Pandas es una biblioteca de Python para la manipulación y análisis de datos. 
# Ofrece estructuras de datos flexibles y eficientes, como los DataFrames y Series, 
# que permiten manejar y analizar datos tabulares y etiquetados de manera sencilla. 
# Pandas facilita operaciones como la limpieza de datos, el análisis estadístico, 
# y la manipulación de grandes conjuntos de datos, convirtiéndola en una herramienta clave 
# para el análisis de datos en Python.

# Cargar el archivo CSV en un DataFrame
dataFrame = pd.read_csv('ADD/datos.csv')

# Un DataFrame es una estructura de datos bidimensional en pandas, similar a una tabla de Excel.
# Está compuesto por filas y columnas, donde cada columna puede contener diferentes tipos de datos.
# Permite realizar operaciones como selección, filtrado, agrupación y manipulación de datos.

# Suelen verse asi:

#         Fecha  Producto  Cantidad  Precio
# 0  2024-08-01  Camiseta        10    20.0
# 1  2024-08-02  Pantalón         5    30.0
# 2  2024-08-03   Zapatos         2    50.0

# Como se puede apreciar, tiene columnas (Fecha,Producto,etc)... 
# ... y filas (todos los indices numericos de la izquierda)

# Imprimir el DataFrame para ver su contenido original
print("DataFrame Original:")
print(dataFrame)

print(dataFrame.describe()) 
# .describe() Nos genera estadísticas descriptivas resumidas de las columnas numéricas de un DataFrame. 
# Esto incluye métricas como la media, la desviación estándar, el valor mínimo, el valor máximo, y los percentiles (25%, 50%, 75%).

# Llenar valores faltantes en la columna 'Precio' con el valor anterior disponible (Forward Fill)
dataFrame['Precio'] = dataFrame['Precio'].ffill()

# Crear una nueva columna 'Total' calculando la cantidad multiplicada por el precio
dataFrame['Total'] = dataFrame['Cantidad'] * dataFrame['Precio']

# Imprimir el DataFrame actualizado con la nueva columna 'Total'
print("\nDataFrame con la columna 'Total':")
print(dataFrame)

print("-------------------------------------------")

# Filtrar el DataFrame para mostrar solo las filas con fecha posterior a '2024-08-02'
dataFrameActualizado = dataFrame[dataFrame['Fecha'] > '2024-08-02']

# Imprimir el DataFrame filtrado
print("\nDataFrame con Fecha posterior a 2024-08-02:")
print(dataFrameActualizado)

# Calcular los ingresos por producto sumando la columna 'Total' para cada producto
ingresos_por_producto = dataFrame.groupby('Producto')['Total'].sum()

# Imprimir los ingresos totales por producto
print("\nIngresos totales por producto:")
print(ingresos_por_producto)

# Resetear el índice del DataFrame, convirtiendo los productos en una columna
Productos = ingresos_por_producto.reset_index()

# Imprimir el DataFrame de productos con sus ingresos totales
print("\nIngresos totales por producto con el índice reseteado:")
print(Productos)

# Guardar el DataFrame actualizado en un nuevo archivo CSV
dataFrame.to_csv('datos_fixed.csv', index=False)

# Cosas adicionales para aprender sobre pandas:

# 1. El método `ffill()` es útil para rellenar valores faltantes en series temporales o secuencias. 
#    Puedes usar `bfill()` para rellenar con el siguiente valor disponible (backward fill).

# 2. `groupby()` es poderoso para agregar y resumir datos. Puedes usar funciones como `sum()`, `mean()`, `count()`, etc., después de agrupar los datos.

# 3. Filtrar DataFrames es esencial. Puedes usar operadores lógicos como `>`, `<`, `==` para seleccionar filas según condiciones específicas.

# 4. `reset_index()` es útil cuando deseas convertir el índice agrupado en una columna para un DataFrame más legible o cuando deseas manipular el DataFrame posterior a una agrupación.

# 5. Puedes aplicar funciones personalizadas a columnas usando el método `apply()`, por ejemplo, si necesitas realizar cálculos más complejos.

# 6. Existen muchas otras funciones útiles como `pivot_table()` para crear tablas dinámicas, `merge()` para combinar DataFrames, y `describe()` para obtener estadísticas descriptivas.

# 7. Pandas permite trabajar con series temporales de manera eficiente. Puedes parsear fechas y realizar resampling con funciones como `pd.to_datetime()` y `resample()`.

# 8. Puedes limpiar datos eliminando filas duplicadas con `drop_duplicates()` o rellenar NaN con un valor específico usando `fillna()`.

