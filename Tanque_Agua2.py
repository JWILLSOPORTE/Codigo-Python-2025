# Un caño de agua puede ser llenado por un caño A en 6 horas,por el caño B en "x" horas.Si existe un desagüe
# que lo puede vaciar en 12 horas. Hallar el tiempo que puede llenar el tanque el Caño B, 
# si el tanque se llena en 4 horas con los caños y el desagüe abiertos.

#Decoración: Nombre del Algoritmo
print("--------------")
print("Tanque de Agua")
print("--------------")
#Entradas
print("Ingrese tiempo de llenado del caño A: ")
A = float(input("CAÑO A: "))
print("Ingrese tiempo de vaciado del caño C: ")
C = float(input("CAÑO C: "))
print("Ingrese tiempo completo del llenado del tanque: ")
D = float(input("Tiempo completo: "))
#Resolución:
#CAÑO A EN 6 HORAS
#CAÑO B EN x HORAS
#CAÑO C EN 12 HORAS
# total se llena en 4 horas
#Proceso
S = ((1/D) + (1/C) - (1/A))
x = (1 / S)

horas = int(x)
m = int((x - horas) * 60)

##Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print("Tiempo de llenado de ambos tanques es:", x)
print(f"Tiempo de llenado de ambos tanques es: {x:.2f}","horas")
print(f"Tiempo de llenado de ambos tanques es: {m:.2f}","minutos")