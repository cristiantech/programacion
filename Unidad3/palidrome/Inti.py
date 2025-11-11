
nombre = input("Ingrese un nombre: ")
nombre = nombre.lower()
coincide = 0
for i in range(len(nombre)):
    if nombre[i] == nombre[len(nombre) - 1 - i]:
        coincide += 1

if coincide == len(nombre):
    print("El nombre es un palíndromo.")
else:
    print("El nombre no es un palíndromo.")
