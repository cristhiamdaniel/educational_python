# -*- coding: utf-8 -*-
"""python_manuel.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NPo9npfZEtCmwkRzi5G7_4mZcM7UtDm5

https://www.youtube.com/playlist?list=PLh7JzoyIyU4K5LvqP1zyn_kJ4IospXvt4

NIVEL 6: BUCLES

Reto 1: Mientras

Programa que muestre en pantalla una secuencia de números del 20 al 0.
"""

n = 20
while n >= 0:
  print(n)
  n = n - 1
print("Fin del programa")

"""Reto 2: Hasta que queramos

Programa que te pide que introduzcas un número que esté entre el 10 y el 20. Si es correcto te diga que estás en el rango, y te pida otro. Hasta que le des un número fuera del rango y se acabe el programa.

"""

n = int(input("Introduce un número entre el 10 y el 20: "))
while n >= 10 and n <= 20:
  print("Estás en el rango")
  print()
  n = int(input("Introduce otro número entre el 10 y el 20: "))

print("Fin del programa")

"""  Reto 3: Usando un contador

  Programa que te pide que adivines un número del 1 al 10 y te pida números constantemente hasta que lo adivines. Añade un contador que te diga los intentos que has necesitado. Conviene que crees tres variables, y utiliza un "else".
"""

numero = 5 # El número que se debe adivinar
n = int(input("Ingresa un número entre 1 y 10: "))
contador = 1

while n != numero:
  print("Número incorrecto")
  n = int(input("Ingresa otro número entre 1 y 10: "))
  contador = contador + 1
else:
  print("Felicidades, adivinaste el número")
  print("lo hiciste en", contador, "intentos")

"""RETO 5: Sumando números de un intervalo

Programa que suma los números pares que hay entre 1 y el 20
"""

li = int(input("Ingresa el límite inferior: "))
ls = int(input("Ingresa el límite superior: "))

pares = 2*li
suma = 0

while pares <= ls:
  suma = suma + pares
  pares += 2

print('La suma de los números pares que hay entre {} y {} es {}'.format(li,ls,suma))

"""NIVEL 6: INTRODUCE LA CONTRASEÑA

Programa que pide el usuario y la contraseña.
Si no pones los dos correctamente te los vuelve a pedir.
"""

user = 'cristhiamdaniel'
pas = '12345'

u = input("Introduce el usuario: ")
p = input("Introduce la contraseña: ")

while u != user or p != pas:
  print("Datos incorrectos")
  u = input("Introduce el usuario: ")
  p = input("Introduce la contraseña: ")

print("Datos correctos")

"""  RETO 8: PLANTANDO UNA BANDERA

  Juego que pregunta un número del 1 al 5 y luego una vocal.
  Tienes 100 puntos, si aciertas uno de ellos te quita 2 puntos, si no aciertas ninguno te quita 5 puntos. El programa no se acaba hasta que aciertes los dos. Cuando se acaba el programa te dice los puntos que te quedan,
"""

number = 3
vowel = 'a'
points = 100

n = int(input("Ingresa un número entre el 1 y el 5: "))
v = str(input("Ingresa una vocal: "))

if n != number and v != vowel:
  points = points - 5
  n = int(input("Ingresa un nuevo número entre el 1 y el 5: "))
  v = str(input("Ingresa una nueva vocal: "))
if n != number or v != vowel:
  points = points - 2
  n = int(input("Ingresa un nuevo número entre el 1 y el 5: "))
  v = str(input("Ingresa una nueva vocal: "))
print("Acertaste")
print('Tu puntaje es {}'.format(points))

