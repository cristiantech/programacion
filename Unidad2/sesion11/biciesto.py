anio = 2027
mes = 2 
dia = 29
isbiciesto = False
if (anio % 4 == 0):
    if (anio % 100 == 0):
        if (anio % 400 == 0):
            isbiciesto = True
        else:
            isbiciesto = False
    else:
        isbiciesto = True
else:
    isbiciesto = False

if isbiciesto:
    print(f"El año {anio} es bisiesto")
else:
    print(f"El año {anio} no es bisiesto")