#Solicitamos los números con los cuales vamos a trabajar
numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))
numero3 = float(input("Ingrese el tercer numero: "))

#Evaluamos si todos son iguales. Mostramos que son iguales en caso positivo
if numero1 == numero2 and numero1 == numero3: 
    print("Los números ingresados son iguales")
else:
    #Evaluamos si numero1 es mayor a los otros 2. Lo mostramos en caso positivo
    if numero1 >= numero2 and numero1 >= numero3: 
        print(f"El numero mayor es {numero1}")

    #Evaluamos si numero2 es mayor a los otros 2. Lo mostramos en caso positivo
    elif numero2 >= numero3 and numero2 >= numero1: 
        print(f"El número mayor es {numero2}")

    #Caso contrario el numero 3 es el mayor y lo mostramos
    else:                                            
        print(f"El número mayor es {numero3}")   