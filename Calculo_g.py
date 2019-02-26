#-*-coding: utf-8-*-
import re
import numpy as np
import matplotlib.pyplot as plt
  
#***TALLER DE ELEMENTOS DE FISICA***


#Creamos una lista que obtendrá los resultados de g en los 7 videos 
resultados=[]
#Hallamos g en el primer video, que cuenta con un factor de conversion diferente al de los demás
#1 fotograma = 1/28 seg
#1 pixel = 1/700 metros
f= open("Trajectories/trajectory1.dat", "r")

list_time = [0]
list_position = [0]
for line in f:
    line_1 = re.findall('\w+', line)
    list_time.append(float(line_1[0])*(1/28))
    list_position.append(float(line_1[2])*(1/700))


coeficientes = np.polyfit(list_time, list_position, 2)

g = 2.*coeficientes[0]
resultados.append(g)
f.close()

#Hallamos g en los otros seis videos, que cuentan con un factor de conversion equivalente
#1 fotograma = 1/32
#1 pixel = 1/747 seg
for i in range(6):

    trajectory = "trajectories/trajectory"+str(i+2)+".dat"
    f_1 = open(trajectory, "r")
    list_time_1 = []
    list_position_1 = []
    for line in f_1:
        line_1 = re.findall('\w+', line)
        list_time_1.append(float(line_1[0])*(1/32))
        list_position_1.append(float(line_1[2])*(1/747))


    coeficientes_1 = np.polyfit(list_time_1, list_position_1, 2)

    g_1 = 2.*coeficientes_1[0]
    resultados.append(g_1)
    f_1.close()
    

#Cálculo de la media aritmetica para poder encontrar las desviaciones respecto a la media:
suma=0
for i in range(7):
    suma += resultados[i]
media_arit = suma/7.
print("Promedio: "+str(media_arit)+("\n"))


#Ahora calculamos la desviacion estandar
aux_de =0
for i in resultados:
    x=(i-media_arit)
    aux_de+= pow(x,2)
aux_de = aux_de/7
desviacion_estandar = pow(aux_de, 0.5)

print("Desviación estándar: "+str(desviacion_estandar)+"\n")


#Ahora compararemos el valor medido de g con: g= GM/R^2
#con M: masa de la tierra
#    G: constante gravitacional
#    R: radio de la tierra en el ecuador

M=5.972*pow(10,24)
G=6.67392*(pow(10,-11))
R=6378000
g_est = (M*G)/(pow(R,2))
print(g_est)


#Creamos grafica de Altura vs Tiempo
x = list_time
y = list_position

y1 = []

for i in x:
    y1.append((4.9)*(pow(i,2)))
plt.figure()
plt.xlabel(r"$Time(s)$", fontsize = 24, color = 'black')
plt.ylabel(r"$Position(m)$", fontsize = 24, color = 'black')

plt.plot(x, y, 'm-', linewidth = 2, label = 'G calculada')
plt.plot(x, y1, 'c-', linewidth = 2, label = 'G estándar')
plt.legend(loc = 4)
plt.show()