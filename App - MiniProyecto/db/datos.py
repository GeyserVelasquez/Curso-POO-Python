import sqlite3

# Esta clase DataBase , es un claro ejemplo de como la POO nos ayuda a segmentar y organizar nuestro codigo ( Modularizacion )
# De forma limpia y ordenada, tenemos separado todas los procesos que pudiese realizar nuestra bdd, sin tener un codigo en el que todo este en un mismo bloque.

# Con esta clase, el uso de la bdd de forma externa queda relegado unicamente a los metodos, 
# puesto que los atributos estan privados incluyendo los metodos que los manipulan directamente ( Encapsulamiento )

# Solamente tenemos lo escencial para el uso de nuestra bdd, sin crear codigo complicado sin uso aparente ( Abstraccion )

# Si tuviesemos muchas BDD , podriamos utilizar esta clase como clase padre para gestionar las otras BDD ( Herencia )

class DataBase:
    def __init__(self):
        self.__conexion = None
        self.__cursor = None

    def __IniciarConn(self):
        self.__conexion = sqlite3.connect('datos.db') #Se inicia la conexion a la base de datos
        self.__cursor = self.__conexion.cursor() # Se crea un cursor para navegar en la base de datos

    def __verifyTable(self): # Verificar si existe la tabla Persona, sino, la crea
        self.__cursor.execute('''
            CREATE TABLE IF NOT EXISTS personas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            edad INTEGER
            )
        ''') 

    def __closeConn(self):
        self.__conexion.close() #Cerrar la conexion
        
    # Nota: Esto es solo un ejemplo, en las bases de datos bajo ningun concepto se debe guardar la edad de una persona, 
    # porque es un dato muy variable que tendria que ser actualizado con mucha frecuencia; lo que se hace es guardar su fecha de nacimiento.

    def insertByParts(self,nombre,apellido,edad):
        self.__IniciarConn() # Iniciar conexion
        self.__verifyTable() # Verificar Existencia de la Table Personas
        self.__cursor.execute('INSERT INTO personas (nombre, apellido, edad) VALUES (?, ?, ?)', (nombre, apellido, edad) ) # Insertar o registrar una persona
        self.__conexion.commit() #Guardar Cambios
        self.__closeConn() #Cerrar conexion

    def insert(self,persona):
        self.insertByParts(persona.nombre,persona.apellido,persona.edad)

    def insertMany(self,people):
        self.__IniciarConn() # Iniciar conexion
        self.__verifyTable() # Verificar Existencia de la Table Personas
        self.__cursor.executemany('INSERT INTO personas (nombre, apellido, edad) VALUES (?, ?, ?)', people ) # Insertar o registrar varias persona
        self.__conexion.commit() #Guardar Cambios
        self.__closeConn() # Cerrar conexion
    
    def getPerson(self,nombre, apellido, edad):
        self.__IniciarConn() # Iniciar conexion
        self.__verifyTable() # Verificar Existencia de la Table Personas
        self.__cursor.execute('SELECT * FROM personas WHERE nombre = ? AND apellido = ? AND edad = ?', (nombre, apellido, edad) ) # Obtener una persona en especifico
        person = self.__cursor.fetchone()
        self.__closeConn() # Cerrar conexion
        return person

    def getPeople(self):
        self.__IniciarConn() # Iniciar conexion
        self.__verifyTable() # Verificar Existencia de la Table Personas
        self.__cursor.execute('SELECT * FROM personas') # Obtener TODAS las personas
        people = self.__cursor.fetchall()
        self.__closeConn() # Cerrar conexion
        return people
    
    def updateName(self,nombreActual,nombreNuevo):
        self.__IniciarConn() # Iniciar conexion
        self.__verifyTable() # Verificar Existencia de la Table Personas
        self.__cursor.execute('UPDATE personas SET edad = ? WHERE nombre = ?', (nombreNuevo,nombreActual) ) # Actualizar un Dato
        self.__conexion.commit() #Guardar Cambios
        self.__closeConn() # Cerrar conexion

    def deletePerson(self,nombre,apellido):
        self.__IniciarConn() # Iniciar conexion
        self.__verifyTable() # Verificar Existencia de la Table Personas
        self.__cursor.execute('DELETE FROM personas WHERE nombre = ? AND apellido = ? ', (nombre,apellido)) # Eliminar Registro
        self.__conexion.commit() #Guardar Cambios
        self.__closeConn() # Cerrar conexion


# Con las base de datos, se lleva a cabo un proceso de Backend conocido como CRUD

#CREATE - Insert
#READ - Select
#UPDATE - Update
#DELETE - Delete

# Esto se refiere a las operaciones basicas que se pueden realizar en cualquier sistema, y son escenciales hoy en dia en todos ellos.

bdd = DataBase()

a = bdd.getPeople()

for b in a:
    # print(b)
    print(b[0])