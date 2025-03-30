#Un tanque para almacenar agua, para ser llenado con el caño A en 10 minutos, 
#con el caño B en 15 minutos, y con el caño C en 30 minutos 
#¿En cuantos minutos llenaran todo el tanque trabajando los 3 caños a la vez?


#Decoración: Nombre del Algoritmo
print("--------------")
print("Tanque de Agua")
print("--------------")
#Entradas
print("Ingrese primer valor TANQUE A: ")
A = float(input("TANQUE A: "))
print("Ingrese segundo valor TANQUE B: ")
B = float(input("TANQUE B: "))
print("Ingrese segundo valor TANQUE C: ")
C = float(input("TANQUE C: "))
#DATOS
#CAÑO A EN 10 HORAS
#CAÑO B EN 15 HORAS
#CAÑO C EN 30 HORAS
#Proceso
S = ((1/A) + (1/B) + (1/C))
R = (1 / S)

horas = int(R)
m = int((R - horas) * 60)

##Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print("Tiempo de llenado de ambos tanques es:", R)
print(f"Tiempo de llenado de ambos tanques es: {R:.2f}","horas")
print(f"Tiempo de llenado de ambos tanques es: {m:.2f}","minutos")
