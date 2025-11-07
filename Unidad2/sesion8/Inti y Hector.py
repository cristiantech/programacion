# Cuenta bancaria
cuenta_bancaria = 0
deposito = 200
retiro = 0

opcion = int(input("""
    Bienvenido a su banca movil, 
    Eliga una de las siguiente opciones:
    1. Deposito
    2. Retiro
    3. Salir
    """))

if opcion == 1:
    print(f"Ingrese la cantidad del deposito:",{deposito})
    print(f"El monto de su cuenta es de:",{cuenta_bancaria})

if deposito >= 500:
    cuenta_bancaria += deposito
    cuenta_bancaria += cuenta_bancaria * 0.05
    print("Deposito realizado es:", cuenta_bancaria)


deposito = 300

if deposito >= 500:
    cuenta_bancaria += deposito
    cuenta_bancaria += cuenta_bancaria * 0.05
    print("Deposito realizado es:", cuenta_bancaria)


cuenta_bancaria += deposito
print("Deposito realizado es:", cuenta_bancaria)

retiro = 300

if retiro >= 1000:
    cuenta_bancaria -= retiro
    cuenta_bancaria -= cuenta_bancaria*0.02
    
print("retiro realizado es",cuenta_bancaria )