# El orden es importante
cuenta_bancaria = 0
deposito = 500
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


retiro=300

if retiro >= 300:
    cuenta_bancaria -= (retiro * 0.01)

cuenta_bancaria -= retiro
print("El total retirado fue: ",retiro)
print("El balance actual de la cuenta es: ",cuenta_bancaria)      

