# Definimos el polinomio
def P(x, m):
    return x**2 + 3*x + m
# x - 1 
# Usamos el teorema del residuo: P(1) debe ser igual a 6
# Despejamos m: P(1) = 6 -> 1^2 + 3*1 + m = 6 -> m = 2

print("¿Cúal es el número que deseas convertir?: ")
x_valor= float(input(" El valor de x : "))
# Calculamos m

print("¿Cúal es el residuo? deseado: ")
residuo_deseado = int (input("resisudo: "))

#residuo_deseado = 6

# Calculamos m a partir de la ecuación
m = int(residuo_deseado - (x_valor**2 + 3*x_valor))

# Mostramos el valor de m y m al cuadrado
print(f"El valor de m es: {m}")
print(f"El valor de m^2 es: {m**2}")
print("El valor de m^2 es:", m**2)
