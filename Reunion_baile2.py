# En una reunión las 2/3 eran varones. De las mujeres 2/3 eran casadas y 6 solteras. ¿Cuánto
# representa la tercera parte del total de hombres?

from fractions import Fraction


print("Fracción de varones: ")
varones = Fraction(input("varones : "))
print("Fracción de mujeres: ")
mujeres = Fraction(input("mujeres : "))

# Dato 2 
print("Fracción de mujeres casadas: ")
mujeres_casadas = Fraction(input("casadas : "))
print("Fracción de mujere solteras: ")
mujeres_solteras = Fraction(input("solteras : "))/6

# Número de asistentes a la reunión  .

personas = Fraction (mujeres) * (mujeres_solteras)


asistentes = 1/personas

Total_varones = varones * asistentes
Total_mujeres = mujeres * asistentes
Tercera_parte_varones = Total_varones * 1/3

##Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print("El número de asistentes  es:", asistentes)
print("El número de total de varones:", Total_varones)
print("El número de total de mujeres :", Total_mujeres)
print("La tercera parte de varones es :", Tercera_parte_varones)




