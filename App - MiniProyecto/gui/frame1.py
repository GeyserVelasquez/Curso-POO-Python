import tkinter as tk
import tkinter.messagebox as msb
from classes import Persona
from db import DataBase as bdd

class Frame1(tk.Frame):

    activo = False
    #Definiremos como atributos, todos los componentes que deba tener nuestro frame

    nombreLabel = ""
    nombreInput = ""

    apellidoLabel = ""
    apellidoInput = ""

    edadLabel = ""
    edadInput = ""

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.iniciarComponentes()

    def registrarCliente(self): # Este metodo es para registrar un cliente

        try: # Codigo que se INTENTARA ejecutar
            nombre = self.nombreInput.get().capitalize() #Obtiene la entrada con Get y con Capitalize vuelve la inicial Mayusula y las demas letras Minusculas

            apellido = self.apellidoInput.get().capitalize() #Obtiene la entrada con Get y con Capitalize vuelve la inicial Mayusula y las demas letras Minusculas

            edad = self.edadInput.get() #Obtiene la entrada con Get

            self.validarEntradas(nombre,apellido,edad) #Valida si los datos de entrada tienen el formato adecuado

            clienteNuevo = Persona(nombre,apellido,edad) #Declara un nuevo objeto de la clase persona, llamado clienteNuevo, con los datos de entrada

            self.parent.bdd.insert(clienteNuevo)

        except ValueError as e: # Se ejecuta si hubo el ERROR especificado
            msb.showerror("Campos Incompletos", e)

        else: # Se ejecuta solamente si NO Hubo errores
            msb.showinfo("Operacion Exitosa", "El cliente fue agregado exitosamente.")
            self.vaciarEntradas()

        finally: # Se ejecuta SIEMPRE
            self.nombreInput.focus()

     #Inserta al final de la tabla los datos del nuevo cliente

    def validarEntradas(self,nombre,apellido,edad):
        if ( nombre == "" or apellido == "" or edad == "" ): #Valida si algun campo esta vacio o en blanco
            raise ValueError("Complete todos los campos.")

        if ( not nombre.isalpha() or not apellido.isalpha() ): 
            raise ValueError("Los nombres y los apellidos no pueden contener numeros.")
            # Valida si el nombre o el apellido contienen unicamente letras. 
            # La funcion isalpha (is Alphabetic) detecta si un string solo tiene letras, y al negar eso, significa que el string NO solo tiene letras

        if ( not edad.isnumeric() ): #Similar al anterior, valida si edad solamente contiene numeros. Al negar eso, significa que el string tiene numeros y otro tipo de caracter
            raise ValueError("Las edades solo pueden ser numeros.")

    def vaciarEntradas(self): #Deja en blanco todas las entradas del frame
        self.nombreInput.delete(0,tk.END) # Elimina desde el primer Char hasta el ultimo del string, en consecuencia, queda vacio
        self.apellidoInput.delete(0,tk.END) # Mismo Proceso que arriba
        self.edadInput.delete(0,tk.END) # Mismo Proceso que arriba


    def iniciarComponentes(self):  # Aquí se inicializan todos los widgets de nuestro frame
    
        # Definir tamaños relativos y fuente
        myFont = ("Arial", 12)
        label_width = 100 #En Pixeles
        input_width = 0.3
    
        # Crear widgets y colocarlos usando place con valores relativos

        #Creacion y posicionamiento del label para el nombre
        self.nombreLabel = tk.Label(self, text="Nombre", font=myFont)
        self.nombreLabel.place(relx=1.5/5, rely=1/5, width=label_width ,anchor="center")

        #Creacion y posicionamiento del input para el nombre
        self.nombreInput = tk.Entry(self, font=myFont)
        self.nombreInput.place(relx=3.5/5 , rely=1/5, relwidth=input_width, anchor="center")
    
        #Creacion y posicionamiento del label e input para el apellido
        self.apellidoLabel = tk.Label(self, text="Apellido", font=myFont)
        self.apellidoLabel.place(relx=1.5/5, rely=2/5, width=label_width, anchor="center")

        #Creacion y posicionamiento del input para el apellido
        self.apellidoInput = tk.Entry(self, font=myFont)
        self.apellidoInput.place(relx=3.5/5 , rely=2/5, relwidth=input_width, anchor="center")
    
        #Creacion y posicionamiento del label para la edad
        self.edadLabel = tk.Label(self, text="Edad", font=myFont)
        self.edadLabel.place(relx=1.5/5, rely=3/5, width=label_width, anchor="center")
        
        #Creacion y posicionamiento del input para la edad
        self.edadInput = tk.Entry(self, font=myFont)
        self.edadInput.place(relx=3.5/5 , rely=3/5, relwidth=input_width, anchor="center")

        #Creacion del boton del formulario
        self.enviar = tk.Button(self, text="Enviar", font=myFont)
        self.enviar.place(relx=0.5, rely=4/5, width=75, height=30, anchor="center")
        self.enviar.config(command=self.registrarCliente)  # Se le añade a este botón la función registrarCliente cuando se haga click
    