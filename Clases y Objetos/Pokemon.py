class Pokemon:
    def __init__(self, nombre, tipo, nivel, color, movs, atq, defs, hp, pp, estado):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel
        self.color = color
        self.movs = movs
        self.atq = atq
        self.defs = defs
        self.hp = hp
        self.pp = pp
        self.estado = estado # Paralizado, quemado, congelado, Fainted, Alive

    def atacar(self, i):
        print("Ha usado " + self.movs[i] ) # 0,1,2,3

    def evolucionar(self, pokemon):

        self.nombre = pokemon.nombre
        self.tipo = pokemon.tipo
        self.nivel = pokemon.nivel
        self.color = pokemon.color
        self.movs = pokemon.movs
        self.atq = pokemon.atq
        self.defs = pokemon.defs
        self.hp = pokemon.hp
        self.pp = pokemon.pp
        self.estado = pokemon.estado

    def cambiar(self, pokemon):
        print("Cambio a: "+pokemon.nombre)

miPokemon = Pokemon ("Bulbasaur", ["Planta","Veneno"], 5,"Verde Lechuga",["Latigo Cepa","Placaje"],10,7,25,10,"Sano")

pokemonNuevo = Pokemon ("Ivysaur", ["Planta","Veneno"], 17,"Verde Lechuga",["Latigo Cepa","Placaje"],10,7,25,10,"Sano")


print(miPokemon.movs[0]+" "+miPokemon.movs[1])
numero = int ( input("Elige Ataque") )

print( miPokemon.atacar(numero) )

miPokemon.evolucionar(pokemonNuevo)

print(miPokemon.nombre)