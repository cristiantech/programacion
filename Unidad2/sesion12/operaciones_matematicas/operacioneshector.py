
opcion = 0 
menu = menu = """SELECCIONE LA OPERACION QUE QUIERE REALIZAR.
Elija una de la siguientes opciones
1. SUMA
2. RESTA
3. MULTIPLICACION
4. DIVICION
5. REALIZAR OTRA OPERACION
6. Salir
"""
def suma(valora, valorb):
    res = valora + valorb
    print("El resultado de la suma es:", res)
def resta(valora, valorb):
    res = valora - valorb
    print("El resultado de la resta es:", res)  
def multiplicacion(valora, valorb):
    res = valora * valorb
    print("El resultado de la multiplicacion es:", res)
def division(valora, valorb):
    res = valora / valorb
    print("El resultado de la division es:", res)

while(opcion != 6):
    opcion = int(input(menu))

    if opcion == 1:
        numero1 = int(input("Ingrese un numero : "))
        numero2 = int(input("Ingrese un numero : "))
        suma(numero1, numero2)
    elif opcion == 2: 
        numero1 = int(input("Ingrese un numero : "))
        numero2 = int(input("Ingrese un numero : "))
        resta(numero1, numero2)
    elif opcion == 3: 
        numero1 = int(input("Ingrese un numero : "))
        numero2 = int(input("Ingrese un numero : "))
        multiplicacion(numero1, numero2)
    elif opcion == 4: 
        numero1 = int(input("Ingrese un numero : "))
        numero2 = int(input("Ingrese un numero : "))
        division(numero1, numero2)   
     
  



