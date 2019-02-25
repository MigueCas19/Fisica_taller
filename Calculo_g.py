#-*-coding: utf-8-*-
import re
import numpy
#***TALLER DE ELEMENTOS DE FISICA***

resultados=[]
#Hallamos g en el primer video, que cuenta con un factor de conversion diferente al de los demás
#1 fotograma = 1/25 seg
#1 pixel = 1/695 metros
f= open("Trajectories/trajectory1.dat", "r")

list_time = []
aux_list_position = []
for line in f:
    line_1 = re.findall('\w+', line)
    list_time.append(float(line_1[0])*(1/25))
    aux_list_position.append(float(line_1[2])*(1/695))

list_position = []
for i in aux_list_position[::-1]:
    list_position.append(i)

coeficientes = numpy.polyfit(list_time, list_position, 2)

g = 2.*coeficientes[0]
resultados.append(g)
f.close()

#Hallamos g en los otros seis videos, que cuentan con un factor de conversion equivalente
#1 fotograma = 1/32
#1 pixel = 1/750 seg
for i in range(5):

    trajectory = "trajectories/trajectory"+str(i+2)+".dat"
    f_1 = open(trajectory, "r")
    list_time_1 = []
    aux_list_position_1 = []
    for line in f_1:
        line_1 = re.findall('\w+', line)
        list_time_1.append(float(line_1[0])*(1/32))
        aux_list_position_1.append(float(line_1[2])*(1/750))

    list_position_1 = []
    for i in aux_list_position_1[::-1]:
        list_position_1.append(i)

    coeficientes_1 = numpy.polyfit(list_time_1, list_position_1, 2)

    g_1 = 2.*coeficientes_1[0]
    resultados.append(g_1)
    f_1.close()
    

#Calculo de la media aritmetica para poder encontrar las desviaciones respecto a la media:
suma=0
for i in range(6):
    suma += resultados[i]
media_arit = suma/6.
#print(media_arit)

#Ahora calculamos la desviacion estandar
aux_de =0
for i in resultados:
    x=abs(i-media_arit)
    aux_de+= pow(x,2)
aux_de = aux_de/6
desviacion_estandar = pow(aux_de, 0.5)
print(desviacion_estandar)