# La Programacion Orientada a Objetos es un Paradigma de la Programacion, que nos permite recrear cosas de la vida real en un entorno de programacion

# Cuando Nos referimos a un objeto, puede ser cualquier cosa, ya sea material o inmaterial, imaginaria o real.

# La POO nos ayuda modelar cosas complejas de forma sencilla, facilitando la creacion de programas y sistemas.

class Carro: # ¿Que es? Es un carro

    def __init__(self,marca,modelo): # ¿Como es?
        
        self.marca = marca # Es de tal marca
        self.modelo = modelo # Es tal modelo
        self.status = False # Esta apagado
        self.velocidad = 0 # Y tiene velocidad 0

    # ¿Que hace?
    
    def encender(self): # Se enciende
        print("Brrrr Brrrrr")
        self.status = True
    
    def apagar(self): # Se apaga
        print("brrr...")
        self.status = False

    def tocarCorneta(): # Puede tocar Corneta
        print("PIIIIIIIIIIII")

    def acelerar(self): # Aumentar su velocidad
        self.velocidad += 10

    def frenar(self): # Disminuir su velocidad
        self.velocidad -= 10

miCarro = Carro("Toyota","Corolla") # miCarro es un nuevo Objeto de la Clase Carro

print(miCarro.marca) # el atributo Marca de miCarro es Toyota

print(miCarro.modelo) # el atributo Modelo de miCarro es Corolla

miCarro.encender() # Enciendo miCarro

miCarro.acelerar() # Acelero miCarro

print(miCarro.velocidad) # el atributo Velocidad de miCarro

miCarro.frenar() # Freno miCarro

print(miCarro.velocidad) # el atributo Velocidad de miCarro

miCarro.apagar() # Apago miCarro

miCarro.tocarCorneta() # Toco la Corneta de miCarro