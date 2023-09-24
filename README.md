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
## Punto 5 
programa que lea tres números reales y determine si la suma de los dos primeros es mayor, menor o igual que el tercer número
**leer documento:** punto5.ipynt
```pseudocode
n1 = float(input("ingrese el primer numero "))
n2 = float(input("ingrese el segundo numero "))
n3 = float(input("ingrese el tercer numero "))
suma= n1 + n2
if suma > n3: 
   print("la suma de los dos primeros numeros es mayor que el tercero")
elif suma < n3:
   print("la suma de los dos primeros numeros es menor que el tercero") 
else:
   print("la suma de los dos prmeros numeros es gual que el tercero")
```
Declaramos las variables ```n1, n2 y n3```para poner los numeros, inicializamos la variable ```suma``` con ```n1+n2```, comparamos la suma con el tercer numero, si la suma es mayor, menor o igual arrojara el mensaje correspondiete 
## Punto 6
Programa que al ingresar una letra diga si es consonante o vocal 
**leer documento:** punto6.py
```pseudocode
letra = input("ingrese una letra: ")
if letra in "aeiou":
    print("la letra es una vocal")
else:
    print("la letra es una consonante")
```
Declaramos la variable ```letra``` para poner la letra, utilizamos ```in``` para saber si la letra esta en la lista de las vocales (aeiou), si la letra esta en a lista la letra es una vocal, si laletra no esta en la lista la letra es una consonante 
