class Prenda:
    def __init__(self, nombre, precio, cantidad):
        self._nombre = nombre
        self._precio = precio
        self._cantidad = cantidad
    
    def mostrar_info(self):
        pass
    
    def actualizar_stock(self, cantidad_vendida):
        if cantidad_vendida <= self._cantidad:
            self._cantidad -= cantidad_vendida
            return True
        else:
            print(f"No hay suficiente stock de {self._nombre}")
            return False
    
    def get_precio(self):
        return self._precio
    
    def get_nombre(self):
        return self._nombre
    
    def get_cantidad(self):
        return self._cantidad


class RopaHombre(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self._talla = talla 
    
    def mostrar_info(self):
        print(f"Ropa de Hombre: {self._nombre} - Precio: ${self._precio} - Cantidad: {self._cantidad} - Talla: {self._talla}")


class RopaMujer(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self._talla = talla
    
    def mostrar_info(self):
        print(f"Ropa de Mujer: {self._nombre} - Precio: ${self._precio} - Cantidad: {self._cantidad} - Talla: {self._talla}")


class Inventario:
    def __init__(self):
        self.prendas = [] 
    
    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)
    
    def mostrar_inventario(self):
        if not self.prendas:
            print("El inventario está vacío.")
        else:
            for prenda in self.prendas:
                prenda.mostrar_info()
    
    def buscar_prenda(self, nombre):
        for prenda in self.prendas:
            if prenda.get_nombre().lower() == nombre.lower():
                return prenda
        return None

class Tienda:
    def __init__(self, inventario):
        self.inventario = inventario
    
    def procesar_compra(self, nombre_prenda, cantidad):
        prenda = self.inventario.buscar_prenda(nombre_prenda)
        if prenda:
            if prenda.actualizar_stock(cantidad):
                total = prenda.get_precio() * cantidad
                print(f"Compra realizada: {cantidad} x {prenda.get_nombre()} - Total: ${total}")
            else:
                print(f"No se pudo completar la compra. Stock insuficiente.")
        else:
            print("La prenda no se encuentra en el inventario.")


def iniciar_tienda():
    camisa_hombre = RopaHombre("Camisa de Hombre", 25.00, 50, "M")
    pantalon_hombre = RopaHombre("Pantalón de Hombre", 30.00, 30, "L")
    falda_mujer = RopaMujer("Falda de Mujer", 28.00, 15, "S")
    blusa_mujer = RopaMujer("Blusa de Mujer", 22.00, 40, "M")

    inventario = Inventario()
    inventario.agregar_prenda(camisa_hombre)
    inventario.agregar_prenda(pantalon_hombre)
    inventario.agregar_prenda(falda_mujer)
    inventario.agregar_prenda(blusa_mujer)

    tienda = Tienda(inventario)

    while True:
        print("\n--- Menú de la Tienda ---")
        print("1. Ver Inventario")
        print("2. Comprar Prenda")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- Inventario Disponible ---")
            inventario.mostrar_inventario()

        elif opcion == "2":
            nombre_prenda = input("Ingrese el nombre de la prenda que desea comprar: ")
            cantidad = int(input("Ingrese la cantidad que desea comprar: "))
            tienda.procesar_compra(nombre_prenda, cantidad)

        elif opcion == "3":
            print("Gracias por visitar la tienda. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

iniciar_tienda()
