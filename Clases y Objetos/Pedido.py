class Pedido:
    def __init__(self, persona):
        self.productos = []
        self.total = 0
        self.cant = 0
        self.persona = persona

    def agregarProducto(self,producto):
        self.productos.append(producto)
        self.total += producto.precio
        self.cant += 1

    def eliminarProducto(self, producto):
        self.productos.remove(producto)
        self.total -= producto.precio
        self.cant -= 1

    def mostrarProductos(self):
        for producto in self.productos:
            print(producto.nombre)

    def pedirNumero():
        return input("Numero de Producto")
    
    def darDatos(self):
        self.mostrarProductos()
        print(self.cant)
        print(self.total)

class Productos:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

comprador = Persona("Ezequiel","Rodriguez")

zanahoria = Productos("Zanahoria",2)
papa = Productos("Papa",3)
remolacha = Productos("remolacha",4)

pedido = Pedido(comprador)

pedido.agregarProducto(zanahoria)
pedido.agregarProducto(papa)

pedido.mostrarProductos()
print(pedido.cant)
print(pedido.total)

pedido.eliminarProducto(zanahoria)

pedido.agregarProducto(remolacha)

pedido.darDatos()