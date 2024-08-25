class Avion:

    def __init__(self, modelo, aerolinea, anio, tipo):
        self.modelo = modelo
        self.aerolinea = aerolinea
        self.anio = anio
        self.tipo = tipo
        self.volando = False

    def despegar(self):
        self.volando = True

    def aterrizar(self):
        self.volando = False

    def estaVolando(self):
        print("El avion de pepito se encuentra volando?")
        print( self.getEstado() )

    def getEstado(self):
        return self.volando

elAvionDePepito = Avion("Boeing 767", "Conviasa", 2015, "Comercial")

elAvionDeJuancito = Avion("Boeing 767", "Conviasa", 2015, "Comercial")

if ( elAvionDePepito == elAvionDeJuancito):
    print("Es lo mismo")
else:
    print("diferentes")







