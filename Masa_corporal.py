#Decoración: Nombre del Algoritmo
print("-------------")
print("MASA CORPORAL")
print("-------------")

#Datos
def calcular_imc(peso,altura):
    return peso / ( altura ** 2)
#Entradas
print("Ingrese su peso: ")
peso = float(input ( "peso (kg):"))
print("Ingrese su altura: ")
altura = float(input ( "altura (ma):"))
imc = calcular_imc(peso, altura)
print("\nSALIDA: ")
print("-------------------------------------------------------")
print ( " Tu imc es :", imc)