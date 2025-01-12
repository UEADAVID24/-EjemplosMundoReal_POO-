# Definir la clase Producto
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_producto(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio}, Cantidad: {self.cantidad}"

# Definir la clase Cliente
class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.reservas = []

    def realizar_reserva(self, producto, cantidad):
        if producto.cantidad >= cantidad:
            producto.cantidad -= cantidad
            reserva = Reserva(self, producto, cantidad)
            self.reservas.append(reserva)
            return f"Reserva realizada para {cantidad} {producto.nombre}(s)."
        else:
            return f"No hay suficiente stock de {producto.nombre}."

# Definir la clase Reserva
class Reserva:
    def __init__(self, cliente, producto, cantidad):
        self.cliente = cliente
        self.producto = producto
        self.cantidad = cantidad
        self.total = self.calcular_total()

    def calcular_total(self):
        return self.cantidad * self.producto.precio

    def mostrar_reserva(self):
        return f"Reserva para {self.cliente.nombre}: {self.cantidad} {self.producto.nombre}(s), Total: ${self.total}"

# Crear instancias de productos
producto1 = Producto("Camiseta", 20, 50)
producto2 = Producto("Pantalón", 30, 30)

# Crear cliente
cliente1 = Cliente("Clinton", "clinton@example.com")

# Realizar una reserva
print(cliente1.realizar_reserva(producto1, 2))  # Reserva para Camiseta
print(cliente1.realizar_reserva(producto2, 5))  # Reserva para Pantalón

# Mostrar las reservas del cliente
for reserva in cliente1.reservas:
    print(reserva.mostrar_reserva())

# Mostrar productos restantes
print(producto1.mostrar_producto())
print(producto2.mostrar_producto())

