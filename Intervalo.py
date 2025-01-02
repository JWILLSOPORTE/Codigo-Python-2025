# Si x E <2;5], determina a que intervalo pertenece 6 x - 3
#Multiplicamos 𝑥 por 6 para obtener 6𝑥:
print("--------------")
print("Intervalo")
print("--------------")

print("¿Cúal es el número que deseas convertir?: ")
A = float(input("Primer valor: "))
print("¿Cúal es el segundo número que deseas convertir?: ")
B =  float(input("Segundo valor: "))

multiA = int( A * 6)
multiB = int ( B * 6)
resta_A = multiA - 3
resta_B = multiB - 3
Total = resta_A , resta_B


##Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print("El resultado del primer valor:", "<", multiA)
print("El resultado del segundo valor :", multiB ,"]")
print("Al restarlo su nuevo valor es:","<", resta_A)
print("Al restarlo su nuevo valor es:", resta_B,"]")
print("El intervalo seria :", Total,"]")




