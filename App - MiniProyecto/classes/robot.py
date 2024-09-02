class Robot:
    def __init__(self,modelo,color):
        self.modelo = modelo
        self.color = color
    
    def darInformacion(self):
        print(f"Hola. Soy el Modelo {self.modelo}")