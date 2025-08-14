#Decoración: Nombre del Algoritmo
# De 120 personas, se sabe que 71 son solteros y 55 son hombres,
# si son 12 mujeres casdas¿Cuántos son los hombres casados?
print("--------------")
print("Hombres Casados")
print("--------------")
#Entradas
print("Ingrese Total de personas ")
A = float(input("Total  es: "))
print("Ingrese Total de Hombres: ")
B = float(input("Total es : "))
print("Ingrese el número casadas: ")
C = float(input("Mujeres casadas: "))
print("Ingrese el número de solteros: ")
D = float(input("Total solteros: "))
#DATOS

Total_mujeres = A - B
Mujeres_solteras = Total_mujeres - C
Hombres_solteros = D - Mujeres_solteras
Hombres_casados = B - Hombres_solteros

##Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print("Total de mujeres es:",Total_mujeres)
print(f"Total mujeres solteras: {Mujeres_solteras:.2f}")
print(f"Total hombres solteros: {Hombres_solteros:.2f}")
print(f"Total hombres casados: {Hombres_casados:.2f}")
print(f"Total hombres casados: {Hombres_casados:.2f}")

