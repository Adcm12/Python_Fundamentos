# Utiliza la biblioteca sqlite3 para crear una base de datos llamada "almacen.db".
# Crea una tabla llamada "Productos" con los siguientes campos: id, nombre, precio y cantidad.
# Crea una clase llamada "Producto".
# Crea los atributos id, nombre, precio y cantidad en la clase Producto. Implementa el constructor __init__() para recibir los valores de los atributos.
# Crea métodos getters (get_id(), get_nombre(), get_precio(), get_cantidad()) para acceder a los valores de los atributos.
# Crea métodos setters (set_nombre(), set_precio(), set_cantidad()) para establecer los valores de los atributos.

# Crea un método estático en la clase Producto llamado crear_producto() que acepte los valores de nombre, precio y cantidad como parámetros. Este método debe crear una instancia de la clase Producto con los valores proporcionados e insertar un registro en la tabla "Productos".
# Crea un método estático llamado buscar_producto_por_id() que acepte un ID como parámetro y retorne una instancia de Producto con los valores correspondientes de la tabla "Productos".
# Crea un método estático llamado listar_productos() que consulte la tabla "Productos" y retorne una lista de instancias de Producto.
# Crea un bucle principal que muestre un menú al usuario con opciones como "Agregar Producto", "Buscar Producto por ID", "Listar Productos" y "Salir". Implementa la lógica para cada opción del menú, llamando a los métodos correspondientes de la clase Producto.
# En la opción "Agregar Producto", solicita al usuario ingresar nombre, precio y cantidad, y luego llama al método crear_producto().
# En la opción "Buscar Producto por ID", pide al usuario que ingrese un ID y muestra los detalles del producto correspondiente utilizando el método buscar_producto_por_id().
# En la opción "Listar Productos", muestra todos los productos utilizando el método listar_productos().
# Al salir del bucle principal, cierra la conexión con la base de datos.

import sqlite3
import os

conexion = sqlite3.connect('almacen.db')
cursor = conexion.cursor()

cursor.execute('''Create Table if not exists Productos
               (id Integer,
               Nombre Text(40),
               Precio Real,
               Cantidad Integer);''')

print('Base de datos creada con exito!!!')

class Productos():

    def __init__(self, id,  nombre, precio, cantidad):

        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def get_id(self):

        return self.id

    def get_nombre(self):

        return self.nombre

    def get_precio(self):

        return self.precio

    def get_cantidad(self):

        return self.cantidad

    def setters_id(self, id_novo):

        self.id = id_novo

    def setters_nombre(self, nombre_novo):

        self.nombre = nombre_novo

    def setters_precio(self, precio_novo):

        self.precio = precio_novo

    def setters_cantidad(self, cantidad_nova):

        self.cantidad = cantidad_nova

    @staticmethod
    def crear_producto(id, nombre, precio, cantidad):
        
        producto = Productos(id, nombre, precio, cantidad)

        conexion = sqlite3.connect('almacen.db')
        cursor = conexion.cursor()

        cursor.execute('''Insert Into Productos
                       Values (?, ?, ?, ?)''', (id, nombre, precio, cantidad))
        
        conexion.commit()
        conexion.close()
        print('\nProducto inserido con exito!!!')

    def buscar_producto_por_id(id):

        producto = Productos(id, nombre, precio, cantidad)

        conexion = sqlite3.connect('almacen.db')
        cursor = conexion.cursor()

        cursor.execute('SELECT * FROM Productos WHERE id = ?', (id))
        cursor.fetchone()
        conexion.close()

        if cursor:
            id, nombre, precio, cantidad = producto
            return Productos(id, nombre, precio, cantidad)
        
        else:
            return None

    def listar_productos(id, nombre, precio, cantidad):

        conexion = sqlite3.connect('almacen.db')
        cursor = conexion.cursor()

        cursor.execute('SELECT * FROM Productos')
        cursor.fetchall()
        conexion.close()

        if cursor:

            id, nombre, precio, cantidad = cursor
            return Productos(id, nombre, precio, cantidad)
        
        else:
            return None
        

if __name__ == '__main__':
    os.system('cls')

    try:            
        while True:

            menu = int(input('\n Menu \n1 - Crear producto  \n2 - Buscar producto por id  \n3 - Listar productos  \n4 - Salir \nEscoje una ipcion: '))

            if menu == 1: 

                id = int(input('Ingresa el id del producto: '))
                nombre = input('Ingresa el nombre del producto: ')
                valor = float(input('Ingresa el valor del producto: '))
                cantidad = int(input('Ingresa la cantidad del producto: '))

                Productos.crear_producto(id, nombre, valor, cantidad)

            elif menu == 2:

                id = int(input('Ingresa el id del producto: '))
                Productos.buscar_producto_por_id(id)                



    except Exception as e:
        print(f'Ocurrió un error: {str(e)}')       