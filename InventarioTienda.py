# Programa de una tienda
class InventarioTienda:
    def __init__(self, nom_tienda):
        self.nom_tienda = nom_tienda
        self.productos = []  # lista vacía de productos


    def agregar_producto(self, nombre, precio, cantidad): # Método 1
        if precio <= 0 or cantidad <= 0: # Valida que precio y cantidad sean positivos
            print('El precio y la cantidad deben ser valores positivos')
            return
        producto = {'nombre': nombre, 'precio': precio, 'cantidad': cantidad} # Crea un diccionario con los datos del producto
        self.productos.append(producto) # Lo agrega (append) a la lista de producto
        print(f"✅ Producto '{nombre}' agregado al inventario")


    def vender_producto(self, nombre, cantidad):
        for producto in self.productos:
            if producto['nombre'].lower() == nombre.lower(): # Busca el producto por nombre (sin importar mayúsculas o minúsculas)
                if cantidad <= 0: # Revisa que la cantidad a vender sea positiva
                    print("La cantidad a vender debe ser positiva")
                    return
                if producto['cantidad'] >= cantidad:
                    producto['cantidad'] -= cantidad
                    print(f"Venta realizada: {cantidad} de '{nombre}'") # Si hay suficiente stock -> lo descuenta
                    if producto['cantidad'] == 0:
                        print(f"El producto '{nombre}' se ha agotado")
                    return
                else:
                    print('No hay suficiente stock disponible')
                    return
        print('El producto no existe en el inventario') # Si no hay suficiente, o no existe -> muestra error


    def mostrar_inventario(self):
        if not self.productos:
            print('El inventario está vacío') # Si la lista está vacía, dice que no hay productos
        else:
            print('\n--- Inventario de la tienda ---')
            for producto in self.productos: # Si hay productos, los muestra uno por uno: 
                print(f"Nombre: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")


    def producto_mas_caro(self):
        if not self.productos:
            print('No hay productos en el inventario')
            return
        producto_caro = max(self.productos, key=lambda p: p["precio"]) # Usa max para buscar el producto con mayor precio en la lista
        print(f"El producto más caro es '{producto_caro['nombre']}' con un precio de ${producto_caro['precio']}")
        # Muestra su nombre y precio



# Programa principal
def menu():
    tienda = InventarioTienda('Mi tiendita') # Crea un objeto tienda

    while True: # Con while True se mantiene el programa corriendo hasta que el usuario elija salir
        print('\n--- Menú ---')
        print('1. Agregar producto')
        print('2. Vender producto')
        print('3. Ver inventario')
        print('4. Consultar producto más caro')
        print('5. Salir')
        
        opcion = input('Seleccione una opción: ')

        if opcion == '1': # Opción 1: Solicita nombre, precio y cantidad -> llama a agregar_producto
            nombre = input('Ingresa el nombre del producto: ')
            try:
                precio = float(input('Ingresa el precio: '))
                cantidad = int(input('Ingresa la cantidad: '))
                tienda.agregar_producto(nombre, precio, cantidad)
            except ValueError:
                print('Entrada inválida. Intenta nuevamente.')

        elif opcion == '2': # Opción 2: Solicita nombre y cantidad -> llama a vender_producto
            nombre = input('Ingresa el nombre del producto a vender: ')
            try:
                cantidad = int(input('Ingresa la cantidad a vender: '))
                tienda.vender_producto(nombre, cantidad)
            except ValueError:
                print('Entrada inválida. Intenta nuevamente.')

        elif opcion == '3': # Opción 3: Muestra el inventario
            tienda.mostrar_inventario()

        elif opcion == '4': # Opción 4: Muestra el producto más caro
            tienda.producto_mas_caro()

        elif opcion == '5': # Opción 5: Sale del programa
            print('Saliendo del programa... adiós 👋')
            break
        else:
            print('Opción no válida, intenta nuevamente.')


# Ejecutar programa
if __name__ == "__main__":
    menu()
