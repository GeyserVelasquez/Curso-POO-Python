# La Abstraccion consiste en utilizar los elementos mas simples que podamos dado el contexto en que el que estemos programando.
# Si vamos a programar un robot o un humano, no hace falta saber como esta hecho por dentro.

class Robot: # En este ejemplo, la clase robor es muy simple. 
    def __init__(self,modelo,color):
        self.modelo = modelo #Solo tiene dos atributos
        self.color = color
    
    def darInformacion(self): # Y dos metodos
        print(f"Hola. Soy el Modelo {self.modelo}")

    def saludarMascota(self,mascota):
        print("Hola "+mascota.nombre)

class Persona: # En este otro ejemplo, la clase persona solo tiene datos basicos. No conocemos su personalidad ni su aspecto fisico.
    def __init__(self,nombre,apellido,edad, mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.mascota = mascota
    
    def saludar(self):
        print(f"Hola mi nombre es {self.nombre}")

astroboy = Robot("Astro-5","Plateado")

# La abstraccion es un proceso cognitivo muy importante en la programacion
# Es una habilidad escencial que nos permite sintetizar nuestras ideas y plasmarmarlas en el codigo
# Para mejorar esto se debe practicar la Logica de Programacion, resolviendo ejercicios complejos y desafiantes.

