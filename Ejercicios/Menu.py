# Para hacer un menu por consola, se hace uso de While
variable = 0
while variable == 0:
    print("Mostrando Lista")
    print("1 - Hamburguesa")
    print("2 - Perros Calientes")
    print("3 - Pizza")

    input("Ingrese el numero de su comida: ") #Solicitamos un dato

    print("Comida Agregada!")

    variable = int( input("Ingrese 0 si su orden no esta lista: ") ) # Solicitamos el valor de variable, para saber si romper el bucle y salir del menu
    # se usa int() para convertir el input (que es un string) a entero

# Con orientacion a objetos este tipo de menus se pueden mejorar e incluso agregar validaciones...
# ...en este ejemplo podemos pedir una comida numero 4 o 5 que no este en el menu, por ej.

#Utilicen este tipo de menu para realizar algunos de los ejercicios que crean convenientes

