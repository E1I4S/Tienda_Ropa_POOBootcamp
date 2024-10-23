class Producto:
    def __init__(self, nombre, precio, cantidad):
        self._nombre = nombre
        self._precio = precio
        self._cantidad = cantidad

    def mostrar_info(self):
        pass

    def get_precio(self):
        return self._precio

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def actualizar_stock(self, cantidad_vendida):
        if cantidad_vendida <= self._cantidad:
            self._cantidad -= cantidad_vendida
            return True
        else:
            print(f"No hay suficiente stock de {self._nombre}.")
            return False


class Ropa(Producto):
    def __init__(self, nombre, precio, cantidad, talla, tipo_tela):
        super().__init__(nombre, precio, cantidad)
        self._talla = talla 
        self._tipo_tela = tipo_tela 

    def mostrar_info(self):
        print(f"{self.get_nombre()} - Precio: ${self.get_precio()} - Cantidad: {self.get_cantidad()} - Talla: {self._talla} - Tela: {self._tipo_tela}")


class Camisa(Ropa):
    def __init__(self, nombre, precio, cantidad, talla, tipo_tela):
        super().__init__(nombre, precio, cantidad, talla, tipo_tela)

    def mostrar_info(self):
        print(f"Camisa: {self.get_nombre()} - Precio: ${self.get_precio()} - Cantidad: {self.get_cantidad()} - Talla: {self._talla} - Tela: {self._tipo_tela}")


class Pantalon(Ropa):
    def __init__(self, nombre, precio, cantidad, talla, tipo_tela):
        super().__init__(nombre, precio, cantidad, talla, tipo_tela)

    def mostrar_info(self):
        print(f"Pantalón: {self.get_nombre()} - Precio: ${self.get_precio()} - Cantidad: {self.get_cantidad()} - Talla: {self._talla} - Tela: {self._tipo_tela}")


class Zapato(Ropa):
    def __init__(self, nombre, precio, cantidad, talla, material):
        super().__init__(nombre, precio, cantidad, talla, material)

    def mostrar_info(self):
        print(f"Zapato: {self.get_nombre()} - Precio: ${self.get_precio()} - Cantidad: {self.get_cantidad()} - Talla: {self._talla} - Material: {self._tipo_tela}")


class Carrito:
    def __init__(self):
        self._productos = [] 

    def agregar_producto(self, producto, cantidad):
        if producto.actualizar_stock(cantidad):
            self._productos.append((producto, cantidad))

    def calcular_total(self):
        total = sum(producto.get_precio() * cantidad for producto, cantidad in self._productos)
        return total

    def mostrar_resumen(self):
        print("\n--- Resumen de Compra ---")
        for producto, cantidad in self._productos:
            print(f"{cantidad} x {producto.get_nombre()} - Precio Unitario: ${producto.get_precio()} - Total: ${producto.get_precio() * cantidad}")
        print(f"Total a pagar: ${self.calcular_total()}")

class Tienda:
    def __init__(self):
        self.inventario = [] 

    def agregar_producto(self, producto):
        self.inventario.append(producto)

    def mostrar_inventario(self):
        print("\n--- Inventario Disponible ---")
        for producto in self.inventario:
            producto.mostrar_info()

    def procesar_compra(self):
        carrito = Carrito()
        while True:
            self.mostrar_inventario()
            nombre_prenda = input("Ingrese el nombre de la prenda que desea comprar (o 'salir' para finalizar): ")
            if nombre_prenda.lower() == 'salir':
                break
            cantidad = int(input("Ingrese la cantidad que desea comprar: "))
            producto = next((p for p in self.inventario if p.get_nombre().lower() == nombre_prenda.lower()), None)
            if producto:
                carrito.agregar_producto(producto, cantidad)
            else:
                print("La prenda no se encuentra en el inventario.")

        carrito.mostrar_resumen()


def iniciar_tienda():
    camisa1 = Camisa("Camisa de Hombre", 25.00, 50, "M", "Algodón")
    pantalon1 = Pantalon("Pantalón de Hombre", 30.00, 30, "L", "Denim")
    zapato1 = Zapato("Zapato de Hombre", 60.00, 25, "42", "Cuero")
    camisa2 = Camisa("Blusa de Mujer", 22.00, 40, "M", "Poliéster")
    pantalon2 = Pantalon("Falda de Mujer", 28.00, 15, "S", "Seda")

    tienda = Tienda()
    tienda.agregar_producto(camisa1)
    tienda.agregar_producto(pantalon1)
    tienda.agregar_producto(zapato1)
    tienda.agregar_producto(camisa2)
    tienda.agregar_producto(pantalon2)

    tienda.procesar_compra()


iniciar_tienda()
