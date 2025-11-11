

numeros = [10, 20, 30, 40, 50]

print(f"Total de items del vector:{len(numeros)} ") # obtenemos la dimencion del vector

numeros.append(60)  # agregamos un nuevo item al final del vector
numeros.insert(2, 25)  # agregamos un nuevo item en la posicion 2 del vector

numeros[1:3] = [12, 18]  # modificamos los valores de los items en la posicion 1 y 2

numeros.pop()  # eliminamos el ultimo item del vector
numeros.remove(12) # eliminamos el item con valor 25

numeros.sort()  # ordenamos los items del vector de menor a mayor
numeros.reverse()  # invertimos el orden de los items del vector

numeros.extend([70, 80, 90])  # agregamos varios items al final del vector

numeros_copy = numeros.copy()  # creamos una copia del vector

print(f"Item en la posicion 0: {numeros[::]}")  # accedemos a cada item del vector por su indice

numeros[0] = 100  # modificamos el valor del item en la posicion 0

  # agregamos un nuevo item al final del vector

print(f"Item en la posicion 0: {numeros[0]}")  # accedemos a cada item del vector por su indice

print(f"{numeros}")  # accedemos a cada item del vector por su indice

# for i in numeros:
#     print(f"Item en la posicion {i} ")  # accedemos a cada item del vector por su indice

# print("Usando indice")

# for i in range(len(numeros)):
#     print(f"Item en la posicion {numeros[i]} ")  # accedemos a cada item del vector por su indice

























