numero_escritorios = int(input("Ingrese el número de escritorios comprados: "))
valor_escritorio = 650000

subtotal = valor_escritorio*numero_escritorios

if numero_escritorios < 5:
    print(f"El valor a pagar es: {subtotal-(subtotal*0.1)}")
elif numero_escritorios >= 5 and numero_escritorios < 10:
    print(f"El valor a pagar es: {subtotal-(subtotal*0.2)}")
elif numero_escritorios >=10:
    print(f"El valor a pagar es: {subtotal-(subtotal*0.4)}")