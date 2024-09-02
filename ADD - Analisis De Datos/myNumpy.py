import numpy as np

# NumPy (Numerical Python) es una biblioteca fundamental para la computación científica en Python. 
# Proporciona soporte para arreglos multidimensionales y matrices, junto con una colección 
# extensa de funciones matemáticas y operaciones para realizar cálculos numéricos eficientes. 
# NumPy es especialmente útil para el procesamiento de datos y la implementación de algoritmos 
# matemáticos y estadísticos debido a su alto rendimiento y facilidad de uso.


# Creación de arreglos unidimensionales y bidimensionales
arreglo = np.array([1, 2, 3])  # Arreglo unidimensional (1D)
matriz = np.array([[1, 2, 3], [4, 5, 6]])  # Arreglo bidimensional (2D)

# Imprimir los arreglos
print("Arreglo unidimensional:")
print(arreglo)
print("\nMatriz bidimensional:")
print(matriz)

# Convertir una lista a un conjunto para eliminar duplicados
lista = [6, 1, 2, 2, 3, 4, 5, 6, 6]
lista = set(lista)  # Elimina duplicados y convierte a un conjunto

# Imprimir los elementos del conjunto
print("\nElementos únicos en la lista:")
for item in lista:
    print(item)  # Imprime cada elemento único

# Suma y multiplicación de arreglos
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Suma de arreglos elemento a elemento
c = a + b  # Resultado: [5, 7, 9]

# Multiplicación de un arreglo por un escalar
d = 2 * a  # Resultado: [2, 4, 6]

print("\nSuma de arreglos:")
print(c)
print("Multiplicación de un arreglo por un escalar:")
print(d)

# Operaciones matemáticas avanzadas
x = np.array([0, np.pi/2, np.pi])
y = np.sin(x)  # Cálculo del seno de los ángulos en radianes

print("\nSeno de los ángulos:")
print(y)  # Resultado: [0.0, 1.0, 0.0]

# Segmentación de arreglos
a = np.array([1, 2, 3, 4, 5])

# Selección de una porción del arreglo
print("\nSegmento del arreglo:")
print(a[1:4])  # Resultado: [2, 3, 4]

# Operaciones avanzadas con NumPy

# 1. Creación de arreglos con valores específicos
zeros = np.zeros((3, 3))  # Arreglo de ceros de 3x3
ones = np.ones((2, 4))    # Arreglo de unos de 2x4
identity = np.eye(3)     # Matriz identidad de 3x3

print("\nArreglo de ceros 3x3:")
print(zeros)
print("\nArreglo de unos 2x4:")
print(ones)
print("\nMatriz identidad 3x3:")
print(identity)

# 2. Funciones estadísticas
data = np.array([1, 2, 3, 4, 5])
mean = np.mean(data)     # Media
std_dev = np.std(data)   # Desviación estándar

print("\nMedia de los datos:")
print(mean)
print("Desviación estándar de los datos:")
print(std_dev)

# 3. Operaciones de álgebra lineal
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Multiplicación de matrices
matrix_product = np.dot(matrix1, matrix2)

print("\nProducto de matrices:")
print(matrix_product)

# 4. Funciones universales (ufuncs)
log_values = np.log(np.array([1, np.e, np.e**2]))  # Logaritmo natural
exp_values = np.exp(np.array([0, 1, 2]))  # Exponencial

print("\nLogaritmos naturales:")
print(log_values)
print("Valores exponenciales:")
print(exp_values)

# 5. Redimensionamiento de arreglos
reshaped_array = np.arange(6).reshape(2, 3)  # Crear un arreglo de 6 elementos y redimensionarlo a 2x3

print("\nArreglo redimensionado 2x3:")
print(reshaped_array)
