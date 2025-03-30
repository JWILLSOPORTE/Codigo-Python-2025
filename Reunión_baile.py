# En una reunión las 2/3 eran varones. De las mujeres 2/3 eran casadas y 6 solteras. ¿Cuánto
# representa la tercera parte del total de hombres?

from fractions import Fraction
personas = "x"
varones = Fraction(2,3) 
mujeres  = Fraction(1,3)

# Dato 2 
mujeres_casadas = Fraction (2,3)
mujeres_solteras =  Fraction (1,3) / 6

# Número de asistentes a la reunión  .

personas = (mujeres * mujeres_solteras) 

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

