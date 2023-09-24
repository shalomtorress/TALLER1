# Taller 1 
## Equipo alfa buena maravilla onda dinamita escuadrón lobo



## Punto 1 
pantallazo quiz de python 

![image.png](https://github.com/shalomtorress/TALLER1/blob/main/image.png)

## Punto 2
Programa que lea tres números reales y determine cuál es el mayor

**leer documento:** punto2.py
```pseudocode
n1 = float(input("ingrese el primer numero: "))
n2 = float(input("ingrese el segundo numero: "))
n3 = float(input("ingrese el tercer numero: ")) 
mayor = n1
if n1 > mayor:
   mayor = n2
if n3 > mayor:
   mayor = n3

print("el numero mayor es ", mayor)
```
Declaramos las variables ```n1, n2 y n3``` para poner los números reales, inicializamos la variable```mayor``` con n1, comparamos cada numero con el mayor (n1), si el numero es mayor que el mayor que ya esta se asigna como el nuevo mayor
## Punto 3 
Prograna que determina si un numero es par o impar 
**Leer documento:** punto3.ipynb
```pseudocode
n = int(input("Ingrese un número entero: "))
if n % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")
```
declaramos la variable ```n``` para poner el numero, el operador ```%``` determina si el numero es divisible por 2, si es divisible por 2 es par si no es impar 
## Punto 4
programa que lea dos números reales y determine si el primero es múltiplo del segundo
**Leer documento:** punto4.py
```pseudocode
n1 = float(input("ingrese el primer numero: "))
n2 = float(input("ingrese el segundo numero: "))
if n1 % n2 == 0:
   print("el primer numero es multiplo del segundo")
else:
   print("el prmer numero no es multiplo del segundo")
```
declaramos las varables ```n1 y n2``` para poner los numeros, usamos el operador ```%``` para saber si el resto de la la division entre n1 y n2 es 0, si el resto es 0, el primero es multiplo del segundo, si el resto no es 0 entonces el primero no es multiplo del segundo

