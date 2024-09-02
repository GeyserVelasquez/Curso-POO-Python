import matplotlib.pyplot as plt
import mySeries as ms

# Matplotlib es una biblioteca de Python para la creación de gráficos y visualizaciones de datos. 
# Proporciona una amplia gama de opciones para crear gráficos estáticos, animados e interactivos, 
# incluyendo gráficos de líneas, barras, histogramas, dispersión, y más. 
# La biblioteca es altamente personalizable y permite ajustar todos los aspectos del gráfico, 
# desde el estilo y el formato hasta el diseño y los elementos visuales. 
# Matplotlib es una herramienta fundamental para la visualización de datos en el análisis científico y en el desarrollo de aplicaciones.

def mostrar_grafico(opcion):
    match opcion:
        case 'lineal':
            # Datos para el gráfico de líneas
            x = [1, 2, 3, 4, 5]
            y = [2, 4, 6, 8, 10]

            # Crear el gráfico de líneas
            plt.plot(x, y)

            # Añadir título y etiquetas
            plt.title('Gráfico de líneas')
            plt.xlabel('Eje X')
            plt.ylabel('Eje Y')

            # Mostrar el gráfico
            plt.show()

        case 'picos':
            # Datos para el gráfico de picos
            x = [1, 2, 3, 4, 5]
            y = [2, 4, 1, 9, 5]

            # Crear el gráfico de líneas
            plt.plot(x, y, color='green')

            # Añadir título y etiquetas
            plt.title('Gráfico con picos por variacion')
            plt.xlabel('Eje X')
            plt.ylabel('Eje Y')

            # Mostrar el gráfico
            plt.show()

        case 'barra':
            # Datos para el gráfico de barras
            categorias = ms.inflacion.index
            valores = ms.inflacion.values

            # Crear el gráfico de barras con diferentes colores para cada barra
            colores = ['red', 'green', 'blue', 'orange']

            plt.bar(categorias, valores, color=colores)

            # Añadir título y etiquetas
            plt.title('Gráfico de barras con colores diferentes')
            plt.xlabel('Categorías')
            plt.ylabel('Valores')

            # Mostrar el gráfico
            plt.show()

        case 'histograma':
            # Datos para el histograma
            datos = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5,5,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

            # Crear el histograma
            plt.hist(datos, bins=5, edgecolor='black')

            # Añadir título y etiquetas
            plt.title('Histograma')
            plt.xlabel('Valores')
            plt.ylabel('Frecuencia')

            # Guardar el gráfico como archivo PNG
            plt.savefig('histograma.png')

            # Mostrar el gráfico
            plt.show()

        case 'personalizado':
            # Datos para el gráfico
            x = [1, 2, 3, 4, 5]
            y = [2, 4, 6, 8, 10]

            # Crear el gráfico de líneas con personalización
            plt.plot(x, y, color='red', linestyle='--', marker='o', label='Línea 1')

            # Añadir título y etiquetas
            plt.title('Gráfico de líneas personalizado')
            plt.xlabel('Eje X')
            plt.ylabel('Eje Y')

            # Añadir una leyenda
            plt.legend()

            # Mostrar el gráfico
            plt.show()

        case 'guardar':
            # Crear un gráfico de ejemplo
            x = [1, 2, 3, 4, 5]
            y = [2, 4, 6, 8, 10]
            plt.plot(x, y)

            # Guardar el gráfico como archivo PNG
            plt.savefig('grafico.png')

            # Mostrar el gráfico en la pantalla
            plt.show()

        case _:
            print("Opción no válida. Las opciones son: 'linea','picos' 'barra', 'histograma', 'personalizado', 'guardar'.")

while True:
    # Solicitar la opción al usuario
    opcion = input("Elige el tipo de gráfico (linea, picos, barra, histograma, personalizado, guardar): ")
    mostrar_grafico(opcion)
