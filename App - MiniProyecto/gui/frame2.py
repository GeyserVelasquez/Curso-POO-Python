import tkinter as tk
import tkinter.ttk as ttk
from classes.persona import Persona

class Frame2(tk.Frame):

    activo = False

    tablaClientes = None

    # Crear las barras de desplazamiento
    vsb = None # Vertical Scroll Bar
    hsb = None # Horizontal Scroll Bar

    def __init__(self, parent): #Constructor
        super().__init__(parent)
        self.parent = parent
        self.iniciarComponentes()

    def cargarClientes(self):
        lista = self.parent.bdd.getPeople() # Llamada al atributo bdd de la clase App para acceder de forma sencilla a la bdd

        for tupla in lista: # Iteracion de la respuesta de la bdd
            cliente = Persona(tupla[1],tupla[2],tupla[3]) # Creamos un objeto con los datos actuales del ciclo for
            self.agregarCliente(cliente) #Agregamos el cliente al cuadro/treeview/excel xdddd
        

    def agregarCliente(self,cliente): #Metodo para insertar los valores en el Treeview
        self.tablaClientes.insert("", tk.END, values=( cliente.nombre, cliente.apellido, cliente.edad ) )

    def iniciarComponentes(self): # Metodo para inicializar y configuar los widgets que tiene Frame 2 como atributos

        style = ttk.Style() #Personalizacion avanzada de widgets

        style.theme_use("clam")

        style.configure("Treeview",
                    background="silver",
                    foreground="black",
                    rowheight=55,
                    fieldbackground="silver",
                    font=("Arial",12)
                )

        #Change selected color:
        style.map("Treeview",
              background=[('selected', 'skyblue')])

        #Creacion del objeto treeview/tabla. Este componente tambien se conoce como DataGrid, DataGridView o DataTable
        self.tablaClientes = ttk.Treeview(self, columns=("Nombre", "Apellido", "Edad"), show="headings", style="Treeview")

        self.tablaClientes.heading("Nombre", text="Nombre") # Se crean los encabezados de la tabla
        self.tablaClientes.heading("Apellido", text="Apellido")
        self.tablaClientes.heading("Edad", text="Edad")

        self.tablaClientes.column("Nombre", minwidth=0, width=100) # Se crean las columnas y se asocian a un encabezado
        self.tablaClientes.column("Apellido", minwidth=0, width=100)
        self.tablaClientes.column("Edad", minwidth=0, width=50)

        # Creacion de los objetos correspondientes a las barras de desplazamiento
        self.vsb = tk.Scrollbar(self.tablaClientes, orient="vertical", command=self.tablaClientes.yview)
        self.hsb = tk.Scrollbar(self.tablaClientes, orient="horizontal", command=self.tablaClientes.xview)

        #Configuracion del atributo Treevie/Tabla
        self.tablaClientes.config(yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set)
        
        #Se posiciona la tabla (Se coloco en el punto 0,0 y se extiende por toda la pantalla)
        self.tablaClientes.place(relx=0,rely=0,relwidth=1,relheight=1)

        # Se colocan los scroll bars, a la derecha y abajo respectivamente
        self.vsb.pack(side="right", fill="y")
        self.hsb.pack(side="bottom", fill="x")

        #Se cargan de la bdd todos los clientes y se muestran en la tabla
        self.cargarClientes()