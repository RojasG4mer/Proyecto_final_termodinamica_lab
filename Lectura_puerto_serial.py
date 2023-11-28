# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 13:34:27 2023

@author: ROJAS MARTINEZ JONATHAN FRANCISCO
"""
import time
import serial
import pandas as pd
import matplotlib.pyplot as plt

#Creamos el dataframe para la lectura de los datos
df = pd.DataFrame(columns = ['Tiempo', 'Temperatura'])

# Abre el puerto serial
serialArduino = serial.Serial('COM3', 9600)
time.sleep(1)

# Define el tiempo de lectura en minutos
tiempo_lectura_minutos = 15  # Cambia el valor a la cantidad de minutos que desees

# Obtiene el tiempo de inicio
tiempo_inicio = time.time()

#Iniciamos un try - except para que se ejecute la lectura del puerto y si interrumpimos el kernel se guarden los datos y no se pierdan
try:
    while (time.time() - tiempo_inicio) < (tiempo_lectura_minutos * 60):
        cad = serialArduino.readline().decode('ascii')
        print(cad)
        num = cad.split(', ') # Separamos los datos en los dos numeros
        num = [float(numero) for numero in num] #Hacemos los numeros a flotantes
        new_row = pd.DataFrame({'Tiempo': [num[0]], 'Temperatura': [num[1]]}) #Esta es la nueva columna 
        df = pd.concat([df, new_row], ignore_index=True) #Agregamos los nuevos datos al dataframe
except KeyboardInterrupt:
    print("Interrupción del usuario. Cerrando el puerto serial y guardando datos...")

# Cierra el archivo y el puerto serial
serialArduino.close()

df['Tiempo'] = df['Tiempo']/1000 # Cambiamos de milisegundos a segundos
df.to_csv("Prueba_01_10.csv", index=False) #Guardamos los datos en csv

## Graficamos los datos obtenidos
plt.scatter(df['Tiempo'], df['Temperatura'], color = 'g')
plt.xlabel('Tiempo ($s$)')
plt.ylabel('Temperatura ($^{\circ}K$)')
plt.title('Intento 02 ')
plt.grid()
plt.show()
