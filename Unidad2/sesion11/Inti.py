año = int(input("Ingrese el Año:"))
mes = int(input("Ingrese el Mes:"))
día = int(input("Ingrese el Día:"))
isbiciesto = False
if (año % 4 == 0):
    if (año % 100 == 0):
        if (año % 400 == 0):
            isbiciesto = True
        else:
            isbiciesto = False
    else:
        isbiciesto = True
else:
    isbiciesto = False

if isbiciesto:
    print(f"El Año {año}/{mes}/{día} es bisiesto")
else:
    print(f"El Año {año}/{mes}/{día} no es bisiesto")