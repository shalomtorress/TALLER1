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
## Punto 7
programa que pida 5 números reales y calcule las siguientes operaciones:
  + El promedio
  + La mediana 
  + El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
  + Ordenar los números de forma ascendente
  + Ordenar los números de forma descendente
  + La potencia del mayor número elevado al menor número
  + La raíz cúbica del menor número
**leer documento:** yanodoymas.ipynt
```pseudocode
primer_numero = float(input("Ingrese primer numero "))
segundo_numero = float(input("Ingrese segundo numero "))
tercer_numero = float(input("Ingrese tercer numero "))
cuarto_numero = float(input("Ingrese cuarto numero "))
quinto_numero = float(input("Ingrese quinto numero "))

#Hallar el promedio
suma_numeros = float(primer_numero + segundo_numero + tercer_numero + cuarto_numero + quinto_numero)
promedio = float(suma_numeros / 5)
print("El promedio es:" +str (promedio))

#Hallar la mediana 
if segundo_numero>tercer_numero>primer_numero>cuarto_numero>quinto_numero:
    print("la media es:" +str(primer_numero))
elif segundo_numero>tercer_numero>primer_numero>quinto_numero>cuarto_numero:
    print("la media es:" +str(primer_numero))
elif tercer_numero>segundo_numero>primer_numero>cuarto_numero>quinto_numero:
    print("la media es:" +str(primer_numero))
elif tercer_numero>segundo_numero>primer_numero>quinto_numero>cuarto_numero:
    print("la media es" +str(primer_numero))
elif segundo_numero>cuarto_numero>primer_numero>tercer_numero>quinto_numero:
    print("la media es "+str(primer_numero))
elif segundo_numero>cuarto_numero>primer_numero>quinto_numero>tercer_numero:
    print("la media es" +str(primer_numero))
elif cuarto_numero>segundo_numero>primer_numero>quinto_numero>tercer_numero:
    print("la media es" +str(primer_numero))
elif cuarto_numero>segundo_numero>primer_numero>tercer_numero>quinto_numero:
    print("la media es" +str(primer_numero))
elif segundo_numero>quinto_numero>primer_numero>cuarto_numero>tercer_numero:
    print("la media es " +str(primer_numero))
elif segundo_numero>quinto_numero>primer_numero>tercer_numero>cuarto_numero:
    print("la meda es" +str(primer_numero))
elif quinto_numero>segundo_numero>primer_numero>tercer_numero>cuarto_numero:
    print("la media es" +str(primer_numero))
elif quinto_numero>segundo_numero>primer_numero>cuarto_numero>tercer_numero:
    print("la media es" +str(primer_numero))
elif tercer_numero>cuarto_numero>primer_numero>segundo_numero>quinto_numero:
    print("la media es"+str(primer_numero))
elif tercer_numero>cuarto_numero>primer_numero>quinto_numero>segundo_numero:
    print("la media es" +str(primer_numero))
elif cuarto_numero>tercer_numero>primer_numero>quinto_numero>segundo_numero:
    print("la media es" +str(primer_numero))
elif cuarto_numero>tercer_numero>primer_numero>segundo_numero>quinto_numero:
    print("la media es" +(primer_numero))
elif tercer_numero>quinto_numero>primer_numero>cuarto_numero>segundo_numero:
    print("la media es" +str(primer_numero))
elif tercer_numero>quinto_numero>primer_numero>segundo_numero>cuarto_numero:
    print("la media es" +str(primer_numero))
elif quinto_numero>tercer_numero>primer_numero>segundo_numero>cuarto_numero:
    print("la media es" +str(primer_numero))
elif quinto_numero>tercer_numero>primer_numero>cuarto_numero>segundo_numero:
    print("la media es" +str(primer_numero))
elif cuarto_numero>quinto_numero>primer_numero>tercer_numero>segundo_numero:
    print("la media es" +str(primer_numero))
elif cuarto_numero>quinto_numero>primer_numero>segundo_numero>tercer_numero:
    print("la media es" +str(primer_numero))
elif quinto_numero>cuarto_numero>primer_numero>segundo_numero>tercer_numero:
    print("la media es" +str(primer_numero))
elif quinto_numero>cuarto_numero>primer_numero>tercer_numero>segundo_numero:
    print("la media es" +str(primer_numero))
elif primer_numero>tercer_numero>segundo_numero>cuarto_numero>quinto_numero:
    print("la media es" +str(segundo_numero))
elif primer_numero>tercer_numero>segundo_numero>quinto_numero>cuarto_numero:
    print("la media es" +str(segundo_numero))
elif tercer_numero>primer_numero>segundo_numero>quinto_numero>cuarto_numero:
    print("la media es" +str(segundo_numero))
elif tercer_numero>primer_numero>segundo_numero>cuarto_numero>quinto_numero:
    print("la media es" +str(segundo_numero))
elif primer_numero>cuarto_numero>segundo_numero>tercer_numero>quinto_numero:
    print("la media es "+str(segundo_numero))
elif primer_numero>cuarto_numero>segundo_numero>quinto_numero>tercer_numero:
    print("la media es" +str(segundo_numero))
elif cuarto_numero>primer_numero>segundo_numero>quinto_numero>tercer_numero:
    print("la media es" +str(segundo_numero))
elif cuarto_numero>primer_numero>segundo_numero>tercer_numero>quinto_numero:
    print("la media es" +str(segundo_numero))
elif primer_numero>quinto_numero>segundo_numero>cuarto_numero>tercer_numero:
    print("la media es" +str(segundo_numero))
elif primer_numero>quinto_numero>segundo_numero>tercer_numero>cuarto_numero:
    print("la media es" +str(segundo_numero))
elif quinto_numero>primer_numero>segundo_numero>tercer_numero>cuarto_numero:
    print("la media es" +str(segundo_numero))
elif quinto_numero>primer_numero>segundo_numero>cuarto_numero>tercer_numero:
    print("la media es" +str(segundo_numero))
elif tercer_numero>cuarto_numero>segundo_numero>primer_numero>quinto_numero:
    print("la media es" +str(segundo_numero))
elif tercer_numero>cuarto_numero>segundo_numero>quinto_numero>primer_numero:
    print("la media es" +str(segundo_numero))
elif cuarto_numero>tercer_numero>segundo_numero>primer_numero>quinto_numero:
    print("la media es" +str(segundo_numero))
elif cuarto_numero>tercer_numero>segundo_numero>quinto_numero>primer_numero:
    print("la media es" +str(segundo_numero))
elif tercer_numero>quinto_numero>segundo_numero>cuarto_numero>primer_numero:
    print("la media es" +str(segundo_numero))
elif tercer_numero>quinto_numero>segundo_numero>primer_numero>cuarto_numero:
    print("la meidia es" +str(segundo_numero))
elif cuarto_numero>quinto_numero>segundo_numero>tercer_numero>primer_numero:
    print("la media es" +str(segundo_numero))
elif cuarto_numero>quinto_numero>segundo_numero>primer_numero>tercer_numero:
    print("la meda es" +str(segundo_numero))
elif quinto_numero>cuarto_numero>segundo_numero>primer_numero>tercer_numero:
    print("la media es" +str(segundo_numero))
elif quinto_numero>cuarto_numero>segundo_numero>tercer_numero>primer_numero:
    print("la media es" +str(segundo_numero))
elif primer_numero>segundo_numero>tercer_numero>cuarto_numero>quinto_numero:
    print("la media es" +str(tercer_numero))
elif primer_numero>segundo_numero>tercer_numero>quinto_numero>cuarto_numero:
    print("la media es" +str(tercer_numero))
elif segundo_numero>primer_numero>tercer_numero>quinto_numero>cuarto_numero:
    print("la media es" +str(tercer_numero))
elif segundo_numero>primer_numero>tercer_numero>cuarto_numero>quinto_numero:
    print("la media es"+str(tercer_numero))
elif primer_numero>cuarto_numero>tercer_numero>quinto_numero>segundo_numero:
    print("la media es"+str(tercer_numero))
elif primer_numero>cuarto_numero>tercer_numero>segundo_numero>quinto_numero:
    print("la media es"+str(tercer_numero))
elif cuarto_numero>primer_numero>tercer_numero>segundo_numero>quinto_numero:
    print("la media es"+str(tercer_numero))
elif cuarto_numero>primer_numero>tercer_numero>quinto_numero>segundo_numero:
    print("la media es"+str(tercer_numero))
elif primer_numero>quinto_numero>tercer_numero>cuarto_numero>segundo_numero:
    print("la media es"+str(tercer_numero))
elif primer_numero>quinto_numero>tercer_numero>segundo_numero>cuarto_numero:
    print("la media es"+str(tercer_numero))
elif quinto_numero>primer_numero>tercer_numero>segundo_numero>cuarto_numero:
    print("la media es"+str(tercer_numero))
elif quinto_numero>primer_numero>tercer_numero>cuarto_numero>segundo_numero:
    print("la media es"+str(tercer_numero))
elif segundo_numero>cuarto_numero>tercer_numero>quinto_numero>primer_numero:
    print("la media es"+str(tercer_numero))
elif segundo_numero>cuarto_numero>tercer_numero>primer_numero>quinto_numero:
    print("la media es"+str(tercer_numero))
elif cuarto_numero>segundo_numero>tercer_numero>primer_numero>quinto_numero:
    print("la media es"+str(tercer_numero))
elif cuarto_numero>segundo_numero>tercer_numero>quinto_numero>primer_numero:
    print("la media es"+str(tercer_numero))
elif segundo_numero>quinto_numero>tercer_numero>primer_numero>cuarto_numero:
    print("la media es"+str(tercer_numero))
elif segundo_numero>quinto_numero>tercer_numero>cuarto_numero>primer_numero:
    print("la media es"+str(tercer_numero))
elif quinto_numero>segundo_numero>tercer_numero>primer_numero>cuarto_numero:
    print("la media es"+str(tercer_numero))
elif quinto_numero>segundo_numero>tercer_numero>cuarto_numero>primer_numero:
    print("la media es"+str(tercer_numero))
elif cuarto_numero>quinto_numero>tercer_numero>segundo_numero>primer_numero:
    print("la media es"+str(tercer_numero))
elif cuarto_numero>quinto_numero>tercer_numero>primer_numero>segundo_numero:
    print("la media es"+str(tercer_numero))
elif quinto_numero>cuarto_numero>tercer_numero>segundo_numero>primer_numero:
    print("la media es"+str(tercer_numero))
elif quinto_numero>cuarto_numero>tercer_numero>primer_numero>segundo_numero:
    print("la media es"+str(tercer_numero))
elif primer_numero>segundo_numero>cuarto_numero>tercer_numero>quinto_numero:
    print("la media es"+str(cuarto_numero))
elif primer_numero>segundo_numero>cuarto_numero>quinto_numero>tercer_numero:
     print("la media es"+str(cuarto_numero))
elif segundo_numero>primer_numero>cuarto_numero>quinto_numero>tercer_numero:
     print("la media es"+str(cuarto_numero))
elif segundo_numero>primer_numero>cuarto_numero>tercer_numero>quinto_numero:
     print("la media es"+str(cuarto_numero))
elif primer_numero>tercer_numero>cuarto_numero>quinto_numero>segundo_numero:
     print("la media es"+str(cuarto_numero))
elif primer_numero>tercer_numero>cuarto_numero>segundo_numero>quinto_numero:
      print("la media es"+str(cuarto_numero))
elif tercer_numero>primer_numero>cuarto_numero>quinto_numero>segundo_numero:
     print("la media es"+str(cuarto_numero))
elif tercer_numero>primer_numero>cuarto_numero>segundo_numero>quinto_numero:
     print("la media es"+str(cuarto_numero))
elif primer_numero>quinto_numero>cuarto_numero>segundo_numero>tercer_numero:
     print("la media es"+str(cuarto_numero))
elif primer_numero>quinto_numero>cuarto_numero>tercer_numero>segundo_numero:
     print("la media es"+str(cuarto_numero))
elif quinto_numero>primer_numero>cuarto_numero>segundo_numero>tercer_numero:
     print("la media es"+str(cuarto_numero))
elif quinto_numero>primer_numero>cuarto_numero>tercer_numero>segundo_numero:
     print("la media es"+str(cuarto_numero))
elif tercer_numero>segundo_numero>cuarto_numero>quinto_numero>primer_numero:
     print("la media es"+str(cuarto_numero))
elif tercer_numero>segundo_numero>cuarto_numero>primer_numero>quinto_numero:
     print("la media es"+str(cuarto_numero))
elif segundo_numero>tercer_numero>cuarto_numero>quinto_numero>primer_numero:
     print("la media es"+str(cuarto_numero))
elif segundo_numero>tercer_numero>cuarto_numero>primer_numero>quinto_numero:
     print("la media es"+str(cuarto_numero))
elif segundo_numero>quinto_numero>cuarto_numero>primer_numero>tercer_numero:
     print("la media es"+str(cuarto_numero))
elif segundo_numero>quinto_numero>cuarto_numero>tercer_numero>primer_numero:
     print("la media es"+str(cuarto_numero))
elif quinto_numero>segundo_numero>cuarto_numero>tercer_numero>primer_numero:
     print("la media es"+str(cuarto_numero))
elif quinto_numero>segundo_numero>cuarto_numero>primer_numero>tercer_numero:
     print("la media es"+str(cuarto_numero))
elif tercer_numero>quinto_numero>cuarto_numero>primer_numero>segundo_numero:
     print("la media es"+str(cuarto_numero))
elif tercer_numero>quinto_numero>cuarto_numero>segundo_numero>primer_numero:
     print("la media es"+str(cuarto_numero))
elif quinto_numero>tercer_numero>cuarto_numero>segundo_numero>primer_numero:
     print("la media es"+str(cuarto_numero))
elif quinto_numero>tercer_numero>cuarto_numero>primer_numero>segundo_numero:
     print("la media es"+str(cuarto_numero))
elif primer_numero>segundo_numero>quinto_numero>tercer_numero>cuarto_numero:
     print("la media es"+str(quinto_numero))
elif primer_numero>segundo_numero>quinto_numero>cuarto_numero>tercer_numero:
    print("la media es"+str(quinto_numero))
elif segundo_numero>primer_numero>quinto_numero>cuarto_numero>tercer_numero:
    print("la media es"+str(quinto_numero))
elif segundo_numero>primer_numero>quinto_numero>tercer_numero>cuarto_numero:
    print("la media es"+str(quinto_numero))
elif primer_numero>tercer_numero>quinto_numero>segundo_numero>cuarto_numero:
    print("la media es"+str(quinto_numero))
elif primer_numero>tercer_numero>quinto_numero>cuarto_numero>segundo_numero:
    print("la media es"+str(quinto_numero))
elif tercer_numero>primer_numero>quinto_numero>segundo_numero>cuarto_numero:
    print("la media es"+str(quinto_numero))
elif primer_numero>cuarto_numero>quinto_numero>tercer_numero>segundo_numero:
    print("la media es"+str(quinto_numero))
elif primer_numero>cuarto_numero>quinto_numero>segundo_numero>tercer_numero:
    print("la media es"+str(quinto_numero))
elif segundo_numero>tercer_numero>quinto_numero>cuarto_numero>primer_numero:
    print("la media es"+str(quinto_numero))
elif segundo_numero>tercer_numero>quinto_numero>primer_numero>cuarto_numero:
    print("la media es"+str(quinto_numero))
elif tercer_numero>segundo_numero>quinto_numero>primer_numero>cuarto_numero:
    print("la media es"+str(quinto_numero))
elif tercer_numero>segundo_numero>quinto_numero>cuarto_numero>primer_numero:
    print("la media es"+str(quinto_numero))
elif segundo_numero>cuarto_numero>quinto_numero>tercer_numero>primer_numero:
    print("la media es"+str(quinto_numero))
elif segundo_numero>cuarto_numero>quinto_numero>primer_numero>tercer_numero:
    print("la media es"+str(quinto_numero))
elif cuarto_numero>segundo_numero>quinto_numero>tercer_numero>primer_numero:
    print("la media es"+str(quinto_numero))
elif cuarto_numero>segundo_numero>quinto_numero>primer_numero>tercer_numero:
    print("la media es"+str(quinto_numero))
elif tercer_numero>cuarto_numero>quinto_numero>segundo_numero>primer_numero:
    print("la media es"+str(quinto_numero))
elif tercer_numero>cuarto_numero>quinto_numero>primer_numero>segundo_numero:
    print("la media es"+str(quinto_numero))
elif tercer_numero>cuarto_numero>quinto_numero>segundo_numero>primer_numero:
    print("la media es"+str(quinto_numero))
elif cuarto_numero>tercer_numero>quinto_numero>segundo_numero>primer_numero:
    print("la media es"+str(quinto_numero))
elif cuarto_numero>tercer_numero>quinto_numero>primer_numero>segundo_numero:
    print("la media es"+str(quinto_numero))

#Hallar promedio multiplicativo
multiplicacion = float(primer_numero*segundo_numero*tercer_numero*cuarto_numero*quinto_numero)
raiz = float(multiplicacion**(1/5))
print("el promedio multiplicativo es" +str(raiz))

#Ordenar de mayor a menor 
if segundo_numero>tercer_numero>primer_numero>cuarto_numero>quinto_numero:
    print("orden de mayor a menor:" +str(segundo_numero)+str(tercer_numero)+str(primer_numero)+str(cuarto_numero)+str(quinto_numero))
elif segundo_numero>tercer_numero>primer_numero>quinto_numero>cuarto_numero:
   print("orden de mayor a menor:" +str(segundo_numero)+str(tercer_numero)+str(primer_numero)+str(quinto_numero)+str(cuarto_numero))
elif tercer_numero>segundo_numero>primer_numero>cuarto_numero>quinto_numero:
    print("orden de mayor a menor:" +str(tercer_numero)+str(segundo_numero)+str(primer_numero)+str(cuarto_numero)+str(quinto_numero))
elif tercer_numero>segundo_numero>primer_numero>quinto_numero>cuarto_numero:
   print("orden de mayor a menor:" +str(tercer_numero)+str(segundo_numero)+str(primer_numero)+str(quinto_numero)+str(cuarto_numero))
elif segundo_numero>cuarto_numero>primer_numero>tercer_numero>quinto_numero:
    print("orden de mayor a menor:" +str(segundo_numero)+str(cuarto_numero)+str(primer_numero)+str(tercer_numero)+str(quinto_numero))
elif segundo_numero>cuarto_numero>primer_numero>quinto_numero>tercer_numero:
    print("orden de mayor a menor:" +str(segundo_numero)+str(cuarto_numero)+str(primer_numero)+str(quinto_numero)+str(tercer_numero))
elif cuarto_numero>segundo_numero>primer_numero>quinto_numero>tercer_numero:
   print("orden de mayor a menor:" +str(cuarto_numero)+str(segundo_numero)+str(primer_numero)+str(quinto_numero)+str(tercer_numero))
elif cuarto_numero>segundo_numero>primer_numero>tercer_numero>quinto_numero:
   print("orden de mayor a menor:" +str(cuarto_numero)+str(segundo_numero)+str(primer_numero)+str(tercer_numero)+str(quinto_numero))
elif segundo_numero>quinto_numero>primer_numero>cuarto_numero>tercer_numero:
    print("orden de mayor a menor:" +str(segundo_numero)+str(quinto_numero)+str(primer_numero)+str(cuarto_numero)+str(tercer_numero))
elif segundo_numero>quinto_numero>primer_numero>tercer_numero>cuarto_numero:
     print("orden de mayor a menor:" +str(segundo_numero)+str(quinto_numero)+str(primer_numero)+str(tercer_numero)+str(cuarto_numero))
elif quinto_numero>segundo_numero>primer_numero>tercer_numero>cuarto_numero:
    print("orden de mayor a menor:" +str(quinto_numero)+str(segundo_numero)+str(primer_numero)+str(tercer_numero)+str(cuarto_numero))
elif quinto_numero>segundo_numero>primer_numero>cuarto_numero>tercer_numero:
    print("orden de mayor a menor:" +str(quinto_numero)+str(segundo_numero)+str(primer_numero)+str(cuarto_numero)+str(tercer_numero))
elif tercer_numero>cuarto_numero>primer_numero>segundo_numero>quinto_numero:
    print("orden de mayor a menor:" +str(tercer_numero)+str(cuarto_numero)+str(primer_numero)+str(segundo_numero)+str(quinto_numero))
elif tercer_numero>cuarto_numero>primer_numero>quinto_numero>segundo_numero:
    print("orden de mayor a menor:" +str(tercer_numero)+str(cuarto_numero)+str(primer_numero)+str(quinto_numero)+str(segundo_numero))
elif cuarto_numero>tercer_numero>primer_numero>quinto_numero>segundo_numero:
    print("orden de mayor a menor:" +str(cuarto_numero)+str(tercer_numero)+str(primer_numero)+str(quinto_numero)+str(segundo_numero))
elif cuarto_numero>tercer_numero>primer_numero>segundo_numero>quinto_numero:
    print("orden de mayor a menor:" +str(cuarto_numero)+str(tercer_numero)+str(primer_numero)+str(segundo_numero)+str(quinto_numero))
elif tercer_numero>quinto_numero>primer_numero>cuarto_numero>segundo_numero:
    print("orden de mayor a menor:" +str(tercer_numero)+str(quinto_numero)+str(primer_numero)+str(cuarto_numero)+str(segundo_numero))
elif tercer_numero>quinto_numero>primer_numero>segundo_numero>cuarto_numero:
    print("orden de mayor a menor:" +str(tercer_numero)+str(quinto_numero)+str(primer_numero)+str(segundo_numero)+str(cuarto_numero))
elif quinto_numero>tercer_numero>primer_numero>segundo_numero>cuarto_numero:
    print("orden de mayor a menor:" +str(quinto_numero)+str(tercer_numero)+str(primer_numero)+str(segundo_numero)+str(cuarto_numero))
elif quinto_numero>tercer_numero>primer_numero>cuarto_numero>segundo_numero:
    print("orden de mayor a menor:" +str(quinto_numero)+str(tercer_numero)+str(primer_numero)+str(cuarto_numero)+str(segundo_numero))
elif cuarto_numero>quinto_numero>primer_numero>tercer_numero>segundo_numero:
    print("orden de mayor a menor:" +str(cuarto_numero)+str(quinto_numero)+str(primer_numero)+str(tercer_numero)+str(segundo_numero))
elif cuarto_numero>quinto_numero>primer_numero>segundo_numero>tercer_numero:
    print("orden de mayor a menor:" +str(cuarto_numero)+str(quinto_numero)+str(primer_numero)+str(segundo_numero)+str(tercer_numero))
elif quinto_numero>cuarto_numero>primer_numero>segundo_numero>tercer_numero:
    print("orden de mayor a menor:" +str(quinto_numero)+str(cuarto_numero)+str(primer_numero)+str(segundo_numero)+str(tercer_numero))
elif quinto_numero>cuarto_numero>primer_numero>tercer_numero>segundo_numero:
    print("orden de mayor a menor:" +str(quinto_numero)+str(cuarto_numero)+str(primer_numero)+str(tercer_numero)+str(segundo_numero))
elif primer_numero>tercer_numero>segundo_numero>cuarto_numero>quinto_numero:
    print("orden de mayor a menor:" +str(primer_numero)+str(tercer_numero)+str(segundo_numero)+str(cuarto_numero)+str(quinto_numero))
elif primer_numero>tercer_numero>segundo_numero>quinto_numero>cuarto_numero:
    print("orden de mayor a menor:" +str(primer_numero)+str(tercer_numero)+str(segundo_numero)+str(quinto_numero)+str(cuarto_numero))
elif tercer_numero>primer_numero>segundo_numero>quinto_numero>cuarto_numero:
    print("orden de mayor a menor:" +str(tercer_numero)+str(primer_numero)+str(segundo_numero)+str(quinto_numero)+str(cuarto_numero))
elif tercer_numero>primer_numero>segundo_numero>cuarto_numero>quinto_numero:
     print("orden de mayor a menor:" +str(tercer_numero)+str(primer_numero)+str(segundo_numero)+str(cuarto_numero)+str(quinto_numero))
elif primer_numero>cuarto_numero>segundo_numero>tercer_numero>quinto_numero:
     print("orden de mayor a menor:" +str(primer_numero)+str(cuarto_numero)+str(segundo_numero)+str(tercer_numero)+str(quinto_numero))
elif primer_numero>cuarto_numero>segundo_numero>quinto_numero>tercer_numero:
     print("orden de mayor a menor:" +str(primer_numero)+str(cuarto_numero)+str(segundo_numero)+str(quinto_numero)+str(tercer_numero))
elif cuarto_numero>primer_numero>segundo_numero>quinto_numero>tercer_numero:
    print("orden de mayor a menor:" +str(cuarto_numero)+str(primer_numero)+str(segundo_numero)+str(quinto_numero)+str(tercer_numero))
elif cuarto_numero>primer_numero>segundo_numero>tercer_numero>quinto_numero:
    print("orden de mayor a menor:" +str(cuarto_numero)+str(primer_numero)+str(segundo_numero)+str(tercer_numero)+str(quinto_numero))
elif primer_numero>quinto_numero>segundo_numero>cuarto_numero>tercer_numero:
    print("orden de mayor a menor:" +str(primer_numero)+str(quinto_numero)+str(segundo_numero)+str(cuarto_numero)+str(tercer_numero))
elif primer_numero>quinto_numero>segundo_numero>tercer_numero>cuarto_numero:
    print("orden de mayor a menor:" +str(primer_numero)+str(quinto_numero)+str(segundo_numero)+str(tercer_numero)+str(cuarto_numero))
elif quinto_numero>primer_numero>segundo_numero>tercer_numero>cuarto_numero:
    print("orden de mayor a menor:" +str(quinto_numero)+str(primer_numero)+str(segundo_numero)+str(tercer_numero)+str(cuarto_numero))
elif quinto_numero>primer_numero>segundo_numero>cuarto_numero>tercer_numero:
    print("orden de mayor a menor:" +str(quinto_numero)+str(primer_numero)+str(segundo_numero)+str(cuarto_numero)+str(tercer_numero))
elif tercer_numero>cuarto_numero>segundo_numero>primer_numero>quinto_numero:
    print("orden de mayor a menor:" +str(tercer_numero)+str(cuarto_numero)+str(segundo_numero)+str(primer_numero)+str(quinto_numero))
elif tercer_numero>cuarto_numero>segundo_numero>quinto_numero>primer_numero:
    print("orden de mayor a menor:" +str(tercer_numero)+str(cuarto_numero)+str(segundo_numero)+str(quinto_numero)+str(primer_numero))
elif cuarto_numero>tercer_numero>segundo_numero>primer_numero>quinto_numero:
    print("orden de mayor a menor:" +str(cuarto_numero)+str(tercer_numero)+str(segundo_numero)+str(primer_numero)+str(quinto_numero))
elif cuarto_numero>tercer_numero>segundo_numero>quinto_numero>primer_numero:
    print("orden de mayor a menor:" +str(cuarto_numero)+str(tercer_numero)+str(segundo_numero)+str(quinto_numero)+str(primer_numero))
elif tercer_numero>quinto_numero>segundo_numero>cuarto_numero>primer_numero:
    print("orden de mayor a menor:" +str(cuarto_numero)+str(tercer_numero)+str(segundo_numero)+str(primer_numero)+str(quinto_numero))
elif tercer_numero>quinto_numero>segundo_numero>primer_numero>cuarto_numero:
    print("orden de mayor a menor:" +str(tercer_numero)+str(quinto_numero)+str(segundo_numero)+str(primer_numero)+str(cuarto_numero))
elif cuarto_numero>quinto_numero>segundo_numero>tercer_numero>primer_numero:
    print("orden de mayor a menor:" +str(cuarto_numero)+str(quinto_numero)+str(segundo_numero)+str(tercer_numero)+str(primer_numero))
elif cuarto_numero>quinto_numero>segundo_numero>primer_numero>tercer_numero:
    print("orden de mayor a menor:" +str(cuarto_numero)+str(quinto_numero)+str(segundo_numero)+str(primer_numero)+str(tercer_numero))
elif quinto_numero>cuarto_numero>segundo_numero>primer_numero>tercer_numero:
    print("orden de mayor a menor:" +str(quinto_numero)+str(cuarto_numero)+str(segundo_numero)+str(primer_numero)+str(tercer_numero))
elif quinto_numero>cuarto_numero>segundo_numero>tercer_numero>primer_numero:
    print("orden de mayor a menor:" +str(quinto_numero)+str(cuarto_numero)+str(segundo_numero)+str(tercer_numero)+str(primer_numero))
elif primer_numero>segundo_numero>tercer_numero>cuarto_numero>quinto_numero:
    print("orden de mayor a menor:" +str(primer_numero)+str(segundo_numero)+str(tercer_numero)+str(cuarto_numero)+str(quinto_numero))
elif primer_numero>segundo_numero>tercer_numero>quinto_numero>cuarto_numero:
    print("orden de mayor a menor:" +str(primer_numero)+str(segundo_numero)+str(tercer_numero)+str(quinto_numero)+str(cuarto_numero))
elif segundo_numero>primer_numero>tercer_numero>quinto_numero>cuarto_numero:
    print("orden de mayor a menor:" +str(segundo_numero)+str(primer_numero)+str(tercer_numero)+str(quinto_numero)+str(cuarto_numero))
elif segundo_numero>primer_numero>tercer_numero>cuarto_numero>quinto_numero:
    print("orden de mayor a menor:" +str(segundo_numero)+str(primer_numero)+str(tercer_numero)+str(cuarto_numero)+str(quinto_numero))
elif primer_numero>cuarto_numero>tercer_numero>quinto_numero>segundo_numero:
    print("orden de mayor a menor:" +str(primer_numero)+str(cuarto_numero)+str(tercer_numero)+str(quinto_numero)+str(segundo_numero))
elif primer_numero>cuarto_numero>tercer_numero>segundo_numero>quinto_numero:
    print("orden de mayor a menor:" +str(primer_numero)+str(cuarto_numero)+str(tercer_numero)+str(segundo_numero)+str(quinto_numero))
elif cuarto_numero>primer_numero>tercer_numero>segundo_numero>quinto_numero:
    print("orden de mayor a menor:" +str(cuarto_numero)+str(primer_numero)+str(tercer_numero)+str(segundo_numero)+str(quinto_numero))
elif cuarto_numero>primer_numero>tercer_numero>quinto_numero>segundo_numero:
    print("orden de mayor a menor:" +str(cuarto_numero)+str(primer_numero)+str(tercer_numero)+str(quinto_numero)+str(segundo_numero))
elif primer_numero>quinto_numero>tercer_numero>cuarto_numero>segundo_numero:
    print("orden de mayor a menor:" +str(primer_numero)+str(quinto_numero)+str(tercer_numero)+str(cuarto_numero)+str(segundo_numero))
elif primer_numero>quinto_numero>tercer_numero>segundo_numero>cuarto_numero:
    print("orden de mayor a menor:" +str(primer_numero)+str(quinto_numero)+str(tercer_numero)+str(segundo_numero)+str(cuarto_numero))
elif quinto_numero>primer_numero>tercer_numero>segundo_numero>cuarto_numero:
    print("orden de mayor a menor:" +str(quinto_numero)+str(primer_numero)+str(tercer_numero)+str(segundo_numero)+str(cuarto_numero))
elif quinto_numero>primer_numero>tercer_numero>cuarto_numero>segundo_numero:
    print("orden de mayor a menor:" +str(quinto_numero)+str(primer_numero)+str(tercer_numero)+str(cuarto_numero)+str(segundo_numero))
elif segundo_numero>cuarto_numero>tercer_numero>quinto_numero>primer_numero:
    print("orden de mayor a menor:" +str(segundo_numero)+str(cuarto_numero)+str(tercer_numero)+str(quinto_numero)+str(primer_numero))
elif segundo_numero>cuarto_numero>tercer_numero>primer_numero>quinto_numero:
    print("orden de mayor a menor:" +str(segundo_numero)+str(cuarto_numero)+str(tercer_numero)+str(primer_numero)+str(quinto_numero))
elif cuarto_numero>segundo_numero>tercer_numero>primer_numero>quinto_numero:
    print("orden de mayor a menor:" +str(cuarto_numero)+str(segundo_numero)+str(tercer_numero)+str(primer_numero)+str(quinto_numero))
elif cuarto_numero>segundo_numero>tercer_numero>quinto_numero>primer_numero:
    print("orden de mayor a menor:" +str(cuarto_numero)+str(segundo_numero)+str(tercer_numero)+str(quinto_numero)+str(primer_numero))
elif segundo_numero>quinto_numero>tercer_numero>primer_numero>cuarto_numero:
    print("orden de mayor a menor:" +str(segundo_numero)+str(quinto_numero)+str(tercer_numero)+str(primer_numero)+str(cuarto_numero))
elif segundo_numero>quinto_numero>tercer_numero>cuarto_numero>primer_numero:
    print("orden de mayor a menor:" +str(segundo_numero)+str(quinto_numero)+str(tercer_numero)+str(cuarto_numero)+str(primer_numero))
elif quinto_numero>segundo_numero>tercer_numero>primer_numero>cuarto_numero:
    print("orden de mayor a menor:" +str(quinto_numero)+str(segundo_numero)+str(tercer_numero)+str(primer_numero)+str(cuarto_numero))
elif quinto_numero>segundo_numero>tercer_numero>cuarto_numero>primer_numero:
    print("orden de mayor a menor:" +str(quinto_numero)+str(segundo_numero)+str(tercer_numero)+str(cuarto_numero)+str(primer_numero))
elif cuarto_numero>quinto_numero>tercer_numero>segundo_numero>primer_numero:
    print("orden de mayor a menor:" +str(cuarto_numero)+str(quinto_numero)+str(tercer_numero)+str(segundo_numero)+str(primer_numero))
elif cuarto_numero>quinto_numero>tercer_numero>primer_numero>segundo_numero:
    print("orden de mayor a menor:" +str(cuarto_numero)+str(quinto_numero)+str(tercer_numero)+str(primer_numero)+str(segundo_numero))
elif quinto_numero>cuarto_numero>tercer_numero>segundo_numero>primer_numero:
    print("orden de mayor a menor:" +str(quinto_numero)+str(cuarto_numero)+str(tercer_numero)+str(segundo_numero)+str(primer_numero))
elif quinto_numero>cuarto_numero>tercer_numero>primer_numero>segundo_numero:
    print("orden de mayor a menor:" +str(quinto_numero)+str(cuarto_numero)+str(tercer_numero)+str(primer_numero)+str(segundo_numero))
elif primer_numero>segundo_numero>cuarto_numero>tercer_numero>quinto_numero:
    print("orden de mayor a menor:" +str(primer_numero)+str(segundo_numero)+str(cuarto_numero)+str(tercer_numero)+str(quinto_numero))
elif primer_numero>segundo_numero>cuarto_numero>quinto_numero>tercer_numero:
     print("orden de mayor a menor:" +str(primer_numero)+str(segundo_numero)+str(cuarto_numero)+str(quinto_numero)+str(tercer_numero))
elif segundo_numero>primer_numero>cuarto_numero>quinto_numero>tercer_numero:
     print("orden de mayor a menor:" +str(segundo_numero)+str(primer_numero)+str(cuarto_numero)+str(quinto_numero)+str(tercer_numero))
elif segundo_numero>primer_numero>cuarto_numero>tercer_numero>quinto_numero:
      print("orden de mayor a menor:" +str(segundo_numero)+str(primer_numero)+str(cuarto_numero)+str(tercer_numero)+str(quinto_numero))
elif primer_numero>tercer_numero>cuarto_numero>quinto_numero>segundo_numero:
      print("orden de mayor a menor:" +str(primer_numero)+str(tercer_numero)+str(cuarto_numero)+str(quinto_numero)+str(segundo_numero))
elif primer_numero>tercer_numero>cuarto_numero>segundo_numero>quinto_numero:
      print("orden de mayor a menor:" +str(primer_numero)+str(tercer_numero)+str(cuarto_numero)+str(segundo_numero)+str(quinto_numero))
elif tercer_numero>primer_numero>cuarto_numero>quinto_numero>segundo_numero:
     print("orden de mayor a menor:" +str(tercer_numero)+str(primer_numero)+str(cuarto_numero)+str(quinto_numero)+str(segundo_numero))
elif tercer_numero>primer_numero>cuarto_numero>segundo_numero>quinto_numero:
     print("orden de mayor a menor:" +str(tercer_numero)+str(primer_numero)+str(cuarto_numero)+str(segundo_numero)+str(quinto_numero))
elif primer_numero>quinto_numero>cuarto_numero>segundo_numero>tercer_numero:
     print("orden de mayor a menor:" +str(primer_numero)+str(quinto_numero)+str(cuarto_numero)+str(segundo_numero)+str(tercer_numero))
elif primer_numero>quinto_numero>cuarto_numero>tercer_numero>segundo_numero:
     print("orden de mayor a menor:" +str(primer_numero)+str(quinto_numero)+str(cuarto_numero)+str(tercer_numero)+str(segundo_numero))
elif quinto_numero>primer_numero>cuarto_numero>segundo_numero>tercer_numero:
     print("orden de mayor a menor:" +str(quinto_numero)+str(primer_numero)+str(cuarto_numero)+str(segundo_numero)+str(tercer_numero))
elif quinto_numero>primer_numero>cuarto_numero>tercer_numero>segundo_numero:
     print("orden de mayor a menor:" +str(quinto_numero)+str(primer_numero)+str(cuarto_numero)+str(tercer_numero)+str(segundo_numero))
elif tercer_numero>segundo_numero>cuarto_numero>quinto_numero>primer_numero:
     print("orden de mayor a menor:" +str(tercer_numero)+str(segundo_numero)+str(cuarto_numero)+str(quinto_numero)+str(primer_numero))
elif tercer_numero>segundo_numero>cuarto_numero>primer_numero>quinto_numero:
     print("orden de mayor a menor:" +str(tercer_numero)+str(segundo_numero)+str(cuarto_numero)+str(primer_numero)+str(quinto_numero))
elif segundo_numero>tercer_numero>cuarto_numero>quinto_numero>primer_numero:
     print("orden de mayor a menor:" +str(segundo_numero)+str(tercer_numero)+str(cuarto_numero)+str(quinto_numero)+str(primer_numero))
elif segundo_numero>tercer_numero>cuarto_numero>primer_numero>quinto_numero:
     print("orden de mayor a menor:" +str(segundo_numero)+str(tercer_numero)+str(cuarto_numero)+str(primer_numero)+str(quinto_numero))
elif segundo_numero>quinto_numero>cuarto_numero>primer_numero>tercer_numero:
     print("orden de mayor a menor:" +str(segundo_numero)+str(quinto_numero)+str(cuarto_numero)+str(primer_numero)+str(tercer_numero))
elif segundo_numero>quinto_numero>cuarto_numero>tercer_numero>primer_numero:
     print("orden de mayor a menor:" +str(segundo_numero)+str(quinto_numero)+str(cuarto_numero)+str(tercer_numero)+str(primer_numero))
elif quinto_numero>segundo_numero>cuarto_numero>tercer_numero>primer_numero:
     print("orden de mayor a menor:" +str(quinto_numero)+str(segundo_numero)+str(cuarto_numero)+str(tercer_numero)+str(primer_numero))
elif quinto_numero>segundo_numero>cuarto_numero>primer_numero>tercer_numero:
     print("orden de mayor a menor:" +str(quinto_numero)+str(segundo_numero)+str(cuarto_numero)+str(primer_numero)+str(tercer_numero))
elif tercer_numero>quinto_numero>cuarto_numero>primer_numero>segundo_numero:
     print("orden de mayor a menor:" +str(tercer_numero)+str(quinto_numero)+str(cuarto_numero)+str(primer_numero)+str(segundo_numero))
elif tercer_numero>quinto_numero>cuarto_numero>segundo_numero>primer_numero:
     print("orden de mayor a menor:" +str(tercer_numero)+str(quinto_numero)+str(cuarto_numero)+str(segundo_numero)+str(primer_numero))
elif quinto_numero>tercer_numero>cuarto_numero>segundo_numero>primer_numero:
     print("orden de mayor a menor:" +str(quinto_numero)+str(tercer_numero)+str(cuarto_numero)+str(segundo_numero)+str(primer_numero))
elif quinto_numero>tercer_numero>cuarto_numero>primer_numero>segundo_numero:
     print("orden de mayor a menor:" +str(quinto_numero)+str(tercer_numero)+str(cuarto_numero)+str(primer_numero)+str(segundo_numero))
elif primer_numero>segundo_numero>quinto_numero>tercer_numero>cuarto_numero:
     print("orden de mayor a menor:" +str(primer_numero)+str(segundo_numero)+str(quinto_numero)+str(tercer_numero)+str(cuarto_numero))
elif primer_numero>segundo_numero>quinto_numero>cuarto_numero>tercer_numero:
     print("orden de mayor a menor:" +str(primer_numero)+str(segundo_numero)+str(quinto_numero)+str(cuarto_numero)+str(tercer_numero))
elif segundo_numero>primer_numero>quinto_numero>cuarto_numero>tercer_numero:
     print("orden de mayor a menor:" +str(segundo_numero)+str(primer_numero)+str(quinto_numero)+str(cuarto_numero)+str(tercer_numero))
elif segundo_numero>primer_numero>quinto_numero>tercer_numero>cuarto_numero:
    print("orden de mayor a menor:" +str(segundo_numero)+str(primer_numero)+str(quinto_numero)+str(tercer_numero)+str(cuarto_numero))
elif primer_numero>tercer_numero>quinto_numero>segundo_numero>cuarto_numero:
    print("orden de mayor a menor:" +str(primer_numero)+str(tercer_numero)+str(quinto_numero)+str(segundo_numero)+str(cuarto_numero))
elif primer_numero>tercer_numero>quinto_numero>cuarto_numero>segundo_numero:
    print("orden de mayor a menor:" +str(primer_numero)+str(tercer_numero)+str(quinto_numero)+str(cuarto_numero)+str(segundo_numero))
elif tercer_numero>primer_numero>quinto_numero>segundo_numero>cuarto_numero:
    print("orden de mayor a menor:" +str(tercer_numero)+str(primer_numero)+str(quinto_numero)+str(segundo_numero)+str(cuarto_numero))
elif primer_numero>cuarto_numero>quinto_numero>tercer_numero>segundo_numero:
    print("orden de mayor a menor:" +str(primer_numero)+str(cuarto_numero)+str(quinto_numero)+str(tercer_numero)+str(segundo_numero))
elif primer_numero>cuarto_numero>quinto_numero>segundo_numero>tercer_numero:
    print("orden de mayor a menor:" +str(primer_numero)+str(cuarto_numero)+str(quinto_numero)+str(segundo_numero)+str(tercer_numero))
elif segundo_numero>tercer_numero>quinto_numero>cuarto_numero>primer_numero:
    print("orden de mayor a menor:" +str(segundo_numero)+str(tercer_numero)+str(quinto_numero)+str(cuarto_numero)+str(primer_numero))
elif segundo_numero>tercer_numero>quinto_numero>primer_numero>cuarto_numero:
    print("orden de mayor a menor:" +str(segundo_numero)+str(tercer_numero)+str(quinto_numero)+str(primer_numero)+str(cuarto_numero))
elif tercer_numero>segundo_numero>quinto_numero>primer_numero>cuarto_numero:
    print("orden de mayor a menor:" +str(tercer_numero)+str(segundo_numero)+str(quinto_numero)+str(primer_numero)+str(cuarto_numero))
elif tercer_numero>segundo_numero>quinto_numero>cuarto_numero>primer_numero:
    print("orden de mayor a menor:" +str(tercer_numero)+str(segundo_numero)+str(quinto_numero)+str(cuarto_numero)+str(primer_numero))
elif segundo_numero>cuarto_numero>quinto_numero>tercer_numero>primer_numero:
    print("orden de mayor a menor:" +str(segundo_numero)+str(cuarto_numero)+str(quinto_numero)+str(tercer_numero)+str(primer_numero))
elif segundo_numero>cuarto_numero>quinto_numero>primer_numero>tercer_numero:
    print("orden de mayor a menor:" +str(segundo_numero)+str(cuarto_numero)+str(quinto_numero)+str(primer_numero)+str(tercer_numero))
elif cuarto_numero>segundo_numero>quinto_numero>tercer_numero>primer_numero:
    print("orden de mayor a menor:" +str(cuarto_numero)+str(segundo_numero)+str(quinto_numero)+str(tercer_numero)+str(primer_numero))
elif cuarto_numero>segundo_numero>quinto_numero>primer_numero>tercer_numero:
    print("orden de mayor a menor:" +str(cuarto_numero)+str(segundo_numero)+str(quinto_numero)+str(primer_numero)+str(tercer_numero))
elif tercer_numero>cuarto_numero>quinto_numero>segundo_numero>primer_numero:
    print("orden de mayor a menor:" +str(tercer_numero)+str(cuarto_numero)+str(quinto_numero)+str(segundo_numero)+str(primer_numero))
elif tercer_numero>cuarto_numero>quinto_numero>primer_numero>segundo_numero:
    print("orden de mayor a menor:" +str(tercer_numero)+str(cuarto_numero)+str(quinto_numero)+str(primer_numero)+str(segundo_numero))
elif tercer_numero>cuarto_numero>quinto_numero>segundo_numero>primer_numero:
    print("orden de mayor a menor:" +str(tercer_numero)+str(cuarto_numero)+str(quinto_numero)+str(segundo_numero)+str(primer_numero))
elif cuarto_numero>tercer_numero>quinto_numero>segundo_numero>primer_numero:
    print("orden de mayor a menor:" +str(cuarto_numero)+str(tercer_numero)+str(quinto_numero)+str(segundo_numero)+str(primer_numero))
elif cuarto_numero>tercer_numero>quinto_numero>primer_numero>segundo_numero:
    print("orden de mayor a menor:" +str(cuarto_numero)+str(tercer_numero)+str(quinto_numero)+str(primer_numero)+str(segundo_numero))

    #Orden menor a mayor
if segundo_numero>tercer_numero>primer_numero>cuarto_numero>quinto_numero:
    print("orden de menor a mayor:" +str(quinto_numero)+str(cuarto_numero)+str(primer_numero)+str(tercer_numero)+str(segundo_numero))
elif segundo_numero>tercer_numero>primer_numero>quinto_numero>cuarto_numero:
   print("orden de menor a mayor:" +str(cuarto_numero)+str(quinto_numero)+str(primer_numero)+str(tercer_numero)+str(segundo_numero))
elif tercer_numero>segundo_numero>primer_numero>cuarto_numero>quinto_numero:
    print("orden de menor a mayor:" +str(quinto_numero)+str(cuarto_numero)+str(primer_numero)+str(segundo_numero)+str(tercer_numero))
elif tercer_numero>segundo_numero>primer_numero>quinto_numero>cuarto_numero:
   print("orden de menor a mayor:" +str(cuarto_numero)+str(quinto_numero)+str(primer_numero)+str(segundo_numero)+str(tercer_numero))
elif segundo_numero>cuarto_numero>primer_numero>tercer_numero>quinto_numero:
    print("orden de menor a mayor:" +str(quinto_numero)+str(tercer_numero)+str(primer_numero)+str(cuarto_numero)+str(segundo_numero))
elif segundo_numero>cuarto_numero>primer_numero>quinto_numero>tercer_numero:
    print("orden de menor a mayor:" +str(tercer_numero)+str(quinto_numero)+str(primer_numero)+str(cuarto_numero)+str(segundo_numero))
elif cuarto_numero>segundo_numero>primer_numero>quinto_numero>tercer_numero:
   print("orden de menor a myor:" +str(tercer_numero)+str(quinto_numero)+str(primer_numero)+str(segundo_numero)+str(cuarto_numero))
elif cuarto_numero>segundo_numero>primer_numero>tercer_numero>quinto_numero:
   print("orden de menor a mayor:" +str(quinto_numero)+str(tercer_numero)+str(primer_numero)+str(segundo_numero)+str(cuarto_numero))
elif segundo_numero>quinto_numero>primer_numero>cuarto_numero>tercer_numero:
    print("orden de menor a mayor:" +str(tercer_numero)+str(cuarto_numero)+str(primer_numero)+str(quinto_numero)+str(segundo_numero))
elif segundo_numero>quinto_numero>primer_numero>tercer_numero>cuarto_numero:
     print("orden de menor a mayor:" +str(cuarto_numero)+str(tercer_numero)+str(primer_numero)+str(quinto_numero)+str(segundo_numero))
elif quinto_numero>segundo_numero>primer_numero>tercer_numero>cuarto_numero:
    print("orden de menor a mayor:" +str(cuarto_numero)+str(tercer_numero)+str(primer_numero)+str(segundo_numero)+str(quinto_numero))
elif quinto_numero>segundo_numero>primer_numero>cuarto_numero>tercer_numero:
    print("orden de menor a mayor:" +str(tercer_numero)+str(cuarto_numero)+str(primer_numero)+str(segundo_numero)+str(quinto_numero))
elif tercer_numero>cuarto_numero>primer_numero>segundo_numero>quinto_numero:
    print("orden de menor a mayor:" +str(quinto_numero)+str(segundo_numero)+str(primer_numero)+str(cuarto_numero)+str(tercer_numero))
elif tercer_numero>cuarto_numero>primer_numero>quinto_numero>segundo_numero:
    print("orden de menor a mayor:" +str(segundo_numero)+str(quinto_numero)+str(primer_numero)+str(cuarto_numero)+str(tercer_numero))
elif cuarto_numero>tercer_numero>primer_numero>quinto_numero>segundo_numero:
    print("orden de menor a mayor:" +str(segundo_numero)+str(quinto_numero)+str(primer_numero)+str(tercer_numero)+str(cuarto_numero))
elif cuarto_numero>tercer_numero>primer_numero>segundo_numero>quinto_numero:
    print("orden de menor a mayor:" +str(quinto_numero)+str(segundo_numero)+str(primer_numero)+str(segundo_numero)+str(quinto_numero))
elif tercer_numero>quinto_numero>primer_numero>cuarto_numero>segundo_numero:
    print("orden de menor a mayor:" +str(segundo_numero)+str(cuarto_numero)+str(primer_numero)+str(quinto_numero)+str(tercer_numero))
elif tercer_numero>quinto_numero>primer_numero>segundo_numero>cuarto_numero:
    print("orden de menor a mayor:" +str(cuarto_numero)+str(segundo_numero)+str(primer_numero)+str(quinto_numero)+str(tercer_numero))
elif quinto_numero>tercer_numero>primer_numero>segundo_numero>cuarto_numero:
    print("orden de menor a mayor:" +str(cuarto_numero)+str(segundo_numero)+str(primer_numero)+str(tercer_numero)+str(quinto_numero))
elif quinto_numero>tercer_numero>primer_numero>cuarto_numero>segundo_numero:
    print("orden de menor a mayor:" +str(segundo_numero)+str(cuarto_numero)+str(primer_numero)+str(tercer_numero)+str(quinto_numero))
elif cuarto_numero>quinto_numero>primer_numero>tercer_numero>segundo_numero:
    print("orden de menor a mayor:" +str(segundo_numero)+str(tercer_numero)+str(primer_numero)+str(quinto_numero)+str(cuarto_numero))
elif cuarto_numero>quinto_numero>primer_numero>segundo_numero>tercer_numero:
    print("orden de menor a mayorr:" +str(tercer_numero)+str(segundo_numero)+str(primer_numero)+str(quinto_numero)+str(cuarto_numero))
elif quinto_numero>cuarto_numero>primer_numero>segundo_numero>tercer_numero:
    print("orden de menor a mayor:" +str(tercer_numero)+str(segundo_numero)+str(primer_numero)+str(cuarto_numero)+str(quinto_numero))
elif quinto_numero>cuarto_numero>primer_numero>tercer_numero>segundo_numero:
    print("orden de menor a mayor:" +str(segundo_numero)+str(tercer_numero)+str(primer_numero)+str(cuarto_numero)+str(quinto_numero))
elif primer_numero>tercer_numero>segundo_numero>cuarto_numero>quinto_numero:
    print("orden de menor a mayor:" +str(quinto_numero)+str(cuarto_numero)+str(segundo_numero)+str(tercer_numero)+str(primer_numero))
elif primer_numero>tercer_numero>segundo_numero>quinto_numero>cuarto_numero:
    print("orden de menor a mayor:" +str(cuarto_numero)+str(quinto_numero)+str(segundo_numero)+str(tercer_numero)+str(primer_numero))
elif tercer_numero>primer_numero>segundo_numero>quinto_numero>cuarto_numero:
    print("orden de menor a mayorr:" +str(cuarto_numero)+str(quinto_numero)+str(segundo_numero)+str(primer_numero)+str(tercer_numero))
elif tercer_numero>primer_numero>segundo_numero>cuarto_numero>quinto_numero:
     print("orden de menor a mayor:" +str(quinto_numero)+str(cuarto_numero)+str(segundo_numero)+str(primer_numero)+str(tercer_numero))
elif primer_numero>cuarto_numero>segundo_numero>tercer_numero>quinto_numero:
     print("orden de menor a mayor:" +str(quinto_numero)+str(tercer_numero)+str(segundo_numero)+str(cuarto_numero)+str(primer_numero))
elif primer_numero>cuarto_numero>segundo_numero>quinto_numero>tercer_numero:
     print("orden de menor a mayor:" +str(tercer_numero)+str(quinto_numero)+str(segundo_numero)+str(cuarto_numero)+str(primer_numero))
elif cuarto_numero>primer_numero>segundo_numero>quinto_numero>tercer_numero:
    print("orden de menor a mayor:" +str(tercer_numero)+str(quinto_numero)+str(segundo_numero)+str(primer_numero)+str(cuarto_numero))
elif cuarto_numero>primer_numero>segundo_numero>tercer_numero>quinto_numero:
    print("orden de menor a mayor:" +str(quinto_numero)+str(tercer_numero)+str(segundo_numero)+str(primer_numero)+str(cuarto_numero))
elif primer_numero>quinto_numero>segundo_numero>cuarto_numero>tercer_numero:
    print("orden de menor a mayor:" +str(tercer_numero)+str(cuarto_numero)+str(segundo_numero)+str(quinto_numero)+str(primer_numero))
elif primer_numero>quinto_numero>segundo_numero>tercer_numero>cuarto_numero:
    print("orden de menor a mayor:" +str(cuarto_numero)+str(tercer_numero)+str(segundo_numero)+str(quinto_numero)+str(primer_numero))
elif quinto_numero>primer_numero>segundo_numero>tercer_numero>cuarto_numero:
    print("orden de menor a mayor:" +str(cuarto_numero)+str(tercer_numero)+str(segundo_numero)+str(primer_numero)+str(quinto_numero))
elif quinto_numero>primer_numero>segundo_numero>cuarto_numero>tercer_numero:
    print("orden de menor a mayor:" +str(tercer_numero)+str(cuarto_numero)+str(segundo_numero)+str(primer_numero)+str(quinto_numero))
elif tercer_numero>cuarto_numero>segundo_numero>primer_numero>quinto_numero:
    print("orden de menor a mayor:" +str(quinto_numero)+str(primer_numero)+str(segundo_numero)+str(cuarto_numero)+str(tercer_numero))
elif tercer_numero>cuarto_numero>segundo_numero>quinto_numero>primer_numero:
    print("orden de menor a mayor:" +str(primer_numero)+str(quinto_numero)+str(segundo_numero)+str(cuarto_numero)+str(tercer_numero))
elif cuarto_numero>tercer_numero>segundo_numero>primer_numero>quinto_numero:
    print("orden de menor a mayor:" +str(quinto_numero)+str(primer_numero)+str(segundo_numero)+str(tercer_numero)+str(cuarto_numero))
elif cuarto_numero>tercer_numero>segundo_numero>quinto_numero>primer_numero:
    print("orden de menor a mayor:" +str(primer_numero)+str(quinto_numero)+str(segundo_numero)+str(tercer_numero)+str(cuarto_numero))
elif tercer_numero>quinto_numero>segundo_numero>cuarto_numero>primer_numero:
    print("orden de menor a mayor:" +str(primer_numero)+str(cuarto_numero)+str(segundo_numero)+str(quinto_numero)+str(tercer_numero))
elif tercer_numero>quinto_numero>segundo_numero>primer_numero>cuarto_numero:
    print("orden de menor a mayor:" +str(cuarto_numero)+str(primer_numero)+str(segundo_numero)+str(quinto_numero)+str(tercer_numero))
elif cuarto_numero>quinto_numero>segundo_numero>tercer_numero>primer_numero:
    print("orden de menor a mayor:" +str(primer_numero)+str(tercer_numero)+str(segundo_numero)+str(quinto_numero)+str(cuarto_numero))
elif cuarto_numero>quinto_numero>segundo_numero>primer_numero>tercer_numero:
    print("orden de menor a mayor:" +str(tercer_numero)+str(primer_numero)+str(segundo_numero)+str(quinto_numero)+str(cuarto_numero))
elif quinto_numero>cuarto_numero>segundo_numero>primer_numero>tercer_numero:
    print("orden de menor a mayor:" +str(tercer_numero)+str(primer_numero)+str(segundo_numero)+str(cuarto_numero)+str(quinto_numero))
elif quinto_numero>cuarto_numero>segundo_numero>tercer_numero>primer_numero:
    print("orden de menor a mayor:" +str(primer_numero)+str(tercer_numero)+str(segundo_numero)+str(cuarto_numero)+str(quinto_numero))
elif primer_numero>segundo_numero>tercer_numero>cuarto_numero>quinto_numero:
    print("orden de menor a mayor:" +str(quinto_numero)+str(cuarto_numero)+str(tercer_numero)+str(segundo_numero)+str(primer_numero))
elif primer_numero>segundo_numero>tercer_numero>quinto_numero>cuarto_numero:
    print("orden de menor a mayor:" +str(cuarto_numero)+str(quinto_numero)+str(tercer_numero)+str(segundo_numero)+str(primer_numero))
elif segundo_numero>primer_numero>tercer_numero>quinto_numero>cuarto_numero:
    print("orden de menor a mayor:" +str(cuarto_numero)+str(quinto_numero)+str(tercer_numero)+str(primer_numero)+str(segundo_numero))
elif segundo_numero>primer_numero>tercer_numero>cuarto_numero>quinto_numero:
    print("orden de menor a mayor:" +str(quinto_numero)+str(cuarto_numero)+str(tercer_numero)+str(primer_numero)+str(segundo_numero))
elif primer_numero>cuarto_numero>tercer_numero>quinto_numero>segundo_numero:
    print("orden de menor a mayor:" +str(primer_numero)+str(cuarto_numero)+str(tercer_numero)+str(quinto_numero)+str(segundo_numero))
elif primer_numero>cuarto_numero>tercer_numero>segundo_numero>quinto_numero:
    print("orden de menor a mayor:" +str(quinto_numero)+str(segundo_numero)+str(tercer_numero)+str(cuarto_numero)+str(primer_numero))
elif cuarto_numero>primer_numero>tercer_numero>segundo_numero>quinto_numero:
    print("orden de menor a mayor:" +str(quinto_numero)+str(segundo_numero)+str(tercer_numero)+str(primer_numero)+str(cuarto_numero))
elif cuarto_numero>primer_numero>tercer_numero>quinto_numero>segundo_numero:
    print("orden de menor a mayor:" +str(segundo_numero)+str(quinto_numero)+str(tercer_numero)+str(primer_numero)+str(cuarto_numero))
elif primer_numero>quinto_numero>tercer_numero>cuarto_numero>segundo_numero:
    print("orden de menor a mayor:" +str(segundo_numero)+str(cuarto_numero)+str(tercer_numero)+str(quinto_numero)+str(primer_numero))
elif primer_numero>quinto_numero>tercer_numero>segundo_numero>cuarto_numero:
    print("orden de menor a mayor:" +str(cuarto_numero)+str(segundo_numero)+str(tercer_numero)+str(quinto_numero)+str(primer_numero))
elif quinto_numero>primer_numero>tercer_numero>segundo_numero>cuarto_numero:
    print("orden de menor a mayor:" +str(cuarto_numero)+str(segundo_numero)+str(tercer_numero)+str(primer_numero)+str(quinto_numero))
elif quinto_numero>primer_numero>tercer_numero>cuarto_numero>segundo_numero:
    print("orden de menor a mayor:" +str(segundo_numero)+str(cuarto_numero)+str(tercer_numero)+str(primer_numero)+str(quinto_numero))
elif segundo_numero>cuarto_numero>tercer_numero>quinto_numero>primer_numero:
    print("orden de menor a mayor:" +str(primer_numero)+str(quinto_numero)+str(tercer_numero)+str(cuarto_numero)+str(segundo_numero))
elif segundo_numero>cuarto_numero>tercer_numero>primer_numero>quinto_numero:
    print("orden de menor a mayor:" +str(quinto_numero)+str(primer_numero)+str(tercer_numero)+str(cuarto_numero)+str(segundo_numero))
elif cuarto_numero>segundo_numero>tercer_numero>primer_numero>quinto_numero:
    print("orden de menor a mayor:" +str(quinto_numero)+str(primer_numero)+str(tercer_numero)+str(segundo_numero)+str(cuarto_numero))
elif cuarto_numero>segundo_numero>tercer_numero>quinto_numero>primer_numero:
    print("orden de menor a mayor:" +str(primer_numero)+str(quinto_numero)+str(tercer_numero)+str(segundo_numero)+str(cuarto_numero))
elif segundo_numero>quinto_numero>tercer_numero>primer_numero>cuarto_numero:
    print("orden de menor a mayor:" +str(cuarto_numero)+str(primer_numero)+str(tercer_numero)+str(quinto_numero)+str(segundo_numero))
elif segundo_numero>quinto_numero>tercer_numero>cuarto_numero>primer_numero:
    print("orden de menor a mayor:" +str(primer_numero)+str(cuarto_numero)+str(tercer_numero)+str(quinto_numero)+str(segundo_numero))
elif quinto_numero>segundo_numero>tercer_numero>primer_numero>cuarto_numero:
    print("orden de menor a mayor:" +str(cuarto_numero)+str(primer_numero)+str(tercer_numero)+str(segundo_numero)+str(quinto_numero))
elif quinto_numero>segundo_numero>tercer_numero>cuarto_numero>primer_numero:
    print("orden de menor a mayor:" +str(primer_numero)+str(cuarto_numero)+str(tercer_numero)+str(segundo_numero)+str(quinto_numero))
elif cuarto_numero>quinto_numero>tercer_numero>segundo_numero>primer_numero:
    print("orden de menor a mayor:" +str(primer_numero)+str(segundo_numero)+str(tercer_numero)+str(quinto_numero)+str(cuarto_numero))
elif cuarto_numero>quinto_numero>tercer_numero>primer_numero>segundo_numero:
    print("orden de menor a mayor:" +str(segundo_numero)+str(primer_numero)+str(tercer_numero)+str(quinto_numero)+str(cuarto_numero))
elif quinto_numero>cuarto_numero>tercer_numero>segundo_numero>primer_numero:
    print("orden de menor a mayor:" +str(primer_numero)+str(segundo_numero)+str(tercer_numero)+str(cuarto_numero)+str(quinto_numero))
elif quinto_numero>cuarto_numero>tercer_numero>primer_numero>segundo_numero:
    print("orden de menor a mayor:" +str(segundo_numero)+str(primer_numero)+str(tercer_numero)+str(cuarto_numero)+str(quinto_numero))
elif primer_numero>segundo_numero>cuarto_numero>tercer_numero>quinto_numero:
    print("orden de menor a mayor:" +str(quinto_numero)+str(tercer_numero)+str(cuarto_numero)+str(segundo_numero)+str(primer_numero))
elif primer_numero>segundo_numero>cuarto_numero>quinto_numero>tercer_numero:
     print("orden de menor a mayor:" +str(tercer_numero)+str(quinto_numero)+str(cuarto_numero)+str(segundo_numero)+str(primer_numero))
elif segundo_numero>primer_numero>cuarto_numero>quinto_numero>tercer_numero:
     print("orden de menor a mayor:" +str(tercer_numero)+str(quinto_numero)+str(cuarto_numero)+str(primer_numero)+str(segundo_numero))
elif segundo_numero>primer_numero>cuarto_numero>tercer_numero>quinto_numero:
      print("orden de menor a mayor:" +str(quinto_numero)+str(tercer_numero)+str(cuarto_numero)+str(primer_numero)+str(segundo_numero))
elif primer_numero>tercer_numero>cuarto_numero>quinto_numero>segundo_numero:
      print("orden de menor a mayor" +str(segundo_numero)+str(quinto_numero)+str(cuarto_numero)+str(tercer_numero)+str(primer_numero))
elif primer_numero>tercer_numero>cuarto_numero>segundo_numero>quinto_numero:
      print("orden de menor a mayor:" +str(quinto_numero)+str(segundo_numero)+str(cuarto_numero)+str(tercer_numero)+str(primer_numero))
elif tercer_numero>primer_numero>cuarto_numero>quinto_numero>segundo_numero:
     print("orden de menor a mayor:" +str(segundo_numero)+str(quinto_numero)+str(cuarto_numero)+str(primer_numero)+str(tercer_numero))
elif tercer_numero>primer_numero>cuarto_numero>segundo_numero>quinto_numero:
     print("orden de menor a mayor:" +str(quinto_numero)+str(segundo_numero)+str(cuarto_numero)+str(primer_numero)+str(tercer_numero))
elif primer_numero>quinto_numero>cuarto_numero>segundo_numero>tercer_numero:
     print("orden de menor a mayor:" +str(tercer_numero)+str(segundo_numero)+str(cuarto_numero)+str(quinto_numero)+str(primer_numero))
elif primer_numero>quinto_numero>cuarto_numero>tercer_numero>segundo_numero:
     print("orden de menor a mayor:" +str(segundo_numero)+str(tercer_numero)+str(cuarto_numero)+str(quinto_numero)+str(primer_numero))
elif quinto_numero>primer_numero>cuarto_numero>segundo_numero>tercer_numero:
     print("orden de menor a mayor:" +str(tercer_numero)+str(segundo_numero)+str(cuarto_numero)+str(primer_numero)+str(quinto_numero))
elif quinto_numero>primer_numero>cuarto_numero>tercer_numero>segundo_numero:
     print("orden de menor a mayor:" +str(segundo_numero+str(tercer_numero)+str(cuarto_numero)+str(primer_numero)+str(quinto_numero)))
elif tercer_numero>segundo_numero>cuarto_numero>quinto_numero>primer_numero:
     print("orden de menor a mayor:" +str(primer_numero)+str(quinto_numero)+str(cuarto_numero)+str(segundo_numero)+str(tercer_numero))
elif tercer_numero>segundo_numero>cuarto_numero>primer_numero>quinto_numero:
     print("orden de menor a mayor:" +str(quinto_numero)+str(primer_numero)+str(cuarto_numero)+str(segundo_numero)+str(tercer_numero))
elif segundo_numero>tercer_numero>cuarto_numero>quinto_numero>primer_numero:
     print("orden de menor a mayor:" +str(primer_numero)+str(quinto_numero)+str(cuarto_numero)+str(tercer_numero)+str(segundo_numero))
elif segundo_numero>tercer_numero>cuarto_numero>primer_numero>quinto_numero:
     print("orden de menor a mayor:" +str(quinto_numero)+str(primer_numero)+str(cuarto_numero)+str(tercer_numero)+str(segundo_numero))
elif segundo_numero>quinto_numero>cuarto_numero>primer_numero>tercer_numero:
     print("orden de menor a mayor:" +str(tercer_numero)+str(primer_numero)+str(cuarto_numero)+str(quinto_numero)+str(segundo_numero))
elif segundo_numero>quinto_numero>cuarto_numero>tercer_numero>primer_numero:
     print("orden de menor a mayor:" +str(primer_numero)+str(tercer_numero)+str(cuarto_numero)+str(quinto_numero)+str(segundo_numero))
elif quinto_numero>segundo_numero>cuarto_numero>tercer_numero>primer_numero:
     print("orden de menor a mayor:" +str(primer_numero)+str(tercer_numero)+str(cuarto_numero)+str(segundo_numero)+str(quinto_numero))
elif quinto_numero>segundo_numero>cuarto_numero>primer_numero>tercer_numero:
     print("orden de menor a mayor:" +str(tercer_numero)+str(primer_numero)+str(cuarto_numero)+str(segundo_numero)+str(quinto_numero))
elif tercer_numero>quinto_numero>cuarto_numero>primer_numero>segundo_numero:
     print("orden de menor a mayor:" +str(segundo_numero)+str(primer_numero)+str(cuarto_numero)+str(quinto_numero)+str(tercer_numero))
elif tercer_numero>quinto_numero>cuarto_numero>segundo_numero>primer_numero:
     print("orden de menor a mayor:" +str(primer_numero)+str(segundo_numero)+str(cuarto_numero)+str(quinto_numero)+str(tercer_numero))
elif quinto_numero>tercer_numero>cuarto_numero>segundo_numero>primer_numero:
     print("orden de menor a mayor:" +str(primer_numero)+str(segundo_numero)+str(cuarto_numero)+str(tercer_numero)+str(quinto_numero))
elif quinto_numero>tercer_numero>cuarto_numero>primer_numero>segundo_numero:
     print("orden de menor a mayor:" +str(segundo_numero)+str(primer_numero)+str(cuarto_numero)+str(tercer_numero)+str(quinto_numero))
elif primer_numero>segundo_numero>quinto_numero>tercer_numero>cuarto_numero:
     print("orden de menor a mayor:" +str(cuarto_numero)+str(tercer_numero)+str(quinto_numero)+str(segundo_numero)+str(primer_numero))
elif primer_numero>segundo_numero>quinto_numero>cuarto_numero>tercer_numero:
     print("orden de mayor a menor:" +str(primer_numero)+str(segundo_numero)+str(quinto_numero)+str(cuarto_numero)+str(tercer_numero))
elif segundo_numero>primer_numero>quinto_numero>cuarto_numero>tercer_numero:
     print("orden de mayor a menor:" +str(segundo_numero)+str(primer_numero)+str(quinto_numero)+str(cuarto_numero)+str(tercer_numero))
elif segundo_numero>primer_numero>quinto_numero>tercer_numero>cuarto_numero:
    print("orden de mayor a menor:" +str(segundo_numero)+str(primer_numero)+str(quinto_numero)+str(tercer_numero)+str(cuarto_numero))
elif primer_numero>tercer_numero>quinto_numero>segundo_numero>cuarto_numero:
    print("orden de menor a mayor:" +str(cuarto_numero)+str(segundo_numero)+str(quinto_numero)+str(tercer_numero)+str(primer_numero))
elif primer_numero>tercer_numero>quinto_numero>cuarto_numero>segundo_numero:
    print("orden de menor a mayor:" +str(primer_numero)+str(tercer_numero)+str(quinto_numero)+str(tercer_numero)+str(primer_numero))
elif tercer_numero>primer_numero>quinto_numero>segundo_numero>cuarto_numero:
    print("orden de menor a mayor:" +str(cuarto_numero)+str(segundo_numero)+str(quinto_numero)+str(primer_numero)+str(tercer_numero))
elif primer_numero>cuarto_numero>quinto_numero>tercer_numero>segundo_numero:
    print("orden de menor a mayor:" +str(segundo_numero)+str(tercer_numero)+str(quinto_numero)+str(cuarto_numero)+str(primer_numero))
elif primer_numero>cuarto_numero>quinto_numero>segundo_numero>tercer_numero:
    print("orden de menor a mayor:" +str(tercer_numero)+str(segundo_numero)+str(quinto_numero)+str(cuarto_numero)+str(primer_numero))
elif segundo_numero>tercer_numero>quinto_numero>cuarto_numero>primer_numero:
    print("orden de menor a mayor:" +str(primer_numero)+str(cuarto_numero)+str(quinto_numero)+str(tercer_numero)+str(segundo_numero))
elif segundo_numero>tercer_numero>quinto_numero>primer_numero>cuarto_numero:
    print("orden de menor a mayorr:" +str(cuarto_numero)+str(primer_numero)+str(quinto_numero)+str(tercer_numero)+str(segundo_numero))
elif tercer_numero>segundo_numero>quinto_numero>primer_numero>cuarto_numero:
    print("orden de menor a mayor:" +str(cuarto_numero)+str(primer_numero)+str(quinto_numero)+str(segundo_numero)+str(tercer_numero))
elif tercer_numero>segundo_numero>quinto_numero>cuarto_numero>primer_numero:
    print("orden de menor a mayor:" +str(primer_numero)+str(cuarto_numero)+str(quinto_numero)+str(segundo_numero)+str(tercer_numero))
elif segundo_numero>cuarto_numero>quinto_numero>tercer_numero>primer_numero:
    print("orden de menor a mayor:" +str(primer_numero)+str(tercer_numero)+str(quinto_numero)+str(cuarto_numero)+str(segundo_numero))
elif segundo_numero>cuarto_numero>quinto_numero>primer_numero>tercer_numero:
    print("orden de menor a mayor:" +str(tercer_numero)+str(primer_numero)+str(quinto_numero)+str(cuarto_numero)+str(segundo_numero))
elif cuarto_numero>segundo_numero>quinto_numero>tercer_numero>primer_numero:
    print("orden de menor a mayor:" +str(primer_numero)+str(tercer_numero)+str(quinto_numero)+str(segundo_numero)+str(cuarto_numero))
elif cuarto_numero>segundo_numero>quinto_numero>primer_numero>tercer_numero:
    print("orden de menor a mayor:" +str(tercer_numero)+str(primer_numero)+str(quinto_numero)+str(segundo_numero)+str(cuarto_numero))
elif tercer_numero>cuarto_numero>quinto_numero>segundo_numero>primer_numero:
    print("orden de menor a mayor:" +str(primer_numero)+str(segundo_numero)+str(quinto_numero)+str(cuarto_numero)+str(tercer_numero))
elif tercer_numero>cuarto_numero>quinto_numero>primer_numero>segundo_numero:
    print("orden de menor a mayor:" +str(segundo_numero)+str(primer_numero)+str(quinto_numero)+str(cuarto_numero)+str(tercer_numero))
elif tercer_numero>cuarto_numero>quinto_numero>segundo_numero>primer_numero:
    print("orden de menor a mayor:" +str(primer_numero)+str(segundo_numero)+str(quinto_numero)+str(cuarto_numero)+str(tercer_numero))
elif cuarto_numero>tercer_numero>quinto_numero>segundo_numero>primer_numero:
    print("orden de menor a mayor:" +str(primer_numero)+str(segundo_numero)+str(quinto_numero)+str(tercer_numero)+str(cuarto_numero))
elif cuarto_numero>tercer_numero>quinto_numero>primer_numero>segundo_numero:
    print("orden de menor a mayor:" +str(segundo_numero)+str(primer_numero)+str(quinto_numero)+str(tercer_numero)+str(cuarto_numero))

#La potencia del mayor número elevado al menor número
if primer_numero>segundo_numero and tercer_numero and cuarto_numero and quinto_numero:
    numero_mayor = primer_numero
elif segundo_numero>primer_numero and tercer_numero and cuarto_numero and quinto_numero:
    numero_mayor = segundo_numero
elif tercer_numero>primer_numero and segundo_numero and cuarto_numero and quinto_numero:
    numero_mayor = tercer_numero
elif cuarto_numero>primer_numero and segundo_numero and tercer_numero and quinto_numero:
    numero_mayor = cuarto_numero
elif quinto_numero>primer_numero and segundo_numero and tercer_numero and cuarto_numero:
    numero_mayor = quinto_numero
if primer_numero<segundo_numero and tercer_numero and cuarto_numero and quinto_numero:
    numero_menor = primer_numero
elif segundo_numero<primer_numero and tercer_numero and cuarto_numero and quinto_numero:
    numero_menor = segundo_numero
elif tercer_numero<primer_numero and segundo_numero and cuarto_numero and quinto_numero:
    numero_menor = tercer_numero
elif cuarto_numero<primer_numero and segundo_numero and tercer_numero and quinto_numero:
    numero_menor = cuarto_numero
elif quinto_numero>primer_numero and segundo_numero and tercer_numero and cuarto_numero:
    numero_menor = quinto_numero 
potencia_numero_mayor = numero_mayor**numero_menor
print("la potencia del numero mayor elevado al numero menor:"+str(potencia_numero_mayor))
#La raíz cúbica del menor número
if primer_numero<segundo_numero and tercer_numero and cuarto_numero and quinto_numero:
    numero_menor = primer_numero
elif segundo_numero<primer_numero and tercer_numero and cuarto_numero and quinto_numero:
    numero_menor = segundo_numero
elif tercer_numero<primer_numero and segundo_numero and cuarto_numero and quinto_numero:
    numero_menor = tercer_numero
elif cuarto_numero<primer_numero and segundo_numero and tercer_numero and quinto_numero:
    numero_menor = cuarto_numero
elif quinto_numero>primer_numero and segundo_numero and tercer_numero and cuarto_numero:
    numero_menor = quinto_numero 
raiz_cubica = numero_menor**(1/3)
print("La raiz cubica de el numero menor es:" +str(raiz_cubica))
```
Para no dormir en toda la noche solo hay que empezar a declarar las variables 
#### Promedio
para hallar el promedio la variable ```suma_numeros``` contiene los numeros ingresador por el usuario
luego se divide ```suma_numeros``` entre 5 ya que es la cantidad de numeros a promediar
#### media
para hallar la media toca encontrar el numero que este en la mitad, para esto usamos  ```if``` y ponemos los datos en ```elif``` escribimos las combinaciones que hay entre los 5 numeros 
#### orden de mayor a menor
usamos la misma estructura ```if``` y ```elif```
y organizamos los numeros 
#### orden de menor a mayor
con el mismo codigo para encontrar el orden de mayor a menor encontramos el orden de menor a mayor, solo hay que cambiar el orden escrito en el anterior codigo
#### Mayor número elevado al menor número
con ```if``` y ```else``` encontramos el mayor y el menor numero comparandolos 
al tener todos los numeros comparados 
usamos las variables y las multiplicamos 
```numero_mayor``` ** ```numero_menor```
#### Raiz cubica del numero menor**
usamos el mismo codigo que usamos para encontrar el numero menor 
y lo operamos para hallar la raiz cubica
```raiz_cubica = numero_menor**(1/3)```
