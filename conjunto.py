#Roberto en el mes de Diciembre practicará 16 días natación y 22 días atletismo.
#Hallar los días en los que solo nadará

print("--------------")
print("Conjunto_deportes")
print("--------------")
#Entradas
print("dias de natación: ")
natación = float(input("días: "))
print("dias de atletismo : ")
atletismo = float(input("días: "))
print("Dias del mes de diciembre: ")
dias_mes = float(input("días: "))
#DATOS
#16 días natación
#22 días atletismo
#Proceso
ambos_deportes = ((natación) + (atletismo) - (dias_mes))
solo_natación= natación - ambos_deportes
solo_atletismo= atletismo - ambos_deportes
##Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print("Días que practica ambos deportes:", ambos_deportes)
print(f"solo practica ntación: {solo_natación:.2f}")
print(f"solo practica atletismo: {solo_atletismo:.2f}")
print("solo practica atletismo:", int(solo_atletismo))
