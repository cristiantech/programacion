
opcion = int(input(""" 
        Bienevido al sistema de inventario
        Eliga una de las siguientes opciones:
        1. Ingresar un nuevo producto
        2. Ingrese el presio del producto
        3. Eliminar un producto
        4. Salir

 """))

if opcion == 1:
    name_producto = input("Ingrese el nombre del producto: ")
    print(f"El nombre del producto ingresado es: {name_producto}")



