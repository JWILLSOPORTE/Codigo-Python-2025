import math

# Coordenadas del punto (6, -8)


print("Ingrese Punto x: ")
x = float(input("x: "))
print("Ingrese Punto y: ")
y = float(input("y: "))

# Calcular el radio (hipotenusa) usando el teorema de Pitágoras
r = math.sqrt((x)**2 + (y)**2)

# Calcular coseno y tangente del ángulo β
cos = x / r
tan = y / x

# Calcular M usando la fórmula dada
M = 5 * cos + 6 * tan

# Mostrar el resultado
print("\nSALIDA: ")
print("-------------------------------------------------------")
print(f"El valor de M es: {M:.2f}")
