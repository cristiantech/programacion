# El orden es importante
cuenta_bancaria = 0
deposito = 200
retiro = 50


if deposito >= 200:
    cuenta_bancaria += deposito
    cuenta_bancaria += cuenta_bancaria * 0.03
    print("Deposito realizado es:", cuenta_bancaria)


deposito = 100

if deposito >= 200:
    cuenta_bancaria += deposito
    cuenta_bancaria += cuenta_bancaria * 0.03
    print("Deposito realizado es:", cuenta_bancaria)


cuenta_bancaria += deposito
print("Deposito realizado es:", cuenta_bancaria)