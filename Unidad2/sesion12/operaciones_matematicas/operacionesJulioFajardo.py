def operacion(valor1,valor2,operacion):
    if operacion == 1:
        print(f"El resultado de la suma es: {valor1+valor2}")
    elif operacion == 2:
        print(f"El resultado de la resta es: {valor1-valor2}")
    elif operacion == 3:
        print(f"El resultado de la multiplicacion es: {valor1*valor2}")
    elif operacion == 4:
        try:
            print(f"El resultado de la división es: {valor1/valor2}")
        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero.")
        # if valor2 != 0:
        #     print(f"El resultado de la división es: {valor1/valor2}")
        # else:
        #     print("El divisor no puede ser cero.")    




# print("=====MENU OPERACIONES MATEMATICAS ====")
# print("Seleccione la operación matemática a realizar:")
# print("1. Suma \n 2. Resta \n 3. Multiplicacion \n 4. División \n 5. Salir")
opcion = 0 #int(input("Elija una opcion (1-5): "))
repetir_bucle=True

while opcion != 5 and repetir_bucle  :
    print("=====MENU OPERACIONES MATEMATICAS ====")
    print("Seleccione la operación matemática a realizar:")
    print("1. Suma \n2. Resta \n3. Multiplicacion \n4. División \n5. Salir")
    opcion = int(input("Elija una opcion (1-5): "))
    
    if opcion == 1:
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        operacion(numero1,numero2,opcion)
    elif opcion == 2:
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        operacion(numero1,numero2,opcion)
    elif opcion == 3:
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        operacion(numero1,numero2,opcion)
    elif opcion == 4:
        numero1 = float(input("Ingrese el dividendo: "))
        numero2 = float(input("Ingrese el divisor: "))
        operacion(numero1,numero2,opcion)
    elif opcion == 5:
        print("===PROGRAMA FINALIZADO===")
        break    
    else:
        print("Operacion Seleccionada no válida.")
    if int(input("Desea realizar una operación adicional, 1-Si 2-No: ")) == 2:
        repetir_bucle=False