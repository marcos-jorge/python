
#Descripción    : Crea una matriz de tamaño NxN y la llena con números aleatorios entre 0 y 9. 
#Fecha creación : 24-07-2023
#Autor          : Marcos Jorge Varela

import random

def crearMatriz(n):
    matriz = []
    for x in range(n):
        fila = []
        for x in range(n):
            fila.append(random.randint(0, 9))
        matriz.append(fila)
    return matriz

def mostrarMatriz(matriz):
    for fila in matriz:
        print(fila)

def sumaFilas(matriz):
    suma_filas = []
    for fila in matriz:
        suma_filas.append(sum(fila))
    return suma_filas

def sumaColumnas(matriz):
    suma_columnas = []
    for j in range(len(matriz[0])):
        suma_columna = 0
        for i in range(len(matriz)):
            suma_columna += matriz[i][j]
        suma_columnas.append(suma_columna)
    return suma_columnas

#Mientras no se ingrese un numero entero positivo se sigue pidiedo que se ingrese un numero
while True:
    try:
        n_tamanio = int(input("Ingrese el tamaño de la matriz: "))
        if n_tamanio <= 0:
            raise ValueError
        break
    except ValueError:
        print("Error: el tamaño de la matriz debe ser un número entero positivo.")


#Esta función genera la matriz con el tamaño ingresado por el usuario
matriz = crearMatriz(n_tamanio)

#Se muestra la matriz creada por pantalla
print("Matriz creada:")
mostrarMatriz(matriz)

#Calcula la suma de todos los valores de la fila
suma_filas = sumaFilas(matriz)

#Calcula la suma de todos los valores de la columna
suma_columnas = sumaColumnas(matriz)

#Mustra por pantalla la suma de cada fila
print("La suma de cada fila es:")
print(suma_filas)

#Mustra por pantalla la suma de cada columna
print("La suma de cada columna es:")
print(suma_columnas)

