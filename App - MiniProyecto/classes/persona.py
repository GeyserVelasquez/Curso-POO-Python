class Persona:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def saludar(self):
        print(f"Hola mi nombre es {self.nombre}")

class Cliente(Persona):
    def __init__(self, cargo, salario):
        super().__init__()
        self.cargo = cargo
        self.salario = salario