anio = int(input("Ingrese el año "))
isbiciesto = anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)
print(f"El año {anio} {'es' if isbiciesto else 'no es'} bisiesto")