def saludar():
    print("Hola Muchachos")

#El encapsulamiento consiste en ocultar ciertos atributos y metodos de una clase. Con el fin de proteger la informacion
#Tambien se usa para aislar la logica de un programa, y que los procesos de uno no interfieran con otros.

class Coche:
    def __init__(self, marca, modelo):
        self.__marca = marca  # Atributo privado
        self.__modelo = modelo  # Atributo privado
    
    def obtener_info(self):
        return f'Marca: {self.__marca}, Modelo: {self.__modelo}'
    
    def actualizar_marca(self, nueva_marca):
        self.__marca = nueva_marca

# Uso del encapsulamiento
mi_coche = Coche('Toyota', 'Corolla')
print(mi_coche.obtener_info())  # Salida: Marca: Toyota, Modelo: Corolla

mi_coche.actualizar_marca('Honda')
print(mi_coche.obtener_info())  # Salida: Marca: Honda, Modelo: Corolla


try: # Intentando acceder directamente a los atributos privados dará error
    print(mi_coche.__marca)  # Esto generará un error
except:
    print("Surgio un error inesperado")

# Este bloque se conoce como Manejo de Excepciones o Try-Catch
# Intentara ejecutar un codigo ( Bloque Try ), y si sucede un error, se va hacia el bloque Except



