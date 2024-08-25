# Cada archivo Python es un modulo que contiene Codigo, nosotros podemos acceder al codigo de otro archivo usando importaciones

from Herencia import Perro, Gato #Importacion Puntual
import Abstraccion # Importacion Absoluta con Apodo
from Encapsulamiento import * # Importacion Absoluta sin apodo

# Las importaciones sin apodos pueden causar interferencia si dentro de diferentes modulos hay nombres iguales
# Los apodos pueden ser dados a un modulo completo o a las importaciones puntuales

# from Herencia import Perro as P, Gato as G #Importacion Puntual
# import Abstraccion as AB
# from Encapsulamiento import * as ( Esta sintaxis es incompatible con apodos )

firulais = Perro("Firulais","Marron","10kg","Aspero","Golden Retriever")
michi = Gato("Michi","Gris", "3kg", 1, "Persa") #Aqui estamos creando Objetos con Clases que se encuentran en otros archivos

#-----------------------------------------------------------------------------------------------------------------------------------#


# El polimorfismo consiste en que un metodo o funcion, se comporte de forma diferente dependiendo de quien haga el llamado a dicho metodo

# Podemos aplicar polimorfismo, sobreescribiendo (Override) los metodos de una clase padre cuando se declare sus clases hijas

class Persona: #Clase Padre a la que se le aplicara polimorfismo
    def __init__(self,nombre):
       self.nombre = nombre
    
    def saludar(self): #Este es el metodo al que le aplicaremos Polimorfismo
        print("Hola! Mi nombre es" + self.nombre)
       
class Empleado(Persona): #Creacion de Primera Sub Clase
    def __init__(self,nombre,cargo):
        super.__init__(nombre) 
        self.cargo = cargo
    
    def saludar(self): #Aqui estamos sobreescribiendo el metodo saludar de la clase padre para que se comporte diferente
        print("Hola! Me llamo "+self.nombre+" y soy "+self.cargo)

class Cliente(Persona): #Creacion de Segunda Sub Clase
    def __init__(self,nombre,pedido):
        super.__init__(nombre)
        self.pedido = pedido
    
    def saludar(self): #Nuevamente sobreescribimos el metodo saludar de la clase padre para que se comporte diferente
        print("Hola! Me llamo "+self.nombre+" y mi pedido fue "+self.pedido)
    
#De esta forma, tendriamos 3 versiones del metodo saludar()


# Tambien se puede aplicar polimorfismo, creando varias funciones con el mismo nombre pero que reciban diferentes argumentos
try:
    def sumar(a,b): #Metodo base
        print(a+b)

    def sumar(a,b,c): #Metodo Polimorfico
        print(a+b+c)

    sumar(1,2) #Llamada al metodo base

    sumar(4,5,6) #Llamada al metodo polimorfico
except:
    print("Lastimosamente este tipo de polimorfismo no esta disponible en Python") 
    #Como lo leen aqui, este tipo de polimorfismo no es valido en pyton, pero sin en C++, Java, C#, etc.

# Uso del polimorfismo

vendedora = Empleado("Maria","Vendedora")

compradora = Cliente("Julia","Unos Zapatos")

vendedora.saludar() #Salida: Hola! Me llamo Maria y soy Vendedora
compradora.saludar() #Salida: Hola! Me llamo Julia y mi pedido fue Unos Zapatos

listaDePersonas = [vendedora,compradora] #Al anadir varios objetos de clases hermanas a una lista comun...

for persona in listaDePersonas: # ... podemos iterarlas y tambien hacer uso del polimorfismo
    persona.saludar() #Al usar polimorfismo, las clases hermanas pueden hacer uso de este metodo pero dando resultados diferentes

def polimorfismo(objeto): #Tambien podemos crear Funciones genericas que ejecuten los metodos a los que le aplicamos Polimorfismo
    objeto.saludar()

polimorfismo(vendedora) #Y de esta forma se ejecuta de forma generica un metodo polimorfico
polimorfismo(compradora)

# -------------------- 

wimin = Abstraccion.Persona("Wimin","Liang",20,michi) 
#Aqui tenemos un uso de los modulos, puesto que la clase persona tiene un atributo de Clase animal que se encuentra en otro archivo

Abstraccion.astroboy.saludarMascota(wimin.mascota) #Esta saludando al atributo mascota del objeto persona wimin
# Y por ultimo, tenemos un ejemplo de polimorfismo, en el que el objeto Robot astroboy, saluda mascotas ( Clase Animal ), independientemente si son Perros o Gatos



#Escalables y Mantenibles