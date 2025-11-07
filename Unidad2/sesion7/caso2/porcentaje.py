#Datos Iniciales
product_name = "PlayStation"
price_product = 653
IVA = 0.12
discount = 0.10
total=0


price_product += price_product * IVA
print("Precio del producto con iva", price_product)
   


#Calculos


price_product -= price_product * discount
print (f"El precio del producto {product_name} con descuento es: {price_product}")

total = price_product

print(f"el prescio del producto {product_name} es de: {total} ")