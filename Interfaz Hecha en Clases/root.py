import tkinter as tk
from tkinter import messagebox # Módulo de tkinter que nos permite mostrar mensajes emergentes

# Función para cambiar entre frames
def mostrar_frame(frameActivo, frameRequerido):
    if frameActivo == frameRequerido: 
        return  # Si el frame activo ya es el frame requerido, no hacemos nada

    frameActivo.destroy()  # Destruimos el frame activo actual
    frameRequerido.pack(side="right", fill="both", expand=True)  # Mostramos el frame requerido

# Configuración de la ventana principal
root = tk.Tk()  # Creamos la ventana principal
root.title("Holick")  # Título de la ventana
root.geometry("500x500")  # Tamaño de la ventana

# Evita que el Frame se ajuste al tamaño del contenido
root.pack_propagate(False)

# Creación del Header (encabezado)
header = tk.Frame(
    root, 
    height=75,
    padx=10, 
    pady=10,
    cursor="arrow",
    bg= "#1e3dd4"  # Color de fondo azul
)

HEADER_COLOR = "#1e3dd4"  # Color constante para el header

# Creación del SideBar (barra lateral)
sideBar = tk.Frame(
    root,
    width=100,
    padx=10, 
    pady=10,
    cursor="arrow",
    bg="#0c1b72"  # Color de fondo azul oscuro
)

# Creación del Frame principal
main = tk.Frame(
    root,
    padx=10, 
    pady=10,
    cursor="arrow",
    bg="#e8e8e8"  # Color de fondo gris claro
)

# Creación del Frame de registro
registro = tk.Frame(
    root,
    padx=10, 
    pady=10,
    cursor="arrow",
    bg="#e8e8e8"  # Color de fondo gris claro
)

# Mostramos el header en la parte superior de la ventana
header.pack(side="top", fill="x")

# Creación de un Label en el Header
Holick = tk.Label(header, text="Holick", font=("Arial", 50), bg=HEADER_COLOR, foreground="white")
Holick.place(x=100, rely=0.5, anchor="center")  # Posicionamos el Label en el Header

# Mostramos el SideBar en la parte izquierda de la ventana
sideBar.pack(side="left", fill="y")

# Creación de botones en el SideBar con diferentes funcionalidades
btn_saludar = tk.Button(sideBar, text="Saludar", command=lambda:messagebox.showinfo("Saludar", "Saludos Participantes"))
btn_saludar.place(relx=0.5, rely=1/4, anchor="center")  # Posicionamos el botón en el SideBar

btn_advertir = tk.Button(sideBar, text="Advertir", command=lambda:messagebox.showwarning("Cuidado!", "Recuerda enderezar la espalda!"))
btn_advertir.place(relx=0.5, rely=1.5/4, anchor="center")  # Posicionamos el botón en el SideBar

btn_registro = tk.Button(sideBar, text="Registro", command=lambda:mostrar_frame(main, registro))
btn_registro.place(relx=0.5, rely=3/4, anchor="center")  # Posicionamos el botón en el SideBar

# Mostramos el Frame principal en la parte derecha
main.pack(side="right", fill="both", expand=True)

# Añadimos una imagen en el Frame principal
picture = tk.PhotoImage(file="Interfaz Hecha en Clases/Avaina.png").subsample(2, 2)  # Cargamos la imagen y la escalamos
image_label = tk.Label(main, image=picture, width=200, height=200)
image_label.place(relx=0.5, rely=0.5, anchor="center")  # Posicionamos la imagen en el Frame principal

# Añadimos un título en el Frame principal
titulo = tk.Label(main, text="Bienvenido", font=("Arial", 16), bg="#e8e8e8")
titulo.place(relx=0.5, rely=0.1, anchor="center")  # Posicionamos el título en el Frame principal

# Añadimos campos de entrada y etiquetas en el Frame de registro
nombreLabel = tk.Label(registro, text="Nombre", font=("Arial", 16), bg="#e8e8e8")
nombreLabel.place(relx=0.2, rely=0.1, anchor="center")  # Posicionamos la etiqueta "Nombre" en el Frame de registro

nombreInput = tk.Entry(registro)  # Campo de entrada para el nombre
nombreInput.place(relx=0.2, rely=0.2, anchor="center")  # Posicionamos el campo de entrada en el Frame de registro

apellidoLabel = tk.Label(registro, text="Apellido", font=("Arial", 16), bg="#e8e8e8")
apellidoLabel.place(relx=0.6, rely=0.1, anchor="center")  # Posicionamos la etiqueta "Apellido" en el Frame de registro

apellidoInput = tk.Entry(registro)  # Campo de entrada para el apellido
apellidoInput.place(relx=0.6, rely=0.2, anchor="center")  # Posicionamos el campo de entrada en el Frame de registro

# Etiquetas para mostrar los datos ingresados
nombreDato = tk.Label(registro, text="")
nombreDato.place(relx=0.2, rely=0.6, anchor="center")  # Posicionamos la etiqueta para mostrar el nombre en el Frame de registro

apellidoDato = tk.Label(registro, text="")
apellidoDato.place(relx=0.6, rely=0.6, anchor="center")  # Posicionamos la etiqueta para mostrar el apellido en el Frame de registro

# Botón para enviar los datos ingresados
enviar = tk.Button(registro, text="Enviar", command=lambda:escribir(nombreInput, nombreDato, apellidoInput, apellidoDato))
enviar.place(relx=0.9, rely=0.2, anchor="center")  # Posicionamos el botón en el Frame de registro

# Función para capturar los datos ingresados y mostrarlos en las etiquetas correspondientes
def escribir(inputN, outputN, inputA, outputA):
    outputN.config(text=inputN.get())  # Captura y asigna el nombre ingresado
    outputA.config(text=inputA.get())  # Captura y asigna el apellido ingresado

    inputN.delete(0, tk.END)  # Borra el contenido del campo de entrada del nombre
    inputA.delete(0, tk.END)  # Borra el contenido del campo de entrada del apellido

# Inicia el bucle principal de la ventana
root.mainloop()
