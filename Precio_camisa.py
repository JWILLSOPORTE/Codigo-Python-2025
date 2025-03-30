#Un sastre vende 2 camisas a S/.60 cada una. En una camisa gana 1/4 de los que le costó, y
#en la otra pierde 1/4 de lo que le costó hacerla. ¿Cuánto ganó o perdió en la venta?

def calcular_costo_A(precio_venta, porcentaje_ganancia):
    costoA = precio_venta / (1 + porcentaje_ganancia)
    return costoA
def calcular_costo_B(precio_venta, porcentaje_perdida):
    costoB = precio_venta / (1 - porcentaje_perdida)
    return costoB
def calcular_ganancia(costoA, precio_venta):
    ganancia = precio_venta - costoA
    return ganancia
def calcular_pérdida(costoB, precio_venta):
    pérdida = precio_venta - costoB
    return pérdida
# Función principal
def main():
    # Datos conocidos
    precio_venta = 60  # Precio al que se vendió la casa
    porcentaje_ganancia = 1 / 4  # Ganancia como fracción
    porcentaje_perdida = 1 / 4  # Ganancia como fracción

    # Calcular el costo de la casa
    costo_camisa_A = calcular_costo_A(precio_venta, porcentaje_ganancia)
    costo_camisa_B = calcular_costo_B(precio_venta, porcentaje_perdida)
    # Calcular ganacia y pérdida
    Ganancia_A = calcular_ganancia(costo_camisa_A, precio_venta)
    Pérdida_B = calcular_pérdida(costo_camisa_B, precio_venta)

    # Mostrar resultados
    
    print(f"El costo original de la camisa fue: S/.{costo_camisa_A:.2f}")
    print(f"La ganacia en la venta camisa A fue: S/.{Ganancia_A:.2f}")
    print(f"El costo original de la casa fue: S/.{costo_camisa_B:.2f}")
    print(f"El pérdia en la venta camisa B fue: S/.{Pérdida_B:.2f}")

# Llamar a la función principal
main()
