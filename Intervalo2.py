# Si x E <2;5], determina a que intervalo pertenece 2 x  +4
#Multiplicamos 𝑥 por 6 para obtener 6𝑥:
print("--------------")
print("Intervalo 2")
print("--------------")

print("¿Cúal es el número que deseas convertir?: ")
A = int(input("Primer valor: "))
print("¿Cúal es el segundo número que deseas convertir?: ")
B = int (input("Segundo valor: "))

multiA =  A * 2
multiB =   B * 2
resta_A = multiA + 4
resta_B = multiB + 4
Total = resta_A , resta_B

##Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print("El resultado del primer valor:", "<", multiA)
print("El resultado del segundo valor :", multiB ,"]")
print("Al restarlo su nuevo valor es:","<", resta_A)
print("Al restarlo su nuevo valor es:", resta_B,"]")
print("El intervalo seria :", "<" ,(Total) ,"]")