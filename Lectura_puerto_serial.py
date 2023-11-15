# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 13:34:27 2023

@author: ROJAS MARTINEZ JONATHAN FRANCISCO
"""
import time
import serial
import pandas as pd
import matplotlib.pyplot as plt


# Abre el archivo para escritura
archivo = open('C:\\Users\\jonat.JONATHANROJAS\\Desktop\\SENSOR_temperatura\\prueba.txt', 'w')

# Abre el puerto serial
serialArduino = serial.Serial('COM3', 9600)
time.sleep(1)

# Define el tiempo de lectura en minutos
tiempo_lectura_minutos = 15  # Cambia el valor a la cantidad de minutos que desees

# Obtiene el tiempo de inicio
tiempo_inicio = time.time()

try:
    while (time.time() - tiempo_inicio) < (tiempo_lectura_minutos * 60):
        cad = serialArduino.readline().decode('ascii')
        print(cad)
        archivo.write(cad)
except KeyboardInterrupt:
    print("Interrupción del usuario. Cerrando el puerto serial y guardando datos...")

# Cierra el archivo y el puerto serial
archivo.close()
serialArduino.close()

df = pd.read_csv('C:\\Users\\jonat.JONATHANROJAS\\Desktop\\SENSOR_temperatura\\prueba.txt', sep = ',', header = None)
##Cambiamos el nombre de las columnas para fácil identificación
n_cols = ['Tiempo', 'Temperatura']
df.columns = n_cols
columnas = list(df.columns)


df['Tiempo'] = df['Tiempo']/1000

plt.scatter(df.iloc[:, 0], df.iloc[:, 1], color = 'g')
plt.xlabel('Tiempo ($s$)')
plt.ylabel('Temperatura ($^{\circ}K$)')
plt.title('Intento')
plt.show()


