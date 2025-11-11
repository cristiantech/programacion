palabra = input("Ingrese un nombre cualquiera: ")

palabra_minusculas = palabra.lower()

if palabra_minusculas == palabra_minusculas[::-1]:
    print(f"La palabra {palabra_minusculas} es un palíndromo.")
else:
    print(f"La palabra {palabra_minusculas} no es un palíndromo.")