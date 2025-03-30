from fractions import Fraction
Equi1 = Fraction(2,3)
Equi2  = Fraction(3,4)
Equi3  = Fraction(7,12)

Resta = Equi2 - Equi3
suma =  (Equi1 + Resta)*1/2
print ( Resta)
print ( suma)

X = 1/suma
resultado = int(X)

##Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print("Tiempo de llenado de ambos tanques es:", X)
print(f"Tiempo de llenado de ambos tanques es: {X:.2f}")

