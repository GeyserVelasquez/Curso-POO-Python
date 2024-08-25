class Animal:
    def __init__(self,nombre,color,peso):
        self.nombre = nombre
        self.color = color
        self.peso = peso

    def hacerRuido():
        pass

class Perro(Animal):

    def __init__(self,nombre,color,peso, pelaje, raza):
        super().__init__(nombre,color,peso)
        self.pelaje = pelaje
        self.raza = raza

    def darLaPata(self):
        print("Esta dando la pata")

    def hacerRuido(self):
        print("WOOF WOOF")

class Gato(Animal):
    def __init__(self,nombre,color,peso, edad, raza):
        super().__init__(nombre,color,peso)
        self.edad = edad
        self.raza = raza

    def rasguniar(self):
        print("Esta rasguniando")

    def hacerRuido(self):
        print("Miau Miau")

class Pato(Animal):
    def __init__(self,nombre,color,peso, edad, raza):
        super().__init__(nombre,color,peso)
        self.edad = edad
        self.raza = raza