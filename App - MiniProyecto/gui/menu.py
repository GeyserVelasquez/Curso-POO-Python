import tkinter as tk
from tkinter import messagebox
from .frame1 import Frame1
from .frame2 import Frame2

class MenuBar(tk.Menu): # Menú Principal
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # Menú "Archivo"
        archivo_menu = tk.Menu(self, tearoff=0)
        archivo_menu.add_command(label="Nuevo", command=self.nuevo)
        archivo_menu.add_command(label="Abrir", command=self.abrir)
        archivo_menu.add_command(label="Guardar", command=self.guardar)
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Salir", command=parent.quit)
        self.add_cascade(label="Productos", menu=archivo_menu)

        # Menú "Editar"
        editar_menu = tk.Menu(self, tearoff=0)
        editar_menu.add_command(label="Cortar", command=self.cortar)
        editar_menu.add_command(label="Copiar", command=self.copiar)
        editar_menu.add_command(label="Pegar", command=self.pegar)
        self.add_cascade(label="Editar", menu=editar_menu)

        # Menú "Ver"
        ver_menu = tk.Menu(self, tearoff=0)
        ver_menu.add_command(label="Mostrar Frame 1", command=lambda: self.mostrar_frame(Frame1))
        ver_menu.add_command(label="Mostrar Frame 2", command=lambda: self.mostrar_frame(Frame2))
        self.add_cascade(label="Ver", menu=ver_menu)

        # Menú "Ayuda"
        ayuda_menu = tk.Menu(self, tearoff=0)
        ayuda_menu.add_command(label="Acerca de", command=self.acerca_de)
        self.add_cascade(label="Ayuda", menu=ayuda_menu)

    def nuevo(self):
        messagebox.showinfo("Nuevo", "Crear un nuevo archivo")

    def abrir(self):
        messagebox.showinfo("Abrir", "Abrir un archivo")

    def guardar(self):
        messagebox.showinfo("Guardar", "Guardar el archivo")

    def cortar(self):
        messagebox.showinfo("Cortar", "Cortar el texto")

    def copiar(self):
        messagebox.showinfo("Copiar", "Copiar el texto")

    def pegar(self):
        messagebox.showinfo("Pegar", "Pegar el texto")

    def acerca_de(self):
        messagebox.showinfo("Acerca de", "Este es un ejemplo de menú en Tkinter")

    def mostrar_frame(self, frame_requerido):

        viejoFrame = self.parent.frameActivo # Obtiene el Frame que se esta mostrando actualmente

        if isinstance(viejoFrame,frame_requerido): #Esto es para validar si el frame que se quiere abrir no existe ya
            return
        
        if viejoFrame:
            viejoFrame.destroy() # Si existe, lo elimina

        nuevoFrame = frame_requerido(self.parent) # Se procede a crear un nuevo objeto del frame solicitado
        nuevoFrame.grid_propagate(False) # Se evita que el Frame se encoja, evita que el frame se acople a sus widgets internos
        nuevoFrame.pack(fill='both', expand=True) # Inserta el nuevo Frame en la ventana principal de la aplicacion

        self.parent.frameActivo = nuevoFrame # Se guarda el nuevo frame en el atributo frameActivo de nuestra app, para poder volver a realizar este proceso en el futuro
