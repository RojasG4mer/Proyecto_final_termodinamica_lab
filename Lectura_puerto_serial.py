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


df = pd.DataFrame(columns = ['Tiempo', 'Temperatura'])

try:
    while (time.time() - tiempo_inicio) < (tiempo_lectura_minutos * 60):
        cad = serialArduino.readline().decode('ascii')
        print(cad)
        num = cad.split(', ')
        num = [float(numero) for numero in num]
        new_row = pd.DataFrame({'Tiempo': [num[0]], 'Temperatura': [num[1]]})
        df = pd.concat([df, new_row], ignore_index=True)
        archivo.write(cad) #pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
except KeyboardInterrupt:
    print("Interrupción del usuario. Cerrando el puerto serial y guardando datos...")

# Cierra el archivo y el puerto serial
archivo.close()
serialArduino.close()

df_txt = pd.read_csv('C:\\Users\\jonat.JONATHANROJAS\\Desktop\\SENSOR_temperatura\\prueba.txt', sep = ',', header = None)
##Cambiamos el nombre de las columnas para fácil identificación
n_cols = ['Tiempo', 'Temperatura']
df_txt.columns = n_cols
columnas = list(df_txt.columns)


df['Tiempo'] = df['Tiempo']/1000
df.to_csv("Prueba_01_01.csv", index=False)


plt.scatter(df['Tiempo'], df['Temperatura'], color = 'g')
plt.xlabel('Tiempo ($s$)')
plt.ylabel('Temperatura ($^{\circ}K$)')
plt.title('Intento')
plt.show()


