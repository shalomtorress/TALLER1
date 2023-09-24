n1 = float(input("ingrese el primer numero: "))
n2 = float(input("ingrese el segundo numero: "))
n3 = float(input("ingrese el tercer numero: ")) 
mayor = n1
if n1 > mayor:
   mayor = n2
if n3 > mayor:
   mayor = n3

print("el numero mayor es ", mayor)