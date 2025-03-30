def calcular_dias_deportes(natacion, atletismo, dias_mes):
    """
    Calcula los días en los que Roberto practica ambos deportes, solo natación, y solo atletismo.

    Args:
        natacion (float): Días que practica natación.
        atletismo (float): Días que practica atletismo.
        dias_mes (float): Total de días en el mes.

    Returns:
        tuple: Días que practica ambos deportes, solo natación, y solo atletismo.
    """
    ambos_deportes = natacion + atletismo - dias_mes
    solo_natacion = natacion - ambos_deportes
    solo_atletismo = atletismo - ambos_deportes
    return ambos_deportes, solo_natacion, solo_atletismo

# Entradas

natacion = float(input("Días de natación: "))
atletismo = float(input("Días de atletismo: "))
dias_mes = float(input("Días del mes de diciembre: "))

# Proceso
ambos_deportes, solo_natacion, solo_atletismo = calcular_dias_deportes(natacion, atletismo, dias_mes)

# Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print(f"Días que practica ambos deportes: {ambos_deportes:.2f}")
print(f"Días que solo practica natación: {solo_natacion:.2f}")
print(f"Días que solo practica atletismo: {solo_atletismo:.2f}")
print(f"Días que solo practica atletismo (redondeado): {int(solo_atletismo)}")