#Numero  es multiplo de otro

numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))

if numero1 == 0 :
    print ("error")
elif numero2 % numero1 == 0 :
    print(f"{numero2} es multiplo {numero1}")  
else : 
    print(f"{numero2} no es multiplo {numero1}")     
