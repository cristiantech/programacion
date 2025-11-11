opcion = 0
menu = """Seleccione el tipo de operación que desea realizar

1. Suma
2. Resta
3. Multiplicación
4. División
5. Salir
"""

def suma(valora, valorb):
    res = valora + valorb
    print("El resultado de la suma es:", res)

def resta(valora, valorb):
    res = valora - valorb
    print("El resultado de la resta es:", res)

def multiplicar(valora, valorb):
    res = valora * valorb
    print("El resultado de la multiplicación es:", res)

def dividir(valora, valorb):
    try:
        res = valora / valorb
        print("El resultado de la división es:", res)
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")

while (opcion !=5):
    opcion = int(input(menu))

    if opcion == 1:
        numero1 = int(input("Ingrese el primer número: "))
        numero2 = int(input("Ingrese el segundo número: "))
        suma(numero1, numero2)

        opcion = int(input("Desea realizar otra operación? (1=si): "))
        
    elif opcion == 2:
        numero1 = int(input("Ingrese el primer número:"))
        numero2 = int(input("Ingrese el segundo número:"))
        resta(numero1, numero2)

        opcion = int(input("Desea realizar otra operación? (1=si): "))

    elif opcion == 3:
        numero1 = int(input("Ingrese el primer número:"))
        numero2 = int(input("Ingrese el primer número:"))
        multiplicar(numero1, numero2)

        opcion = int(input("Desea realizar otra operación? (1=si): "))
    
    elif opcion == 4:
        numero1 = int(input("Ingrese el primer número:"))
        numero2 = int(input("Ingrese el primer número:"))
        dividir(numero1, numero2)

        opcion = int(input("Desea realizar otra operación? (1=si): "))
print("Gracias por usar la calculadora")